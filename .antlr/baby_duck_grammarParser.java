// Generated from c:/Users/fztmo/code/babyDuck/baby_duck_grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class baby_duck_grammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, ID=35, INT=36, WS=37, FLOAT=38;
	public static final int
		RULE_string = 0, RULE_program = 1, RULE_program_post_var = 2, RULE_body = 3, 
		RULE_statement = 4, RULE_type = 5, RULE_assign = 6, RULE_expression = 7, 
		RULE_rel_op = 8, RULE_cte = 9, RULE_print = 10, RULE_print_helper = 11, 
		RULE_f_param_list = 12, RULE_f_param_list_helper = 13, RULE_funcs = 14, 
		RULE_function_id = 15, RULE_vars = 16, RULE_vars_declarations = 17, RULE_cycle = 18, 
		RULE_while_keyword = 19, RULE_condition = 20, RULE_condition_else = 21, 
		RULE_operator = 22, RULE_exp = 23, RULE_term = 24, RULE_term_operator = 25, 
		RULE_factor = 26, RULE_factor_operator = 27, RULE_parenthesized_expression = 28, 
		RULE_f_call = 29, RULE_f_call_helper = 30;
	private static String[] makeRuleNames() {
		return new String[] {
			"string", "program", "program_post_var", "body", "statement", "type", 
			"assign", "expression", "rel_op", "cte", "print", "print_helper", "f_param_list", 
			"f_param_list_helper", "funcs", "function_id", "vars", "vars_declarations", 
			"cycle", "while_keyword", "condition", "condition_else", "operator", 
			"exp", "term", "term_operator", "factor", "factor_operator", "parenthesized_expression", 
			"f_call", "f_call_helper"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\"'", "'program'", "';'", "'main'", "'end'", "'{'", "'}'", "'int'", 
			"'float'", "'bool'", "'void'", "'='", "'<'", "'>'", "'!='", "'=='", "'<='", 
			"'>=c'", "'print'", "'('", "')'", "','", "':'", "'['", "']'", "'var'", 
			"'do'", "'while'", "'if'", "'else'", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "ID", 
			"INT", "WS", "FLOAT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "baby_duck_grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public baby_duck_grammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringContext extends ParserRuleContext {
		public StringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_string; }
	}

	public final StringContext string() throws RecognitionException {
		StringContext _localctx = new StringContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_string);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__0);
			setState(66);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(63);
					matchWildcard();
					}
					} 
				}
				setState(68);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(69);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public Program_post_varContext program_post_var() {
			return getRuleContext(Program_post_varContext.class,0);
		}
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(T__1);
			setState(72);
			match(ID);
			setState(73);
			match(T__2);
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25) {
				{
				setState(74);
				vars();
				}
			}

			setState(77);
			program_post_var();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Program_post_varContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public List<FuncsContext> funcs() {
			return getRuleContexts(FuncsContext.class);
		}
		public FuncsContext funcs(int i) {
			return getRuleContext(FuncsContext.class,i);
		}
		public Program_post_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program_post_var; }
	}

	public final Program_post_varContext program_post_var() throws RecognitionException {
		Program_post_varContext _localctx = new Program_post_varContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_program_post_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) {
				{
				{
				setState(79);
				funcs();
				}
				}
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(85);
			match(T__3);
			setState(86);
			body();
			setState(87);
			match(T__4);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BodyContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(T__5);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 35031351296L) != 0)) {
				{
				{
				setState(90);
				statement();
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(96);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public CycleContext cycle() {
			return getRuleContext(CycleContext.class,0);
		}
		public F_callContext f_call() {
			return getRuleContext(F_callContext.class,0);
		}
		public PrintContext print() {
			return getRuleContext(PrintContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_statement);
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(98);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(100);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(101);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(102);
				print();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(ID);
			setState(108);
			match(T__11);
			setState(109);
			expression();
			setState(110);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			exp();
			setState(116);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 516096L) != 0)) {
				{
				setState(113);
				rel_op();
				setState(114);
				expression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Rel_opContext extends ParserRuleContext {
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 516096L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(baby_duck_grammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(baby_duck_grammarParser.FLOAT, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			_la = _input.LA(1);
			if ( !(_la==INT || _la==FLOAT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintContext extends ParserRuleContext {
		public Print_helperContext print_helper() {
			return getRuleContext(Print_helperContext.class,0);
		}
		public PrintContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print; }
	}

	public final PrintContext print() throws RecognitionException {
		PrintContext _localctx = new PrintContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			match(T__18);
			setState(123);
			match(T__19);
			setState(124);
			print_helper();
			setState(125);
			match(T__20);
			setState(126);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Print_helperContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<StringContext> string() {
			return getRuleContexts(StringContext.class);
		}
		public StringContext string(int i) {
			return getRuleContext(StringContext.class,i);
		}
		public Print_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_helper; }
	}

	public final Print_helperContext print_helper() throws RecognitionException {
		Print_helperContext _localctx = new Print_helperContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_print_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
			case T__30:
			case T__31:
			case ID:
			case INT:
			case FLOAT:
				{
				setState(128);
				expression();
				}
				break;
			case T__0:
				{
				setState(129);
				string();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__21) {
				{
				{
				setState(132);
				match(T__21);
				setState(135);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__19:
				case T__30:
				case T__31:
				case ID:
				case INT:
				case FLOAT:
					{
					setState(133);
					expression();
					}
					break;
				case T__0:
					{
					setState(134);
					string();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_param_listContext extends ParserRuleContext {
		public List<F_param_list_helperContext> f_param_list_helper() {
			return getRuleContexts(F_param_list_helperContext.class);
		}
		public F_param_list_helperContext f_param_list_helper(int i) {
			return getRuleContext(F_param_list_helperContext.class,i);
		}
		public F_param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_param_list; }
	}

	public final F_param_listContext f_param_list() throws RecognitionException {
		F_param_listContext _localctx = new F_param_listContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_f_param_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(142);
				f_param_list_helper();
				setState(147);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__21) {
					{
					{
					setState(143);
					match(T__21);
					setState(144);
					f_param_list_helper();
					}
					}
					setState(149);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_param_list_helperContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public F_param_list_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_param_list_helper; }
	}

	public final F_param_list_helperContext f_param_list_helper() throws RecognitionException {
		F_param_list_helperContext _localctx = new F_param_list_helperContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_f_param_list_helper);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(152);
			match(ID);
			setState(153);
			match(T__22);
			setState(154);
			type();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncsContext extends ParserRuleContext {
		public Function_idContext function_id() {
			return getRuleContext(Function_idContext.class,0);
		}
		public F_param_listContext f_param_list() {
			return getRuleContext(F_param_listContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public VarsContext vars() {
			return getRuleContext(VarsContext.class,0);
		}
		public FuncsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs; }
	}

	public final FuncsContext funcs() throws RecognitionException {
		FuncsContext _localctx = new FuncsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			function_id();
			setState(157);
			match(T__19);
			setState(158);
			f_param_list();
			setState(159);
			match(T__20);
			setState(160);
			match(T__23);
			setState(162);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25) {
				{
				setState(161);
				vars();
				}
			}

			setState(164);
			body();
			setState(165);
			match(T__24);
			setState(166);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_idContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public Function_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_id; }
	}

	public final Function_idContext function_id() throws RecognitionException {
		Function_idContext _localctx = new Function_idContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_function_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			type();
			setState(169);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarsContext extends ParserRuleContext {
		public List<Vars_declarationsContext> vars_declarations() {
			return getRuleContexts(Vars_declarationsContext.class);
		}
		public Vars_declarationsContext vars_declarations(int i) {
			return getRuleContext(Vars_declarationsContext.class,i);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			match(T__25);
			setState(173); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(172);
				vars_declarations();
				}
				}
				setState(175); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Vars_declarationsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(baby_duck_grammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(baby_duck_grammarParser.ID, i);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public Vars_declarationsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars_declarations; }
	}

	public final Vars_declarationsContext vars_declarations() throws RecognitionException {
		Vars_declarationsContext _localctx = new Vars_declarationsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_vars_declarations);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(177);
			match(ID);
			setState(182);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__21) {
				{
				{
				setState(178);
				match(T__21);
				setState(179);
				match(ID);
				}
				}
				setState(184);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(185);
			match(T__22);
			setState(186);
			type();
			setState(187);
			match(T__2);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CycleContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public CycleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cycle; }
	}

	public final CycleContext cycle() throws RecognitionException {
		CycleContext _localctx = new CycleContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			match(T__26);
			setState(190);
			body();
			setState(191);
			match(T__27);
			setState(192);
			match(T__19);
			setState(193);
			expression();
			setState(194);
			match(T__20);
			setState(195);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_keywordContext extends ParserRuleContext {
		public While_keywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_keyword; }
	}

	public final While_keywordContext while_keyword() throws RecognitionException {
		While_keywordContext _localctx = new While_keywordContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_while_keyword);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(T__27);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public Condition_elseContext condition_else() {
			return getRuleContext(Condition_elseContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			match(T__28);
			setState(200);
			match(T__19);
			setState(201);
			expression();
			setState(202);
			match(T__20);
			setState(203);
			body();
			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__29) {
				{
				setState(204);
				condition_else();
				}
			}

			setState(207);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Condition_elseContext extends ParserRuleContext {
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public Condition_elseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition_else; }
	}

	public final Condition_elseContext condition_else() throws RecognitionException {
		Condition_elseContext _localctx = new Condition_elseContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_condition_else);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(209);
			match(T__29);
			setState(210);
			body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperatorContext extends ParserRuleContext {
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			_la = _input.LA(1);
			if ( !(_la==T__30 || _la==T__31) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public OperatorContext operator() {
			return getRuleContext(OperatorContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			term();
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__30 || _la==T__31) {
				{
				setState(215);
				operator();
				setState(216);
				exp();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_operatorContext term_operator() {
			return getRuleContext(Term_operatorContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(220);
			factor();
			setState(224);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__32 || _la==T__33) {
				{
				setState(221);
				term_operator();
				setState(222);
				term();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Term_operatorContext extends ParserRuleContext {
		public Term_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term_operator; }
	}

	public final Term_operatorContext term_operator() throws RecognitionException {
		Term_operatorContext _localctx = new Term_operatorContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_term_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			_la = _input.LA(1);
			if ( !(_la==T__32 || _la==T__33) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public Parenthesized_expressionContext parenthesized_expression() {
			return getRuleContext(Parenthesized_expressionContext.class,0);
		}
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public Factor_operatorContext factor_operator() {
			return getRuleContext(Factor_operatorContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_factor);
		int _la;
		try {
			setState(236);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__19:
				enterOuterAlt(_localctx, 1);
				{
				setState(228);
				parenthesized_expression();
				}
				break;
			case T__30:
			case T__31:
			case ID:
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(230);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__30 || _la==T__31) {
					{
					setState(229);
					factor_operator();
					}
				}

				setState(234);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(232);
					match(ID);
					}
					break;
				case INT:
				case FLOAT:
					{
					setState(233);
					cte();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Factor_operatorContext extends ParserRuleContext {
		public Factor_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_operator; }
	}

	public final Factor_operatorContext factor_operator() throws RecognitionException {
		Factor_operatorContext _localctx = new Factor_operatorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_factor_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			_la = _input.LA(1);
			if ( !(_la==T__30 || _la==T__31) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Parenthesized_expressionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Parenthesized_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenthesized_expression; }
	}

	public final Parenthesized_expressionContext parenthesized_expression() throws RecognitionException {
		Parenthesized_expressionContext _localctx = new Parenthesized_expressionContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_parenthesized_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(T__19);
			setState(241);
			expression();
			setState(242);
			match(T__20);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public F_call_helperContext f_call_helper() {
			return getRuleContext(F_call_helperContext.class,0);
		}
		public F_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call; }
	}

	public final F_callContext f_call() throws RecognitionException {
		F_callContext _localctx = new F_callContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_f_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			match(ID);
			setState(245);
			match(T__19);
			setState(247);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 384400621568L) != 0)) {
				{
				setState(246);
				f_call_helper();
				}
			}

			setState(249);
			match(T__20);
			setState(250);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class F_call_helperContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public F_call_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call_helper; }
	}

	public final F_call_helperContext f_call_helper() throws RecognitionException {
		F_call_helperContext _localctx = new F_call_helperContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_f_call_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			expression();
			setState(257);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__21) {
				{
				{
				setState(253);
				match(T__21);
				setState(254);
				expression();
				}
				}
				setState(259);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001&\u0105\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0001\u0000\u0001\u0000\u0005\u0000A\b\u0000\n\u0000\f\u0000D\t\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001L\b\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0005\u0002"+
		"Q\b\u0002\n\u0002\f\u0002T\t\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0005\u0003\\\b\u0003\n\u0003\f\u0003"+
		"_\t\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004h\b\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007u\b\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0003\u000b\u0083\b\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u0088\b\u000b\u0005\u000b\u008a\b\u000b\n\u000b\f\u000b"+
		"\u008d\t\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u0092\b\f\n\f\f\f\u0095"+
		"\t\f\u0003\f\u0097\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00a3"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0004\u0010\u00ae\b\u0010\u000b"+
		"\u0010\f\u0010\u00af\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00b5"+
		"\b\u0011\n\u0011\f\u0011\u00b8\t\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014"+
		"\u00ce\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0003\u0017\u00db\b\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u00e1\b\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0003\u001a\u00e7\b\u001a\u0001\u001a\u0001\u001a\u0003\u001a\u00eb\b"+
		"\u001a\u0003\u001a\u00ed\b\u001a\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0003"+
		"\u001d\u00f8\b\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0005\u001e\u0100\b\u001e\n\u001e\f\u001e\u0103\t\u001e"+
		"\u0001\u001e\u0001B\u0000\u001f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<\u0000\u0005"+
		"\u0001\u0000\b\u000b\u0001\u0000\r\u0012\u0002\u0000$$&&\u0001\u0000\u001f"+
		" \u0001\u0000!\"\u00fe\u0000>\u0001\u0000\u0000\u0000\u0002G\u0001\u0000"+
		"\u0000\u0000\u0004R\u0001\u0000\u0000\u0000\u0006Y\u0001\u0000\u0000\u0000"+
		"\bg\u0001\u0000\u0000\u0000\ni\u0001\u0000\u0000\u0000\fk\u0001\u0000"+
		"\u0000\u0000\u000ep\u0001\u0000\u0000\u0000\u0010v\u0001\u0000\u0000\u0000"+
		"\u0012x\u0001\u0000\u0000\u0000\u0014z\u0001\u0000\u0000\u0000\u0016\u0082"+
		"\u0001\u0000\u0000\u0000\u0018\u0096\u0001\u0000\u0000\u0000\u001a\u0098"+
		"\u0001\u0000\u0000\u0000\u001c\u009c\u0001\u0000\u0000\u0000\u001e\u00a8"+
		"\u0001\u0000\u0000\u0000 \u00ab\u0001\u0000\u0000\u0000\"\u00b1\u0001"+
		"\u0000\u0000\u0000$\u00bd\u0001\u0000\u0000\u0000&\u00c5\u0001\u0000\u0000"+
		"\u0000(\u00c7\u0001\u0000\u0000\u0000*\u00d1\u0001\u0000\u0000\u0000,"+
		"\u00d4\u0001\u0000\u0000\u0000.\u00d6\u0001\u0000\u0000\u00000\u00dc\u0001"+
		"\u0000\u0000\u00002\u00e2\u0001\u0000\u0000\u00004\u00ec\u0001\u0000\u0000"+
		"\u00006\u00ee\u0001\u0000\u0000\u00008\u00f0\u0001\u0000\u0000\u0000:"+
		"\u00f4\u0001\u0000\u0000\u0000<\u00fc\u0001\u0000\u0000\u0000>B\u0005"+
		"\u0001\u0000\u0000?A\t\u0000\u0000\u0000@?\u0001\u0000\u0000\u0000AD\u0001"+
		"\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000"+
		"CE\u0001\u0000\u0000\u0000DB\u0001\u0000\u0000\u0000EF\u0005\u0001\u0000"+
		"\u0000F\u0001\u0001\u0000\u0000\u0000GH\u0005\u0002\u0000\u0000HI\u0005"+
		"#\u0000\u0000IK\u0005\u0003\u0000\u0000JL\u0003 \u0010\u0000KJ\u0001\u0000"+
		"\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MN\u0003"+
		"\u0004\u0002\u0000N\u0003\u0001\u0000\u0000\u0000OQ\u0003\u001c\u000e"+
		"\u0000PO\u0001\u0000\u0000\u0000QT\u0001\u0000\u0000\u0000RP\u0001\u0000"+
		"\u0000\u0000RS\u0001\u0000\u0000\u0000SU\u0001\u0000\u0000\u0000TR\u0001"+
		"\u0000\u0000\u0000UV\u0005\u0004\u0000\u0000VW\u0003\u0006\u0003\u0000"+
		"WX\u0005\u0005\u0000\u0000X\u0005\u0001\u0000\u0000\u0000Y]\u0005\u0006"+
		"\u0000\u0000Z\\\u0003\b\u0004\u0000[Z\u0001\u0000\u0000\u0000\\_\u0001"+
		"\u0000\u0000\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000"+
		"^`\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000`a\u0005\u0007\u0000"+
		"\u0000a\u0007\u0001\u0000\u0000\u0000bh\u0003\f\u0006\u0000ch\u0003(\u0014"+
		"\u0000dh\u0003$\u0012\u0000eh\u0003:\u001d\u0000fh\u0003\u0014\n\u0000"+
		"gb\u0001\u0000\u0000\u0000gc\u0001\u0000\u0000\u0000gd\u0001\u0000\u0000"+
		"\u0000ge\u0001\u0000\u0000\u0000gf\u0001\u0000\u0000\u0000h\t\u0001\u0000"+
		"\u0000\u0000ij\u0007\u0000\u0000\u0000j\u000b\u0001\u0000\u0000\u0000"+
		"kl\u0005#\u0000\u0000lm\u0005\f\u0000\u0000mn\u0003\u000e\u0007\u0000"+
		"no\u0005\u0003\u0000\u0000o\r\u0001\u0000\u0000\u0000pt\u0003.\u0017\u0000"+
		"qr\u0003\u0010\b\u0000rs\u0003\u000e\u0007\u0000su\u0001\u0000\u0000\u0000"+
		"tq\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000u\u000f\u0001\u0000"+
		"\u0000\u0000vw\u0007\u0001\u0000\u0000w\u0011\u0001\u0000\u0000\u0000"+
		"xy\u0007\u0002\u0000\u0000y\u0013\u0001\u0000\u0000\u0000z{\u0005\u0013"+
		"\u0000\u0000{|\u0005\u0014\u0000\u0000|}\u0003\u0016\u000b\u0000}~\u0005"+
		"\u0015\u0000\u0000~\u007f\u0005\u0003\u0000\u0000\u007f\u0015\u0001\u0000"+
		"\u0000\u0000\u0080\u0083\u0003\u000e\u0007\u0000\u0081\u0083\u0003\u0000"+
		"\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0082\u0081\u0001\u0000"+
		"\u0000\u0000\u0083\u008b\u0001\u0000\u0000\u0000\u0084\u0087\u0005\u0016"+
		"\u0000\u0000\u0085\u0088\u0003\u000e\u0007\u0000\u0086\u0088\u0003\u0000"+
		"\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0086\u0001\u0000"+
		"\u0000\u0000\u0088\u008a\u0001\u0000\u0000\u0000\u0089\u0084\u0001\u0000"+
		"\u0000\u0000\u008a\u008d\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000"+
		"\u0000\u0000\u008b\u008c\u0001\u0000\u0000\u0000\u008c\u0017\u0001\u0000"+
		"\u0000\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e\u0093\u0003\u001a"+
		"\r\u0000\u008f\u0090\u0005\u0016\u0000\u0000\u0090\u0092\u0003\u001a\r"+
		"\u0000\u0091\u008f\u0001\u0000\u0000\u0000\u0092\u0095\u0001\u0000\u0000"+
		"\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000"+
		"\u0000\u0094\u0097\u0001\u0000\u0000\u0000\u0095\u0093\u0001\u0000\u0000"+
		"\u0000\u0096\u008e\u0001\u0000\u0000\u0000\u0096\u0097\u0001\u0000\u0000"+
		"\u0000\u0097\u0019\u0001\u0000\u0000\u0000\u0098\u0099\u0005#\u0000\u0000"+
		"\u0099\u009a\u0005\u0017\u0000\u0000\u009a\u009b\u0003\n\u0005\u0000\u009b"+
		"\u001b\u0001\u0000\u0000\u0000\u009c\u009d\u0003\u001e\u000f\u0000\u009d"+
		"\u009e\u0005\u0014\u0000\u0000\u009e\u009f\u0003\u0018\f\u0000\u009f\u00a0"+
		"\u0005\u0015\u0000\u0000\u00a0\u00a2\u0005\u0018\u0000\u0000\u00a1\u00a3"+
		"\u0003 \u0010\u0000\u00a2\u00a1\u0001\u0000\u0000\u0000\u00a2\u00a3\u0001"+
		"\u0000\u0000\u0000\u00a3\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a5\u0003"+
		"\u0006\u0003\u0000\u00a5\u00a6\u0005\u0019\u0000\u0000\u00a6\u00a7\u0005"+
		"\u0003\u0000\u0000\u00a7\u001d\u0001\u0000\u0000\u0000\u00a8\u00a9\u0003"+
		"\n\u0005\u0000\u00a9\u00aa\u0005#\u0000\u0000\u00aa\u001f\u0001\u0000"+
		"\u0000\u0000\u00ab\u00ad\u0005\u001a\u0000\u0000\u00ac\u00ae\u0003\"\u0011"+
		"\u0000\u00ad\u00ac\u0001\u0000\u0000\u0000\u00ae\u00af\u0001\u0000\u0000"+
		"\u0000\u00af\u00ad\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000\u0000"+
		"\u0000\u00b0!\u0001\u0000\u0000\u0000\u00b1\u00b6\u0005#\u0000\u0000\u00b2"+
		"\u00b3\u0005\u0016\u0000\u0000\u00b3\u00b5\u0005#\u0000\u0000\u00b4\u00b2"+
		"\u0001\u0000\u0000\u0000\u00b5\u00b8\u0001\u0000\u0000\u0000\u00b6\u00b4"+
		"\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000\u0000\u00b7\u00b9"+
		"\u0001\u0000\u0000\u0000\u00b8\u00b6\u0001\u0000\u0000\u0000\u00b9\u00ba"+
		"\u0005\u0017\u0000\u0000\u00ba\u00bb\u0003\n\u0005\u0000\u00bb\u00bc\u0005"+
		"\u0003\u0000\u0000\u00bc#\u0001\u0000\u0000\u0000\u00bd\u00be\u0005\u001b"+
		"\u0000\u0000\u00be\u00bf\u0003\u0006\u0003\u0000\u00bf\u00c0\u0005\u001c"+
		"\u0000\u0000\u00c0\u00c1\u0005\u0014\u0000\u0000\u00c1\u00c2\u0003\u000e"+
		"\u0007\u0000\u00c2\u00c3\u0005\u0015\u0000\u0000\u00c3\u00c4\u0005\u0003"+
		"\u0000\u0000\u00c4%\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\u001c\u0000"+
		"\u0000\u00c6\'\u0001\u0000\u0000\u0000\u00c7\u00c8\u0005\u001d\u0000\u0000"+
		"\u00c8\u00c9\u0005\u0014\u0000\u0000\u00c9\u00ca\u0003\u000e\u0007\u0000"+
		"\u00ca\u00cb\u0005\u0015\u0000\u0000\u00cb\u00cd\u0003\u0006\u0003\u0000"+
		"\u00cc\u00ce\u0003*\u0015\u0000\u00cd\u00cc\u0001\u0000\u0000\u0000\u00cd"+
		"\u00ce\u0001\u0000\u0000\u0000\u00ce\u00cf\u0001\u0000\u0000\u0000\u00cf"+
		"\u00d0\u0005\u0003\u0000\u0000\u00d0)\u0001\u0000\u0000\u0000\u00d1\u00d2"+
		"\u0005\u001e\u0000\u0000\u00d2\u00d3\u0003\u0006\u0003\u0000\u00d3+\u0001"+
		"\u0000\u0000\u0000\u00d4\u00d5\u0007\u0003\u0000\u0000\u00d5-\u0001\u0000"+
		"\u0000\u0000\u00d6\u00da\u00030\u0018\u0000\u00d7\u00d8\u0003,\u0016\u0000"+
		"\u00d8\u00d9\u0003.\u0017\u0000\u00d9\u00db\u0001\u0000\u0000\u0000\u00da"+
		"\u00d7\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000\u0000\u0000\u00db"+
		"/\u0001\u0000\u0000\u0000\u00dc\u00e0\u00034\u001a\u0000\u00dd\u00de\u0003"+
		"2\u0019\u0000\u00de\u00df\u00030\u0018\u0000\u00df\u00e1\u0001\u0000\u0000"+
		"\u0000\u00e0\u00dd\u0001\u0000\u0000\u0000\u00e0\u00e1\u0001\u0000\u0000"+
		"\u0000\u00e11\u0001\u0000\u0000\u0000\u00e2\u00e3\u0007\u0004\u0000\u0000"+
		"\u00e33\u0001\u0000\u0000\u0000\u00e4\u00ed\u00038\u001c\u0000\u00e5\u00e7"+
		"\u00036\u001b\u0000\u00e6\u00e5\u0001\u0000\u0000\u0000\u00e6\u00e7\u0001"+
		"\u0000\u0000\u0000\u00e7\u00ea\u0001\u0000\u0000\u0000\u00e8\u00eb\u0005"+
		"#\u0000\u0000\u00e9\u00eb\u0003\u0012\t\u0000\u00ea\u00e8\u0001\u0000"+
		"\u0000\u0000\u00ea\u00e9\u0001\u0000\u0000\u0000\u00eb\u00ed\u0001\u0000"+
		"\u0000\u0000\u00ec\u00e4\u0001\u0000\u0000\u0000\u00ec\u00e6\u0001\u0000"+
		"\u0000\u0000\u00ed5\u0001\u0000\u0000\u0000\u00ee\u00ef\u0007\u0003\u0000"+
		"\u0000\u00ef7\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005\u0014\u0000\u0000"+
		"\u00f1\u00f2\u0003\u000e\u0007\u0000\u00f2\u00f3\u0005\u0015\u0000\u0000"+
		"\u00f39\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005#\u0000\u0000\u00f5\u00f7"+
		"\u0005\u0014\u0000\u0000\u00f6\u00f8\u0003<\u001e\u0000\u00f7\u00f6\u0001"+
		"\u0000\u0000\u0000\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u00f9\u0001"+
		"\u0000\u0000\u0000\u00f9\u00fa\u0005\u0015\u0000\u0000\u00fa\u00fb\u0005"+
		"\u0003\u0000\u0000\u00fb;\u0001\u0000\u0000\u0000\u00fc\u0101\u0003\u000e"+
		"\u0007\u0000\u00fd\u00fe\u0005\u0016\u0000\u0000\u00fe\u0100\u0003\u000e"+
		"\u0007\u0000\u00ff\u00fd\u0001\u0000\u0000\u0000\u0100\u0103\u0001\u0000"+
		"\u0000\u0000\u0101\u00ff\u0001\u0000\u0000\u0000\u0101\u0102\u0001\u0000"+
		"\u0000\u0000\u0102=\u0001\u0000\u0000\u0000\u0103\u0101\u0001\u0000\u0000"+
		"\u0000\u0016BKR]gt\u0082\u0087\u008b\u0093\u0096\u00a2\u00af\u00b6\u00cd"+
		"\u00da\u00e0\u00e6\u00ea\u00ec\u00f7\u0101";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}