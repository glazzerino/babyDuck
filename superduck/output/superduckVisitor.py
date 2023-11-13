# Generated from superduck.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .superduckParser import superduckParser
else:
    from superduckParser import superduckParser

# This class defines a complete generic visitor for a parse tree produced by superduckParser.

class superduckVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by superduckParser#program.
    def visitProgram(self, ctx:superduckParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#expression.
    def visitExpression(self, ctx:superduckParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#equality.
    def visitEquality(self, ctx:superduckParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#comparison.
    def visitComparison(self, ctx:superduckParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#term.
    def visitTerm(self, ctx:superduckParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#factor.
    def visitFactor(self, ctx:superduckParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#unary.
    def visitUnary(self, ctx:superduckParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by superduckParser#primary.
    def visitPrimary(self, ctx:superduckParser.PrimaryContext):
        return self.visitChildren(ctx)



del superduckParser