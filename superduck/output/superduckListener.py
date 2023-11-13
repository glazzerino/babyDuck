# Generated from superduck.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .superduckParser import superduckParser
else:
    from superduckParser import superduckParser

# This class defines a complete listener for a parse tree produced by superduckParser.
class superduckListener(ParseTreeListener):

    # Enter a parse tree produced by superduckParser#program.
    def enterProgram(self, ctx:superduckParser.ProgramContext):
        pass

    # Exit a parse tree produced by superduckParser#program.
    def exitProgram(self, ctx:superduckParser.ProgramContext):
        pass


    # Enter a parse tree produced by superduckParser#expression.
    def enterExpression(self, ctx:superduckParser.ExpressionContext):
        pass

    # Exit a parse tree produced by superduckParser#expression.
    def exitExpression(self, ctx:superduckParser.ExpressionContext):
        pass


    # Enter a parse tree produced by superduckParser#equality.
    def enterEquality(self, ctx:superduckParser.EqualityContext):
        pass

    # Exit a parse tree produced by superduckParser#equality.
    def exitEquality(self, ctx:superduckParser.EqualityContext):
        pass


    # Enter a parse tree produced by superduckParser#comparison.
    def enterComparison(self, ctx:superduckParser.ComparisonContext):
        pass

    # Exit a parse tree produced by superduckParser#comparison.
    def exitComparison(self, ctx:superduckParser.ComparisonContext):
        pass


    # Enter a parse tree produced by superduckParser#term.
    def enterTerm(self, ctx:superduckParser.TermContext):
        pass

    # Exit a parse tree produced by superduckParser#term.
    def exitTerm(self, ctx:superduckParser.TermContext):
        pass


    # Enter a parse tree produced by superduckParser#factor.
    def enterFactor(self, ctx:superduckParser.FactorContext):
        pass

    # Exit a parse tree produced by superduckParser#factor.
    def exitFactor(self, ctx:superduckParser.FactorContext):
        pass


    # Enter a parse tree produced by superduckParser#unary.
    def enterUnary(self, ctx:superduckParser.UnaryContext):
        pass

    # Exit a parse tree produced by superduckParser#unary.
    def exitUnary(self, ctx:superduckParser.UnaryContext):
        pass


    # Enter a parse tree produced by superduckParser#primary.
    def enterPrimary(self, ctx:superduckParser.PrimaryContext):
        pass

    # Exit a parse tree produced by superduckParser#primary.
    def exitPrimary(self, ctx:superduckParser.PrimaryContext):
        pass



del superduckParser