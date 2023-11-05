# Generated from baby_duck_grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .baby_duck_grammarParser import baby_duck_grammarParser
else:
    from baby_duck_grammarParser import baby_duck_grammarParser

# This class defines a complete listener for a parse tree produced by baby_duck_grammarParser.
class baby_duck_grammarListener(ParseTreeListener):

    # Enter a parse tree produced by baby_duck_grammarParser#program.
    def enterProgram(self, ctx:baby_duck_grammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#program.
    def exitProgram(self, ctx:baby_duck_grammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#program_post_var.
    def enterProgram_post_var(self, ctx:baby_duck_grammarParser.Program_post_varContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#program_post_var.
    def exitProgram_post_var(self, ctx:baby_duck_grammarParser.Program_post_varContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#body.
    def enterBody(self, ctx:baby_duck_grammarParser.BodyContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#body.
    def exitBody(self, ctx:baby_duck_grammarParser.BodyContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#statement.
    def enterStatement(self, ctx:baby_duck_grammarParser.StatementContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#statement.
    def exitStatement(self, ctx:baby_duck_grammarParser.StatementContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#type.
    def enterType(self, ctx:baby_duck_grammarParser.TypeContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#type.
    def exitType(self, ctx:baby_duck_grammarParser.TypeContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#assign.
    def enterAssign(self, ctx:baby_duck_grammarParser.AssignContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#assign.
    def exitAssign(self, ctx:baby_duck_grammarParser.AssignContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#expression.
    def enterExpression(self, ctx:baby_duck_grammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#expression.
    def exitExpression(self, ctx:baby_duck_grammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#rel_op.
    def enterRel_op(self, ctx:baby_duck_grammarParser.Rel_opContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#rel_op.
    def exitRel_op(self, ctx:baby_duck_grammarParser.Rel_opContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#cte.
    def enterCte(self, ctx:baby_duck_grammarParser.CteContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#cte.
    def exitCte(self, ctx:baby_duck_grammarParser.CteContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#print.
    def enterPrint(self, ctx:baby_duck_grammarParser.PrintContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#print.
    def exitPrint(self, ctx:baby_duck_grammarParser.PrintContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#print_helper.
    def enterPrint_helper(self, ctx:baby_duck_grammarParser.Print_helperContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#print_helper.
    def exitPrint_helper(self, ctx:baby_duck_grammarParser.Print_helperContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#f_param_list.
    def enterF_param_list(self, ctx:baby_duck_grammarParser.F_param_listContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#f_param_list.
    def exitF_param_list(self, ctx:baby_duck_grammarParser.F_param_listContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#f_param_list_helper.
    def enterF_param_list_helper(self, ctx:baby_duck_grammarParser.F_param_list_helperContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#f_param_list_helper.
    def exitF_param_list_helper(self, ctx:baby_duck_grammarParser.F_param_list_helperContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#funcs.
    def enterFuncs(self, ctx:baby_duck_grammarParser.FuncsContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#funcs.
    def exitFuncs(self, ctx:baby_duck_grammarParser.FuncsContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#vars.
    def enterVars(self, ctx:baby_duck_grammarParser.VarsContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#vars.
    def exitVars(self, ctx:baby_duck_grammarParser.VarsContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#vars_declarations.
    def enterVars_declarations(self, ctx:baby_duck_grammarParser.Vars_declarationsContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#vars_declarations.
    def exitVars_declarations(self, ctx:baby_duck_grammarParser.Vars_declarationsContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#cycle.
    def enterCycle(self, ctx:baby_duck_grammarParser.CycleContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#cycle.
    def exitCycle(self, ctx:baby_duck_grammarParser.CycleContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#while_keyword.
    def enterWhile_keyword(self, ctx:baby_duck_grammarParser.While_keywordContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#while_keyword.
    def exitWhile_keyword(self, ctx:baby_duck_grammarParser.While_keywordContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#condition.
    def enterCondition(self, ctx:baby_duck_grammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#condition.
    def exitCondition(self, ctx:baby_duck_grammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#condition_else.
    def enterCondition_else(self, ctx:baby_duck_grammarParser.Condition_elseContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#condition_else.
    def exitCondition_else(self, ctx:baby_duck_grammarParser.Condition_elseContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#operator.
    def enterOperator(self, ctx:baby_duck_grammarParser.OperatorContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#operator.
    def exitOperator(self, ctx:baby_duck_grammarParser.OperatorContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#exp.
    def enterExp(self, ctx:baby_duck_grammarParser.ExpContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#exp.
    def exitExp(self, ctx:baby_duck_grammarParser.ExpContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#term.
    def enterTerm(self, ctx:baby_duck_grammarParser.TermContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#term.
    def exitTerm(self, ctx:baby_duck_grammarParser.TermContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#term_operator.
    def enterTerm_operator(self, ctx:baby_duck_grammarParser.Term_operatorContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#term_operator.
    def exitTerm_operator(self, ctx:baby_duck_grammarParser.Term_operatorContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#factor.
    def enterFactor(self, ctx:baby_duck_grammarParser.FactorContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#factor.
    def exitFactor(self, ctx:baby_duck_grammarParser.FactorContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#factor_operator.
    def enterFactor_operator(self, ctx:baby_duck_grammarParser.Factor_operatorContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#factor_operator.
    def exitFactor_operator(self, ctx:baby_duck_grammarParser.Factor_operatorContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:baby_duck_grammarParser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:baby_duck_grammarParser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#f_call.
    def enterF_call(self, ctx:baby_duck_grammarParser.F_callContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#f_call.
    def exitF_call(self, ctx:baby_duck_grammarParser.F_callContext):
        pass


    # Enter a parse tree produced by baby_duck_grammarParser#f_call_helper.
    def enterF_call_helper(self, ctx:baby_duck_grammarParser.F_call_helperContext):
        pass

    # Exit a parse tree produced by baby_duck_grammarParser#f_call_helper.
    def exitF_call_helper(self, ctx:baby_duck_grammarParser.F_call_helperContext):
        pass



del baby_duck_grammarParser