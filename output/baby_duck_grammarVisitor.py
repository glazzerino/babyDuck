# Generated from baby_duck_grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .baby_duck_grammarParser import baby_duck_grammarParser
else:
    from baby_duck_grammarParser import baby_duck_grammarParser

# This class defines a complete generic visitor for a parse tree produced by baby_duck_grammarParser.

class baby_duck_grammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by baby_duck_grammarParser#program.
    def visitProgram(self, ctx:baby_duck_grammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#program_post_var.
    def visitProgram_post_var(self, ctx:baby_duck_grammarParser.Program_post_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#body.
    def visitBody(self, ctx:baby_duck_grammarParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#statement.
    def visitStatement(self, ctx:baby_duck_grammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#type.
    def visitType(self, ctx:baby_duck_grammarParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#assign.
    def visitAssign(self, ctx:baby_duck_grammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#expression.
    def visitExpression(self, ctx:baby_duck_grammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#rel_op.
    def visitRel_op(self, ctx:baby_duck_grammarParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#cte.
    def visitCte(self, ctx:baby_duck_grammarParser.CteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#print.
    def visitPrint(self, ctx:baby_duck_grammarParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#print_helper.
    def visitPrint_helper(self, ctx:baby_duck_grammarParser.Print_helperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#f_param_list.
    def visitF_param_list(self, ctx:baby_duck_grammarParser.F_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#f_param_list_helper.
    def visitF_param_list_helper(self, ctx:baby_duck_grammarParser.F_param_list_helperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#funcs.
    def visitFuncs(self, ctx:baby_duck_grammarParser.FuncsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#vars.
    def visitVars(self, ctx:baby_duck_grammarParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#vars_declarations.
    def visitVars_declarations(self, ctx:baby_duck_grammarParser.Vars_declarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#cycle.
    def visitCycle(self, ctx:baby_duck_grammarParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#condition.
    def visitCondition(self, ctx:baby_duck_grammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#condition_else.
    def visitCondition_else(self, ctx:baby_duck_grammarParser.Condition_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#operator.
    def visitOperator(self, ctx:baby_duck_grammarParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#exp.
    def visitExp(self, ctx:baby_duck_grammarParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#term.
    def visitTerm(self, ctx:baby_duck_grammarParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#term_operator.
    def visitTerm_operator(self, ctx:baby_duck_grammarParser.Term_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#factor.
    def visitFactor(self, ctx:baby_duck_grammarParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#factor_operator.
    def visitFactor_operator(self, ctx:baby_duck_grammarParser.Factor_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#parenthesized_expression.
    def visitParenthesized_expression(self, ctx:baby_duck_grammarParser.Parenthesized_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#f_call.
    def visitF_call(self, ctx:baby_duck_grammarParser.F_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by baby_duck_grammarParser#f_call_helper.
    def visitF_call_helper(self, ctx:baby_duck_grammarParser.F_call_helperContext):
        return self.visitChildren(ctx)



del baby_duck_grammarParser