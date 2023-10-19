import sys
from antlr4 import *
from output.baby_duck_grammarLexer import baby_duck_grammarLexer
from output.baby_duck_grammarParser import baby_duck_grammarParser

from output.baby_duck_grammarListener import baby_duck_grammarListener


class Listener(baby_duck_grammarListener):
    def exitVars(self, ctx: baby_duck_grammarParser.VarsContext):
        print("Var parsed: " + ctx.getText())
        return super().exitVars(ctx)
    
    def exitExpression(self, ctx: baby_duck_grammarParser.ExpressionContext):
        print("Expression parsed: " + ctx.getText())
        return super().exitExpression(ctx)


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = baby_duck_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duck_grammarParser(stream)
    parser.addParseListener(Listener())
    tree = parser.program()
    if tree.exception is None:
        print("No errors found")
    else:
        print("Syntax errors found")


if __name__ == "__main__":
    main(sys.argv)
