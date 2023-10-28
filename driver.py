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


@dataclass
class FunctionID:
    name: str
    type: str


class FunctionTable:
    def __init__(self):
        self.table = {}

    def get(self, func_id: FunctionID) -> VariableTable:
        return self.table.get(func_id, None)

    def insert(self, var_id, var_type, value=None):
        self.top().insert(var_id, var_type, value)
    


class Listener(baby_duck_grammarListener):
    def __init__(self):
        self.function_table = FunctionTable()

    def enterProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        self.symbol_table_stack.push(VariableTable())
        return super().enterProgram(ctx)

    def exitProgram(self, ctx: baby_duck_grammarParser.ProgramContext):
        self.symbol_table_stack.top().print()
        self.symbol_table_stack.pop()
        return super().exitProgram(ctx)

    def enterFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        self.symbol_table_stack.push(VariableTable())
        return super().enterFuncs(ctx)

    def exitFuncs(self, ctx: baby_duck_grammarParser.FuncsContext):
        self.symbol_table_stack.top().print()
        self.symbol_table_stack.pop()
        return super().exitFuncs(ctx)

    def exitVars_declarations(
        self, ctx: baby_duck_grammarParser.Vars_declarationsContext
    ):
        var_type = ctx.type_().getText()

        for id in ctx.ID():
            print("Variable name: " + id.getText())
            id_text = id.getText()
            self.symbol_table_stack.insert(id_text, var_type)

        return super().exitVars_declarations(ctx)

    def exitExpression(self, ctx: baby_duck_grammarParser.ExpressionContext):
        return super().exitExpression(ctx)


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = baby_duck_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duck_grammarParser(stream)
    parser.addParseListener(Listener())
    tree = parser.program()
    print("parsing complete")


if __name__ == "__main__":
    main(sys.argv)
