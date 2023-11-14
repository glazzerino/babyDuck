// Generated from c:/Users/fztmo/code/babyDuck/baby_duck_grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link baby_duck_grammarParser}.
 */
public interface baby_duck_grammarListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#string}.
	 * @param ctx the parse tree
	 */
	void enterString(baby_duck_grammarParser.StringContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#string}.
	 * @param ctx the parse tree
	 */
	void exitString(baby_duck_grammarParser.StringContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(baby_duck_grammarParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(baby_duck_grammarParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#program_post_var}.
	 * @param ctx the parse tree
	 */
	void enterProgram_post_var(baby_duck_grammarParser.Program_post_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#program_post_var}.
	 * @param ctx the parse tree
	 */
	void exitProgram_post_var(baby_duck_grammarParser.Program_post_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(baby_duck_grammarParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(baby_duck_grammarParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(baby_duck_grammarParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(baby_duck_grammarParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(baby_duck_grammarParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(baby_duck_grammarParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(baby_duck_grammarParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(baby_duck_grammarParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(baby_duck_grammarParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(baby_duck_grammarParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#rel_op}.
	 * @param ctx the parse tree
	 */
	void enterRel_op(baby_duck_grammarParser.Rel_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#rel_op}.
	 * @param ctx the parse tree
	 */
	void exitRel_op(baby_duck_grammarParser.Rel_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(baby_duck_grammarParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(baby_duck_grammarParser.CteContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#print}.
	 * @param ctx the parse tree
	 */
	void enterPrint(baby_duck_grammarParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#print}.
	 * @param ctx the parse tree
	 */
	void exitPrint(baby_duck_grammarParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#print_helper}.
	 * @param ctx the parse tree
	 */
	void enterPrint_helper(baby_duck_grammarParser.Print_helperContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#print_helper}.
	 * @param ctx the parse tree
	 */
	void exitPrint_helper(baby_duck_grammarParser.Print_helperContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#f_param_list}.
	 * @param ctx the parse tree
	 */
	void enterF_param_list(baby_duck_grammarParser.F_param_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#f_param_list}.
	 * @param ctx the parse tree
	 */
	void exitF_param_list(baby_duck_grammarParser.F_param_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#f_param_list_helper}.
	 * @param ctx the parse tree
	 */
	void enterF_param_list_helper(baby_duck_grammarParser.F_param_list_helperContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#f_param_list_helper}.
	 * @param ctx the parse tree
	 */
	void exitF_param_list_helper(baby_duck_grammarParser.F_param_list_helperContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#funcs}.
	 * @param ctx the parse tree
	 */
	void enterFuncs(baby_duck_grammarParser.FuncsContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#funcs}.
	 * @param ctx the parse tree
	 */
	void exitFuncs(baby_duck_grammarParser.FuncsContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#function_id}.
	 * @param ctx the parse tree
	 */
	void enterFunction_id(baby_duck_grammarParser.Function_idContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#function_id}.
	 * @param ctx the parse tree
	 */
	void exitFunction_id(baby_duck_grammarParser.Function_idContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#vars}.
	 * @param ctx the parse tree
	 */
	void enterVars(baby_duck_grammarParser.VarsContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#vars}.
	 * @param ctx the parse tree
	 */
	void exitVars(baby_duck_grammarParser.VarsContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#vars_declarations}.
	 * @param ctx the parse tree
	 */
	void enterVars_declarations(baby_duck_grammarParser.Vars_declarationsContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#vars_declarations}.
	 * @param ctx the parse tree
	 */
	void exitVars_declarations(baby_duck_grammarParser.Vars_declarationsContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#cycle}.
	 * @param ctx the parse tree
	 */
	void enterCycle(baby_duck_grammarParser.CycleContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#cycle}.
	 * @param ctx the parse tree
	 */
	void exitCycle(baby_duck_grammarParser.CycleContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#while_keyword}.
	 * @param ctx the parse tree
	 */
	void enterWhile_keyword(baby_duck_grammarParser.While_keywordContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#while_keyword}.
	 * @param ctx the parse tree
	 */
	void exitWhile_keyword(baby_duck_grammarParser.While_keywordContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(baby_duck_grammarParser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(baby_duck_grammarParser.ConditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#condition_else}.
	 * @param ctx the parse tree
	 */
	void enterCondition_else(baby_duck_grammarParser.Condition_elseContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#condition_else}.
	 * @param ctx the parse tree
	 */
	void exitCondition_else(baby_duck_grammarParser.Condition_elseContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(baby_duck_grammarParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(baby_duck_grammarParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(baby_duck_grammarParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(baby_duck_grammarParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(baby_duck_grammarParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(baby_duck_grammarParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#term_operator}.
	 * @param ctx the parse tree
	 */
	void enterTerm_operator(baby_duck_grammarParser.Term_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#term_operator}.
	 * @param ctx the parse tree
	 */
	void exitTerm_operator(baby_duck_grammarParser.Term_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(baby_duck_grammarParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(baby_duck_grammarParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#factor_operator}.
	 * @param ctx the parse tree
	 */
	void enterFactor_operator(baby_duck_grammarParser.Factor_operatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#factor_operator}.
	 * @param ctx the parse tree
	 */
	void exitFactor_operator(baby_duck_grammarParser.Factor_operatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#parenthesized_expression}.
	 * @param ctx the parse tree
	 */
	void enterParenthesized_expression(baby_duck_grammarParser.Parenthesized_expressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#parenthesized_expression}.
	 * @param ctx the parse tree
	 */
	void exitParenthesized_expression(baby_duck_grammarParser.Parenthesized_expressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#f_call}.
	 * @param ctx the parse tree
	 */
	void enterF_call(baby_duck_grammarParser.F_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#f_call}.
	 * @param ctx the parse tree
	 */
	void exitF_call(baby_duck_grammarParser.F_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link baby_duck_grammarParser#f_call_helper}.
	 * @param ctx the parse tree
	 */
	void enterF_call_helper(baby_duck_grammarParser.F_call_helperContext ctx);
	/**
	 * Exit a parse tree produced by {@link baby_duck_grammarParser#f_call_helper}.
	 * @param ctx the parse tree
	 */
	void exitF_call_helper(baby_duck_grammarParser.F_call_helperContext ctx);
}