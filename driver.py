import sys
from antlr4 import *
from output.baby_duck_grammarLexer import baby_duck_grammarLexer
from output.baby_duck_grammarParser import baby_duck_grammarParser
from Quadruple import Quadruple
from output.baby_duck_grammarListener import baby_duck_grammarListener
from output.baby_duck_grammarVisitor import baby_duck_grammarVisitor
from mem_tables import MemoryTable, FunctionID, Value
from vm import VirtualMachine
from SemanticCube import (
    Operator,
    Type,
    baby_duck_type_to_enum,
    parse_operator,
    parse_string,
    python_type_to_enum,
)


class Listener(baby_duck_grammarListener):
    def __init__(self, memory_table: MemoryTable):
        self.memory_table = memory_table
        self.variable_buffer = []
        self.function_id_stack = []

    def save_vars_to_memory(self, function_id: FunctionID):
        for var_id, var_type in self.variable_buffer:
            variable_value = Value(baby_duck_type_to_enum(var_type), None)
            self.memory_table[function_id]["$" + var_id] = variable_value
        self.variable_buffer = []

    def enterProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        self.function_id_stack.append(FunctionID("global", "void"))
        self.memory_table[FunctionID("global", "void")] = {}
        return super().enterProgram(ctx)

    def exitProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        return super().exitProgram(ctx)

    def enterProgram_post_var(
        self, ctx: baby_duck_grammarParser.Program_post_varContext
    ):
        current_function_id = self.function_id_stack.pop()

        self.save_vars_to_memory(current_function_id)
        return super().enterProgram_post_var(ctx)

    def exitString(self, ctx: baby_duck_grammarParser.StringContext):
        print("listener string: " + ctx.getText())
        return super().exitString(ctx)

    def enterFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        self.variable_buffer = []
        return super().enterFuncs(ctx)

    def exitFunction_id(self, ctx: baby_duck_grammarParser.Function_idContext):
        function_id = FunctionID(ctx.ID().getText(), ctx.type_().getText())
        self.function_id_stack.append(function_id)
        return super().exitFunction_id(ctx)

    def exitFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        current_function = self.function_id_stack.pop()
        self.memory_table[current_function] = {}

        self.save_vars_to_memory(current_function)
        self.variable_buffer = []
        return super().exitFuncs(ctx)

    def exitF_param_list(self, ctx: baby_duck_grammarParser.F_param_listContext):
        for param in ctx.f_param_list_helper():
            var_id = param.ID().getText()
            var_type = param.type_().getText()
            self.variable_buffer.append((var_id, var_type))
        return super().exitF_param_list(ctx)

    def exitVars_declarations(
        self, ctx: baby_duck_grammarParser.Vars_declarationsContext
    ):
        var_type = ctx.type_().getText()

        for id in ctx.ID():
            id_text = id.getText()
            self.variable_buffer.append((id_text, var_type))
        return super().exitVars_declarations(ctx)


def determine_type(ctx):
    if ctx.ID():
        return "VAR"
    if ctx.cte():
        return "CTE"


class Visitor(baby_duck_grammarVisitor):
    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.quadruples = []
            
    def visitFactor(self, ctx: baby_duck_grammarParser.FactorContext):
        if ctx.parenthesized_expression():
            # A parenthesized expression should be evaluated first.
            return self.visit(ctx.parenthesized_expression())
        else:
            unary_op = None
            result = None

            if ctx.factor_operator():  # If there is a unary operator present
                unary_op = ctx.factor_operator().getText()
                operand = ctx.getChild(1).getText()
            else:
                operand = ctx.getChild(0).getText()

            if unary_op:
                result = self.new_temporary()
                self.generate_quadruple(unary_op, operand, None, result)
            else:
                result = operand

        return result

    def generate_quadruple(self, operator, left_operand, right_operand, result) -> int:
        operator = parse_operator(operator)
        quad = Quadruple(
            operator=operator,
            left_operand=left_operand,
            right_operand=right_operand,
            result=result,
        )
        self.quadruples.append(quad)
        return len(self.quadruples) - 1

    def new_temporary(self):
        name = f"$t_{self.temp_counter}"
        self.temp_counter += 1
        return name

    def visitParenthesized_expression(
        self, ctx: baby_duck_grammarParser.Parenthesized_expressionContext
    ):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: baby_duck_grammarParser.ExpressionContext):
        left = self.visit(ctx.exp())
        if ctx.getChildCount() != 1:
            operator = ctx.rel_op().getText()
            right = self.visit(ctx.getChild(2))
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, left, right, temp_var)
            return temp_var

        return left

    def visitF_call(self, ctx: baby_duck_grammarParser.F_callContext):
        function_name = ctx.ID().getText()
        arg_count = 0
        # Check if there are arguments
        if ctx.f_call_helper() and ctx.f_call_helper().expression():
            arg_count = len(ctx.f_call_helper().expression())

            for arg in ctx.f_call_helper().expression():
                arg_result = self.visit(arg)
                self.generate_quadruple("param", arg_result, None, None)

        self.generate_quadruple("call", function_name, arg_count, None)
        return None

    # helper that genertes a new label for later jumpback
    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def new_placeholder(self):
        placeholder = f"P{self.label_counter}"
        self.label_counter += 1
        return placeholder

    def backpatch(self, target: int, replacement: int):
        self.quadruples[target].result = replacement

    def visitCondition(self, ctx: baby_duck_grammarParser.ConditionContext):
        # 1. Evaluate condition
        # 2. Generate gotof to jump to end of IF block
        # 3. generate quads of IF block
        # 4. backpatch the first gotof
        # 4. If theres an ELSE block, add the quads
        print(ctx.body().getText())

        condition_temporary = self.visit(ctx.expression())
        gotof = self.generate_quadruple("gotof", condition_temporary, None, None)
        self.visit(ctx.body())
        if_end_index = self.generate_quadruple("label", self.new_label(), None, None)
        self.backpatch(gotof, if_end_index)

    def visitBody(self, ctx: baby_duck_grammarParser.BodyContext):
        for child in ctx.getChildren():
            self.visit(child)
        return None

    def visitCycle(self, ctx: baby_duck_grammarParser.CycleContext):
        # start with a new label
        start_index = self.generate_quadruple("label", self.new_label(), None, None)

        # generate body quads
        self.visit(ctx.body())

        # visit condition quads, which also generates quads
        result_temp_variable = self.visit(ctx.expression())

        self.generate_quadruple("gotot", result_temp_variable, None, start_index)
        return None

    def print_all(self):
        for quad in self.quadruples:
            print(quad)
        print(self.operand_stack)

    def visitBody(self, ctx: baby_duck_grammarParser.BodyContext):
        for statement in ctx.statement():
            self.visit(statement)
        return None

    def visitExp(self, ctx: baby_duck_grammarParser.ExpContext):
        # Assume the first term is always present and visit it
        result = self.visit(ctx.term())

        if ctx.getChildCount() != 1:
            operator = ctx.operator().getText()
            right = self.visit(ctx.getChild(2))
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, result, right, temp_var)
            result = temp_var

        return result

    def visitTerm(self, ctx: baby_duck_grammarParser.TermContext):
        # This assumes the first factor is always present (based on the grammar)
        left = self.visit(ctx.factor())
        if ctx.getChildCount() != 1:
            operator = ctx.term_operator().getText()
            right = self.visit(ctx.term())
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, left, right, temp_var)
            return temp_var
        return left

    def visitPrint(self, ctx: baby_duck_grammarParser.PrintContext):
        if ctx.print_helper():
            self.visit(ctx.print_helper())
        else:
            self.generate_quadruple("print_newline", None, None, None)
        self.generate_quadruple("print_newline", None, None, None)
        return None

    def visitPrint_helper(self, ctx: baby_duck_grammarParser.Print_helperContext):
        for child in ctx.getChildren():
            if child.getText() != ",":
                self.generate_quadruple("print", self.visit(child), None, None)
        return None

    def visitString(self, ctx: baby_duck_grammarParser.StringContext):
        print("string: " + ctx.getText())
        return ctx.getText()

    def visitAssign(self, ctx: baby_duck_grammarParser.AssignContext):
        # get right hand side
        right = self.visit(ctx.expression())
        # get left hand side
        left = ctx.ID().getText()
        # generate quadruple
        self.generate_quadruple("=", right, None, "$" + left)
        return None

def process_string_token(token):
    if isinstance(token, str):
        if token[0] == '"':
            return token[1:-1]
        return "$" + token if token[0] != "$" else token
    return token

def preprocess_quads(quads):
    new_quads = []
    for quad in quads:
        left = parse_string(quad.left_operand)
        right = parse_string(quad.right_operand)

        left = process_string_token(left)
        right = process_string_token(right) 

        quad.left_operand = left
        quad.right_operand = right
        new_quads.append(quad)
    return new_quads


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = baby_duck_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duck_grammarParser(stream)
    memory_table = MemoryTable()
    parser.addParseListener(Listener(memory_table))
    tree = parser.program()
    memory_table.print()

    visitor = Visitor()
    visitor.visit(tree)

    new_quads = preprocess_quads(visitor.quadruples)
    for quad in new_quads:
        print(quad)
    vm = VirtualMachine(quads=new_quads, memory=memory_table)
    vm.run()


if __name__ == "__main__":
    main(sys.argv)
