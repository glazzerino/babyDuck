from dataclasses import dataclass
import sys
from antlr4 import *
from output.baby_duck_grammarLexer import baby_duck_grammarLexer
from output.baby_duck_grammarParser import baby_duck_grammarParser

from output.baby_duck_grammarListener import baby_duck_grammarListener


class VariableTable:
    def __init__(self):
        self.table = {}

    def insert(self, var_id, var_type, value=None):
        if var_id in self.table:
            raise Exception("Variable already declared")
        self.table[var_id] = {"type": var_type, "value": value}

    def get(self, var_id) -> dict:
        return self.table.get(var_id, None)

    def print(self):
        if not self.table:
            print("Empty Symbol Table")
            return

        header = "| {:<15} | {:<10} | {:<10} |".format("Variable", "Type", "Value")
        print("-" * len(header))
        print(header)
        print("-" * len(header))

        for var_id, details in self.table.items():
            row = "| {:<15} | {:<10} | {:<10} |".format(
                var_id,
                details["type"],
                str(details["value"]) if details["value"] is not None else "N/A",
            )
            print(row)
        print("-" * len(header))



@dataclass(frozen=True)
class FunctionID:
    name: str
    type: str

    def __hash__(self):
        return hash((self.name, self.type))

    def __eq__(self, other):
        if not isinstance(other, FunctionID):
            return False
        return self.name == other.name and self.type == other.type


class FunctionTable:
    def __init__(self):
        self.table = {}
        self.active_function = None

    def get(self, func_id: FunctionID) -> VariableTable:
        return self.table.get(func_id, None)

    def insert_to_top(self, var_id, var_type, value=None):
        self.table[self.active_function].insert(var_id, var_type, value)
    
    def insert_new_function(self, func_id: FunctionID):
        if func_id in self.table:
            raise Exception("Function already declared")
        self.table[func_id] = VariableTable()
        self.active_function = func_id
    
    def get_active_function_table(self) -> VariableTable:
        return self.table[self.active_function]
    
    def print_all(self):
        for func_id, var_table in self.table.items():
            print("Function: ", func_id.name, func_id.type)
            var_table.print()
            print("\n")
    
class Listener(baby_duck_grammarListener):
    def __init__(self, function_table: FunctionTable):
        self.function_table = function_table
        self.var_stack = []
    def enterProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        return super().enterProgram(ctx)

    def exitProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        return super().exitProgram(ctx)

    def enterProgram_post_var(self, ctx: baby_duck_grammarParser.Program_post_varContext):
        for id, type in self.var_stack:
            self.function_table.insert_to_top(id, type)
        return super().enterProgram_post_var(ctx)
    def enterFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        self.var_stack = []
        return super().enterFuncs(ctx)

    def exitFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        function_id = FunctionID(ctx.ID().getText(), ctx.type_().getText())
        self.function_table.insert_new_function(function_id)
        for var_id, var_type in self.var_stack:
            self.function_table.insert_to_top(var_id, var_type)
        return super().exitFuncs(ctx)

    def exitVars_declarations(
        self, ctx: baby_duck_grammarParser.Vars_declarationsContext
    ):     
        var_type = ctx.type_().getText()
    
        for id in ctx.ID():
            id_text = id.getText()
            self.var_stack.append((id_text, var_type)) 
        return super().exitVars_declarations(ctx)

    def exitExpression(self, ctx: baby_duck_grammarParser.ExpressionContext):
        return super().exitExpression(ctx)


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = baby_duck_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duck_grammarParser(stream)
    function_table = FunctionTable()
    function_table.insert_new_function(FunctionID("global", "void"))    
    parser.addParseListener(Listener(function_table))
    tree = parser.program()
    print("parsing complete")
    function_table.print_all()



if __name__ == "__main__":
    main(sys.argv)
