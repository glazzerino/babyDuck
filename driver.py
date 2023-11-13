import sys
from antlr4 import *
from output.baby_duck_grammarLexer import baby_duck_grammarLexer
from output.baby_duck_grammarParser import baby_duck_grammarParser
from Quadruple import Quadruple
from output.baby_duck_grammarListener import baby_duck_grammarListener
from tables import FunctionID, FunctionTable, VariableTable
from output.baby_duck_grammarVisitor import baby_duck_grammarVisitor


class Listener(baby_duck_grammarListener):
    def __init__(self, function_table: FunctionTable):
        self.function_table = function_table
        self.variable_buffer = []

    def enterProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        return super().enterProgram(ctx)

    def exitProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        return super().exitProgram(ctx)

    def enterProgram_post_var(
        self, ctx: baby_duck_grammarParser.Program_post_varContext
    ):
        for id, type in self.variable_buffer:
            self.function_table.insert_to_top(id, type)
        return super().enterProgram_post_var(ctx)

    def enterFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        self.variable_buffer = []
        return super().enterFuncs(ctx)

    def binary_op_quadruple(self, ctx):
        if ctx.getChildCount() == 3:
            left_operand = ctx.getChild(0)
            operator = ctx.getChild(1)
            right_operand = ctx.getChild(2)
            print(left_operand.getText(), operator.getText(), right_operand.getText())

            result_temp = self.new_temporary()

            quad = Quadruple(
                left_operand=left_operand.getText(),
                operator=operator.getText(),
                right_operand=right_operand.getText(),
                result=result_temp,
            )
            self.quadruples.append(quad)
            print("Generated Quadruple: ", quad)

    def exitFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        function_id = FunctionID(ctx.ID().getText(), ctx.type_().getText())
        self.function_table.insert_new_function(function_id)
        for var_id, var_type in self.variable_buffer:
            self.function_table.insert_to_top(var_id, var_type)
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

    def new_temporary(self):
        name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return name


def determine_type(ctx):
    if ctx.ID():
        return "VAR"
    if ctx.cte():
        return "CTE"


class Visitor(baby_duck_grammarVisitor):
    def __init__(self):
        self.temp_counter = 0
        self.quadruples = []
        self.operand_stack = []
        self.operator_stack = []
        self.type_stack = []
        self.jump_stack = []
        self.quadruples = []
        self.temp_counter = 0
        self.label_counter = 0
        self.quadruples = []

    def visitFactor(self, ctx: baby_duck_grammarParser.FactorContext):
        if ctx.parenthesized_expression():
            # A parenthesized expression should be evaluated on its own terms.
            return self.visit(ctx.parenthesized_expression())
        else:
            unary_op = None

            if ctx.factor_operator():  # If there is a unary operator present
                unary_op = ctx.factor_operator().getText()
                operand = ctx.getChild(
                    1
                ).getText()  # The operand follows the unary operator
            else:
                operand = ctx.getChild(0).getText()  # Just a simple ID or cte

            if unary_op:
                temp_var = self.new_temporary()
                self.generate_quadruple(unary_op, operand, None, temp_var)
                self.operand_stack.append(temp_var)
            else:
                # Push the operand onto the operand stack
                self.operand_stack.append(operand)

        return self.operand_stack[-1] if self.operand_stack else None

    def generate_quadruple(self, operator, left_operand, right_operand, result) -> int:
        quad = Quadruple(
            operator=operator,
            left_operand=left_operand,
            right_operand=right_operand,
            result=result,
        )
        self.quadruples.append(quad)
        return len(self.quadruples) - 1

    def new_temporary(self):
        name = f"t{self.temp_counter}"
        self.temp_counter += 1
        return name

    def visitParenthesized_expression(
        self, ctx: baby_duck_grammarParser.Parenthesized_expressionContext
    ):
        return self.visit(ctx.expression())

    def visitExpression(self, ctx: baby_duck_grammarParser.ExpressionContext):
        left = self.visit(ctx.exp())
        if (ctx.getChildCount() != 1):
            operator = ctx.rel_op().getText()
            right = self.visit(ctx.getChild(2))
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, left, right, temp_var)
            return temp_var
        
        return left
        # elif ctx.getChildCount() == 3:
        #     lhs_result = self.visit(ctx.exp(0))
        #     rhs_result = self.visit(ctx.exp(1))

        #     rel_op = ctx.rel_op().getText()

        #     temp_var = self.new_temporary()

        #     self.generate_quadruple(rel_op, lhs_result, rhs_result, temp_var)

        #     self.operand_stack.append(temp_var)

        #     return temp_var
        # else:
        #     raise Exception("Unsupported expression structure")

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
    
    def visitCondition(self, ctx: baby_duck_grammarParser.ConditionContext):
        condition = self.visit(ctx.expression())

        false_placeholder = self.new_placeholder()

        self.jump_stack.append(("if_false", false_placeholder))
        false_jump_index = self.generate_quadruple("if_false", condition, None, false_placeholder)
        
        self.visit(ctx.body())

        end_if_placeholder = None

        if ctx.condition_else():
            end_if_placeholder = self.new_placeholder()
            self.jump_stack.append(("goto_end_if", end_if_placeholder))
            end_if_index = self.generate_quadruple("goto", None, None, end_if_placeholder)
        
        false_jump_label = self.new_label()
        self.backpatch(false_jump_index, false_jump_label)
        self.jump_stack.pop()

        if ctx.condition_else():
            self.visit(ctx.condition_else())
            end_if_label = self.new_label()
            self.backpatch(end_if_index, end_if_label)
            self.jump_stack.pop()
        
        if not ctx.condition_else():
            self.generate_quadruple("label", false_jump_label, None, None) 
        if end_if_placeholder:
            self.generate_quadruple("label", end_if_label, None, None)
        return None

    def backpatch(self, placeolder: str, label: str):
        for i, quad in enumerate(self.quadruples):
            if quad.result == placeolder:
                self.quadruples[i].result = label


    def visitCycle(self, ctx: baby_duck_grammarParser.CycleContext):
        start_label = self.new_label()
        self.jump_stack.append(("start", start_label))
        self.generate_quadruple("label", start_label, None, None)

        condition_result = self.visit(ctx.expression())
        exit_label_placeholder = self.new_placeholder()
        self.jump_stack.append(("end", exit_label_placeholder))
        exit_index = self.generate_quadruple(
            "if_false", condition_result, None, exit_label_placeholder
        )

        self.visit(ctx.body())

        self.generate_quadruple("goto", start_label, None, None)

        end_label = self.new_label()
        self.generate_quadruple("label", end_label, None, None)

        self.backpatch(exit_index, end_label)

        while self.jump_stack and self.jump_stack[-1][0] == "end":
            label_type, placeholder = self.jump_stack.pop()
            self.backpatch(placeholder, end_label)

        return None


    def print_all(self):
        for quad in self.quadruples:
            print(quad)
        print(self.operand_stack)

    def visitExp(self, ctx: baby_duck_grammarParser.ExpContext):
        # Assume the first term is always present and visit it
        result = self.visit(ctx.term())
        
        if (ctx.getChildCount() != 1):
            operator = ctx.operator().getText()
            right = self.visit(ctx.getChild(2))
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, result, right, temp_var)
            result = temp_var
        
        return result

        # Now, process all subsequent terms with their preceding operators
        # for i in range(1, len(ctx.term())):
        #     operator = ctx.operator(i - 1).getText()  # The operator between terms
        #     right = self.visit(ctx.term(i))  # The right operand (term)

        #     # Generate a quadruple if there is a valid right operand
        #     if right is not None:
        #         result_temp = self.new_temporary()

        #         # Generate a quadruple for the operation
        #         self.generate_quadruple(operator, result, right, result_temp)

        #         # The result of this operation becomes the "result" for the next operation
        #         result = result_temp

        return result

    def visitTerm(self, ctx: baby_duck_grammarParser.TermContext):
        # This assumes the first factor is always present (based on the grammar)
        left = self.visit(ctx.factor())
        if (ctx.getChildCount() != 1):
            operator = ctx.term_operator().getText()
            right = self.visit(ctx.term())
            temp_var = self.new_temporary()
            self.generate_quadruple(operator, left, right, temp_var)
            return temp_var
        return left
        # Now, process all subsequent factors
        # for i in range(1, len(ctx.factor())):
        #     operator = ctx.getChild(2 * i - 1).getText()
        #     right = self.visit(ctx.factor(i))

        #     if right is not None:
        #         result_temp = self.new_temporary()

        #         # Generate a quadruple for the operation
        #         self.generate_quadruple(operator, result, right, result_temp)

        #         # The result of this operation will be used as the left operand
        #         # for the next operation (if any)
        #         result = result_temp

        return result

    def visitPrint(self, ctx: baby_duck_grammarParser.PrintContext):
        if ctx.print_helper():
            print_items = ctx.print_helper()
            for item in print_items.expression():
                item_result = self.visit(item)

                self.generate_quadruple("print", item_result, None, None)
            self.generate_quadruple("print_newline", None, None, None)
        else:
            self.generate_quadruple("print_newline", None, None, None)

        return None

    def visitAssign(self, ctx: baby_duck_grammarParser.AssignContext):
        # get right hand side
        right = self.visit(ctx.expression())
        # get left hand side
        left = ctx.ID().getText()
        # generate quadruple
        self.generate_quadruple("=", right, None, left)
        return None


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = baby_duck_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duck_grammarParser(stream)
    function_table = FunctionTable()
    function_table.insert_new_function(FunctionID("global", "void"))
    parser.addParseListener(Listener(function_table))
    tree = parser.program()
    # function_table.print_all()
    print("parsing complete")
    print("Visitor start")
    visitor = Visitor()
    visitor.visit(tree)
    visitor.print_all()


if __name__ == "__main__":
    main(sys.argv)
