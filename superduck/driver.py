from antlr4 import *

from output.superduckVisitor import superduckVisitor
from output.superduckParser import superduckParser
from dataclasses import dataclass
from output.superduckLexer import superduckLexer


@dataclass
class Quadruple:
    operator: str
    left_operand: str
    right_operand: str
    result: str


quads = []


def create_quadruple(operator, left_operand, right_operand, result):
    quads.append(Quadruple(operator, left_operand, right_operand, result))


class customVisitor(superduckVisitor):
    def __init__(self):
        self.temp_count = 0
    # Visit a parse tree produced by superduckParser#primary.
    def visitPrimary(self, ctx: superduckParser.PrimaryContext):
        return self.visit(ctx.getChild(0))
    def visit
    def new_temporary(self):
        return "t" + str(self.temp_count)
    
    def visitUnary(self, ctx: superduckParser.UnaryContext):
        if ctx.getChild(0) in ['+', '-']:
            temp =  self.new_temporary()
            operand = ctx.visit(ctx.getChild(1))
            create_quadruple(ctx.getChild(0), operand, None, temp)
            return temp
        else:
            return self.visit(ctx.primary())

# run parser with input file
def run():
    stream = FileStream("input.txt")
    lexer = superduckLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = superduckParser(stream)
    tree = parser.program()
    visitor = customVisitor()
    visitor.visit(tree)
    print(quads)


run()
