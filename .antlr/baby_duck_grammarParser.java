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
		T__24=25, T__25=26, T__26=27, ID=28, INT=29, WS=30, STRING=31;
	public static final int
		RULE_program = 0, RULE_funcs_list = 1, RULE_body = 2, RULE_statement_list = 3, 
		RULE_statement = 4, RULE_type = 5, RULE_assign = 6, RULE_expression = 7, 
		RULE_rel_op = 8, RULE_cte = 9, RULE_exp = 10, RULE_f_param_list = 11, 
		RULE_f_param_list_helper = 12, RULE_funcs = 13, RULE_vars = 14, RULE_print = 15, 
		RULE_print_arg = 16, RULE_print_helper = 17, RULE_print_helper_inner = 18, 
		RULE_cycle = 19, RULE_condition = 20, RULE_condition_else = 21, RULE_term = 22, 
		RULE_term_helper = 23, RULE_factor = 24, RULE_factor_expr = 25, RULE_factor_op = 26, 
		RULE_f_call = 27, RULE_f_call_helper = 28, RULE_expression_list = 29, 
		RULE_expression_list_helper = 30;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "funcs_list", "body", "statement_list", "statement", "type", 
			"assign", "expression", "rel_op", "cte", "exp", "f_param_list", "f_param_list_helper", 
			"funcs", "vars", "print", "print_arg", "print_helper", "print_helper_inner", 
			"cycle", "condition", "condition_else", "term", "term_helper", "factor", 
			"factor_expr", "factor_op", "f_call", "f_call_helper", "expression_list", 
			"expression_list_helper"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "';'", "'{'", "'}'", "'int'", "'float'", "'='", "'<'", 
			"'>'", "'!='", "'+'", "'-'", "'('", "')'", "':'", "','", "'void'", "'['", 
			"']'", "'var'", "'print'", "'while'", "'do'", "'if'", "'else'", "'*'", 
			"'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "ID", "INT", "WS", "STRING"
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
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
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
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__0);
			setState(63);
			match(ID);
			setState(64);
			match(T__1);
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__19) {
				{
				setState(65);
				vars();
				}
			}

			setState(68);
			funcs();
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
	public static class Funcs_listContext extends ParserRuleContext {
		public FuncsContext funcs() {
			return getRuleContext(FuncsContext.class,0);
		}
		public Funcs_listContext funcs_list() {
			return getRuleContext(Funcs_listContext.class,0);
		}
		public Funcs_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcs_list; }
	}

	public final Funcs_listContext funcs_list() throws RecognitionException {
		Funcs_listContext _localctx = new Funcs_listContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_funcs_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			funcs();
			setState(72);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(71);
				funcs_list();
				}
				break;
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
		enterRule(_localctx, 4, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(T__2);
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 291512320L) != 0)) {
				{
				{
				setState(75);
				statement();
				}
				}
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(81);
			match(T__3);
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
	public static class Statement_listContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public Statement_listContext statement_list() {
			return getRuleContext(Statement_listContext.class,0);
		}
		public Statement_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement_list; }
	}

	public final Statement_listContext statement_list() throws RecognitionException {
		Statement_listContext _localctx = new Statement_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			statement();
			setState(85);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(84);
				statement_list();
				}
				break;
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
			setState(92);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(87);
				assign();
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 2);
				{
				setState(88);
				condition();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 3);
				{
				setState(89);
				cycle();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 4);
				{
				setState(90);
				f_call();
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 5);
				{
				setState(91);
				print();
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
			setState(94);
			_la = _input.LA(1);
			if ( !(_la==T__4 || _la==T__5) ) {
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
			setState(96);
			match(ID);
			setState(97);
			match(T__6);
			setState(98);
			expression();
			setState(99);
			match(T__1);
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
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public Rel_opContext rel_op() {
			return getRuleContext(Rel_opContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expression);
		try {
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				exp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(102);
				exp();
				setState(103);
				rel_op();
				setState(104);
				exp();
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
			setState(108);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1792L) != 0)) ) {
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
			setState(110);
			_la = _input.LA(1);
			if ( !(_la==T__5 || _la==INT) ) {
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
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			term();
			setState(117);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__10 || _la==T__11) {
				{
				{
				setState(113);
				_la = _input.LA(1);
				if ( !(_la==T__10 || _la==T__11) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(114);
				term();
				}
				}
				setState(119);
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
		public F_param_list_helperContext f_param_list_helper() {
			return getRuleContext(F_param_list_helperContext.class,0);
		}
		public F_param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_param_list; }
	}

	public final F_param_listContext f_param_list() throws RecognitionException {
		F_param_listContext _localctx = new F_param_listContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_f_param_list);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(T__12);
			setState(121);
			f_param_list_helper();
			setState(122);
			match(T__13);
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
		public F_param_list_helperContext f_param_list_helper() {
			return getRuleContext(F_param_list_helperContext.class,0);
		}
		public F_param_list_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_param_list_helper; }
	}

	public final F_param_list_helperContext f_param_list_helper() throws RecognitionException {
		F_param_list_helperContext _localctx = new F_param_list_helperContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_f_param_list_helper);
		try {
			setState(133);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				match(ID);
				setState(125);
				match(T__14);
				setState(126);
				type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				match(ID);
				setState(128);
				match(T__14);
				setState(129);
				type();
				setState(130);
				match(T__15);
				setState(131);
				f_param_list_helper();
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
	public static class FuncsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
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
		enterRule(_localctx, 26, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(T__16);
			setState(136);
			match(ID);
			setState(137);
			match(T__12);
			setState(138);
			f_param_list();
			setState(139);
			match(T__13);
			setState(140);
			match(T__17);
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__19) {
				{
				setState(141);
				vars();
				}
			}

			setState(144);
			body();
			setState(145);
			match(T__18);
			setState(146);
			match(T__1);
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
		public List<TerminalNode> ID() { return getTokens(baby_duck_grammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(baby_duck_grammarParser.ID, i);
		}
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public VarsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vars; }
	}

	public final VarsContext vars() throws RecognitionException {
		VarsContext _localctx = new VarsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__19);
			setState(149);
			match(ID);
			setState(154);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(150);
				match(T__15);
				setState(151);
				match(ID);
				}
				}
				setState(156);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(157);
			match(T__14);
			setState(158);
			type();
			setState(159);
			match(T__1);
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
		enterRule(_localctx, 30, RULE_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(T__20);
			setState(162);
			match(T__12);
			setState(163);
			print_helper();
			setState(164);
			match(T__13);
			setState(165);
			match(T__1);
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
	public static class Print_argContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode STRING() { return getToken(baby_duck_grammarParser.STRING, 0); }
		public Print_argContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_arg; }
	}

	public final Print_argContext print_arg() throws RecognitionException {
		Print_argContext _localctx = new Print_argContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_print_arg);
		try {
			setState(169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
			case T__11:
			case T__12:
				enterOuterAlt(_localctx, 1);
				{
				setState(167);
				expression();
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(168);
				match(STRING);
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
	public static class Print_helperContext extends ParserRuleContext {
		public Print_argContext print_arg() {
			return getRuleContext(Print_argContext.class,0);
		}
		public Print_helper_innerContext print_helper_inner() {
			return getRuleContext(Print_helper_innerContext.class,0);
		}
		public Print_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_helper; }
	}

	public final Print_helperContext print_helper() throws RecognitionException {
		Print_helperContext _localctx = new Print_helperContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_print_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			print_arg();
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(172);
				print_helper_inner();
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
	public static class Print_helper_innerContext extends ParserRuleContext {
		public Print_argContext print_arg() {
			return getRuleContext(Print_argContext.class,0);
		}
		public Print_helper_innerContext print_helper_inner() {
			return getRuleContext(Print_helper_innerContext.class,0);
		}
		public Print_helper_innerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_print_helper_inner; }
	}

	public final Print_helper_innerContext print_helper_inner() throws RecognitionException {
		Print_helper_innerContext _localctx = new Print_helper_innerContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_print_helper_inner);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(T__15);
			setState(176);
			print_arg();
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(177);
				print_helper_inner();
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
		enterRule(_localctx, 38, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			match(T__21);
			setState(181);
			body();
			setState(182);
			match(T__22);
			setState(183);
			match(T__12);
			setState(184);
			expression();
			setState(185);
			match(T__13);
			setState(186);
			match(T__1);
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
			setState(188);
			match(T__23);
			setState(189);
			match(T__12);
			setState(190);
			expression();
			setState(191);
			match(T__13);
			setState(192);
			body();
			setState(194);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__24) {
				{
				setState(193);
				condition_else();
				}
			}

			setState(196);
			match(T__1);
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
			setState(198);
			match(T__24);
			setState(199);
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
	public static class TermContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_helperContext term_helper() {
			return getRuleContext(Term_helperContext.class,0);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			factor();
			setState(203);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25 || _la==T__26) {
				{
				setState(202);
				term_helper();
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
	public static class Term_helperContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Term_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term_helper; }
	}

	public final Term_helperContext term_helper() throws RecognitionException {
		Term_helperContext _localctx = new Term_helperContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_term_helper);
		try {
			setState(209);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
				enterOuterAlt(_localctx, 1);
				{
				setState(205);
				match(T__25);
				setState(206);
				term();
				}
				break;
			case T__26:
				enterOuterAlt(_localctx, 2);
				{
				setState(207);
				match(T__26);
				setState(208);
				term();
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
	public static class FactorContext extends ParserRuleContext {
		public Factor_exprContext factor_expr() {
			return getRuleContext(Factor_exprContext.class,0);
		}
		public Factor_opContext factor_op() {
			return getRuleContext(Factor_opContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_factor);
		try {
			setState(213);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__12:
				enterOuterAlt(_localctx, 1);
				{
				setState(211);
				factor_expr();
				}
				break;
			case T__10:
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				setState(212);
				factor_op();
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
	public static class Factor_exprContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Factor_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_expr; }
	}

	public final Factor_exprContext factor_expr() throws RecognitionException {
		Factor_exprContext _localctx = new Factor_exprContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_factor_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215);
			match(T__12);
			setState(216);
			expression();
			setState(217);
			match(T__13);
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
	public static class Factor_opContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public Factor_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor_op; }
	}

	public final Factor_opContext factor_op() throws RecognitionException {
		Factor_opContext _localctx = new Factor_opContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_factor_op);
		try {
			setState(227);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(219);
				match(T__10);
				setState(220);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(221);
				match(T__10);
				setState(222);
				cte();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(223);
				match(T__11);
				setState(224);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(225);
				match(T__11);
				setState(226);
				cte();
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
	public static class F_callContext extends ParserRuleContext {
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
		enterRule(_localctx, 54, RULE_f_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			match(T__12);
			setState(230);
			f_call_helper();
			setState(231);
			match(T__13);
			setState(232);
			match(T__1);
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
		public Expression_listContext expression_list() {
			return getRuleContext(Expression_listContext.class,0);
		}
		public F_call_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_f_call_helper; }
	}

	public final F_call_helperContext f_call_helper() throws RecognitionException {
		F_call_helperContext _localctx = new F_call_helperContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_f_call_helper);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			expression_list();
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
	public static class Expression_listContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expression_list_helperContext expression_list_helper() {
			return getRuleContext(Expression_list_helperContext.class,0);
		}
		public Expression_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_list; }
	}

	public final Expression_listContext expression_list() throws RecognitionException {
		Expression_listContext _localctx = new Expression_listContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_expression_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			expression();
			setState(238);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(237);
				expression_list_helper();
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
	public static class Expression_list_helperContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public Expression_list_helperContext expression_list_helper() {
			return getRuleContext(Expression_list_helperContext.class,0);
		}
		public Expression_list_helperContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression_list_helper; }
	}

	public final Expression_list_helperContext expression_list_helper() throws RecognitionException {
		Expression_list_helperContext _localctx = new Expression_list_helperContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_expression_list_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(240);
			match(T__15);
			setState(241);
			expression();
			setState(243);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__15) {
				{
				setState(242);
				expression_list_helper();
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

	public static final String _serializedATN =
		"\u0004\u0001\u001f\u00f6\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003\u0000C\b"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0003\u0001I\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0005\u0002M\b\u0002\n\u0002\f\u0002P\t"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0003\u0003V\b"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003"+
		"\u0004]\b\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0003\u0007k\b\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0005\nt\b\n\n\n\f\nw\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u0086\b\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u008f\b\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e"+
		"\u0099\b\u000e\n\u000e\f\u000e\u009c\t\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0003\u0010\u00aa\b\u0010\u0001"+
		"\u0011\u0001\u0011\u0003\u0011\u00ae\b\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0003\u0012\u00b3\b\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001"+
		"\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0003\u0014\u00c3"+
		"\b\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0003\u0016\u00cc\b\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0003\u0017\u00d2\b\u0017\u0001\u0018\u0001\u0018\u0003"+
		"\u0018\u00d6\b\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0003\u001a\u00e4\b\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d\u0001"+
		"\u001d\u0003\u001d\u00ef\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0003"+
		"\u001e\u00f4\b\u001e\u0001\u001e\u0000\u0000\u001f\u0000\u0002\u0004\u0006"+
		"\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,."+
		"02468:<\u0000\u0004\u0001\u0000\u0005\u0006\u0001\u0000\b\n\u0002\u0000"+
		"\u0006\u0006\u001d\u001d\u0001\u0000\u000b\f\u00ef\u0000>\u0001\u0000"+
		"\u0000\u0000\u0002F\u0001\u0000\u0000\u0000\u0004J\u0001\u0000\u0000\u0000"+
		"\u0006S\u0001\u0000\u0000\u0000\b\\\u0001\u0000\u0000\u0000\n^\u0001\u0000"+
		"\u0000\u0000\f`\u0001\u0000\u0000\u0000\u000ej\u0001\u0000\u0000\u0000"+
		"\u0010l\u0001\u0000\u0000\u0000\u0012n\u0001\u0000\u0000\u0000\u0014p"+
		"\u0001\u0000\u0000\u0000\u0016x\u0001\u0000\u0000\u0000\u0018\u0085\u0001"+
		"\u0000\u0000\u0000\u001a\u0087\u0001\u0000\u0000\u0000\u001c\u0094\u0001"+
		"\u0000\u0000\u0000\u001e\u00a1\u0001\u0000\u0000\u0000 \u00a9\u0001\u0000"+
		"\u0000\u0000\"\u00ab\u0001\u0000\u0000\u0000$\u00af\u0001\u0000\u0000"+
		"\u0000&\u00b4\u0001\u0000\u0000\u0000(\u00bc\u0001\u0000\u0000\u0000*"+
		"\u00c6\u0001\u0000\u0000\u0000,\u00c9\u0001\u0000\u0000\u0000.\u00d1\u0001"+
		"\u0000\u0000\u00000\u00d5\u0001\u0000\u0000\u00002\u00d7\u0001\u0000\u0000"+
		"\u00004\u00e3\u0001\u0000\u0000\u00006\u00e5\u0001\u0000\u0000\u00008"+
		"\u00ea\u0001\u0000\u0000\u0000:\u00ec\u0001\u0000\u0000\u0000<\u00f0\u0001"+
		"\u0000\u0000\u0000>?\u0005\u0001\u0000\u0000?@\u0005\u001c\u0000\u0000"+
		"@B\u0005\u0002\u0000\u0000AC\u0003\u001c\u000e\u0000BA\u0001\u0000\u0000"+
		"\u0000BC\u0001\u0000\u0000\u0000CD\u0001\u0000\u0000\u0000DE\u0003\u001a"+
		"\r\u0000E\u0001\u0001\u0000\u0000\u0000FH\u0003\u001a\r\u0000GI\u0003"+
		"\u0002\u0001\u0000HG\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000"+
		"I\u0003\u0001\u0000\u0000\u0000JN\u0005\u0003\u0000\u0000KM\u0003\b\u0004"+
		"\u0000LK\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001\u0000"+
		"\u0000\u0000NO\u0001\u0000\u0000\u0000OQ\u0001\u0000\u0000\u0000PN\u0001"+
		"\u0000\u0000\u0000QR\u0005\u0004\u0000\u0000R\u0005\u0001\u0000\u0000"+
		"\u0000SU\u0003\b\u0004\u0000TV\u0003\u0006\u0003\u0000UT\u0001\u0000\u0000"+
		"\u0000UV\u0001\u0000\u0000\u0000V\u0007\u0001\u0000\u0000\u0000W]\u0003"+
		"\f\u0006\u0000X]\u0003(\u0014\u0000Y]\u0003&\u0013\u0000Z]\u00036\u001b"+
		"\u0000[]\u0003\u001e\u000f\u0000\\W\u0001\u0000\u0000\u0000\\X\u0001\u0000"+
		"\u0000\u0000\\Y\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000\\["+
		"\u0001\u0000\u0000\u0000]\t\u0001\u0000\u0000\u0000^_\u0007\u0000\u0000"+
		"\u0000_\u000b\u0001\u0000\u0000\u0000`a\u0005\u001c\u0000\u0000ab\u0005"+
		"\u0007\u0000\u0000bc\u0003\u000e\u0007\u0000cd\u0005\u0002\u0000\u0000"+
		"d\r\u0001\u0000\u0000\u0000ek\u0003\u0014\n\u0000fg\u0003\u0014\n\u0000"+
		"gh\u0003\u0010\b\u0000hi\u0003\u0014\n\u0000ik\u0001\u0000\u0000\u0000"+
		"je\u0001\u0000\u0000\u0000jf\u0001\u0000\u0000\u0000k\u000f\u0001\u0000"+
		"\u0000\u0000lm\u0007\u0001\u0000\u0000m\u0011\u0001\u0000\u0000\u0000"+
		"no\u0007\u0002\u0000\u0000o\u0013\u0001\u0000\u0000\u0000pu\u0003,\u0016"+
		"\u0000qr\u0007\u0003\u0000\u0000rt\u0003,\u0016\u0000sq\u0001\u0000\u0000"+
		"\u0000tw\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001\u0000"+
		"\u0000\u0000v\u0015\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000"+
		"xy\u0005\r\u0000\u0000yz\u0003\u0018\f\u0000z{\u0005\u000e\u0000\u0000"+
		"{\u0017\u0001\u0000\u0000\u0000|}\u0005\u001c\u0000\u0000}~\u0005\u000f"+
		"\u0000\u0000~\u0086\u0003\n\u0005\u0000\u007f\u0080\u0005\u001c\u0000"+
		"\u0000\u0080\u0081\u0005\u000f\u0000\u0000\u0081\u0082\u0003\n\u0005\u0000"+
		"\u0082\u0083\u0005\u0010\u0000\u0000\u0083\u0084\u0003\u0018\f\u0000\u0084"+
		"\u0086\u0001\u0000\u0000\u0000\u0085|\u0001\u0000\u0000\u0000\u0085\u007f"+
		"\u0001\u0000\u0000\u0000\u0086\u0019\u0001\u0000\u0000\u0000\u0087\u0088"+
		"\u0005\u0011\u0000\u0000\u0088\u0089\u0005\u001c\u0000\u0000\u0089\u008a"+
		"\u0005\r\u0000\u0000\u008a\u008b\u0003\u0016\u000b\u0000\u008b\u008c\u0005"+
		"\u000e\u0000\u0000\u008c\u008e\u0005\u0012\u0000\u0000\u008d\u008f\u0003"+
		"\u001c\u000e\u0000\u008e\u008d\u0001\u0000\u0000\u0000\u008e\u008f\u0001"+
		"\u0000\u0000\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0091\u0003"+
		"\u0004\u0002\u0000\u0091\u0092\u0005\u0013\u0000\u0000\u0092\u0093\u0005"+
		"\u0002\u0000\u0000\u0093\u001b\u0001\u0000\u0000\u0000\u0094\u0095\u0005"+
		"\u0014\u0000\u0000\u0095\u009a\u0005\u001c\u0000\u0000\u0096\u0097\u0005"+
		"\u0010\u0000\u0000\u0097\u0099\u0005\u001c\u0000\u0000\u0098\u0096\u0001"+
		"\u0000\u0000\u0000\u0099\u009c\u0001\u0000\u0000\u0000\u009a\u0098\u0001"+
		"\u0000\u0000\u0000\u009a\u009b\u0001\u0000\u0000\u0000\u009b\u009d\u0001"+
		"\u0000\u0000\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009d\u009e\u0005"+
		"\u000f\u0000\u0000\u009e\u009f\u0003\n\u0005\u0000\u009f\u00a0\u0005\u0002"+
		"\u0000\u0000\u00a0\u001d\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005\u0015"+
		"\u0000\u0000\u00a2\u00a3\u0005\r\u0000\u0000\u00a3\u00a4\u0003\"\u0011"+
		"\u0000\u00a4\u00a5\u0005\u000e\u0000\u0000\u00a5\u00a6\u0005\u0002\u0000"+
		"\u0000\u00a6\u001f\u0001\u0000\u0000\u0000\u00a7\u00aa\u0003\u000e\u0007"+
		"\u0000\u00a8\u00aa\u0005\u001f\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000"+
		"\u0000\u00a9\u00a8\u0001\u0000\u0000\u0000\u00aa!\u0001\u0000\u0000\u0000"+
		"\u00ab\u00ad\u0003 \u0010\u0000\u00ac\u00ae\u0003$\u0012\u0000\u00ad\u00ac"+
		"\u0001\u0000\u0000\u0000\u00ad\u00ae\u0001\u0000\u0000\u0000\u00ae#\u0001"+
		"\u0000\u0000\u0000\u00af\u00b0\u0005\u0010\u0000\u0000\u00b0\u00b2\u0003"+
		" \u0010\u0000\u00b1\u00b3\u0003$\u0012\u0000\u00b2\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b2\u00b3\u0001\u0000\u0000\u0000\u00b3%\u0001\u0000\u0000\u0000"+
		"\u00b4\u00b5\u0005\u0016\u0000\u0000\u00b5\u00b6\u0003\u0004\u0002\u0000"+
		"\u00b6\u00b7\u0005\u0017\u0000\u0000\u00b7\u00b8\u0005\r\u0000\u0000\u00b8"+
		"\u00b9\u0003\u000e\u0007\u0000\u00b9\u00ba\u0005\u000e\u0000\u0000\u00ba"+
		"\u00bb\u0005\u0002\u0000\u0000\u00bb\'\u0001\u0000\u0000\u0000\u00bc\u00bd"+
		"\u0005\u0018\u0000\u0000\u00bd\u00be\u0005\r\u0000\u0000\u00be\u00bf\u0003"+
		"\u000e\u0007\u0000\u00bf\u00c0\u0005\u000e\u0000\u0000\u00c0\u00c2\u0003"+
		"\u0004\u0002\u0000\u00c1\u00c3\u0003*\u0015\u0000\u00c2\u00c1\u0001\u0000"+
		"\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000\u0000\u00c3\u00c4\u0001\u0000"+
		"\u0000\u0000\u00c4\u00c5\u0005\u0002\u0000\u0000\u00c5)\u0001\u0000\u0000"+
		"\u0000\u00c6\u00c7\u0005\u0019\u0000\u0000\u00c7\u00c8\u0003\u0004\u0002"+
		"\u0000\u00c8+\u0001\u0000\u0000\u0000\u00c9\u00cb\u00030\u0018\u0000\u00ca"+
		"\u00cc\u0003.\u0017\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000\u00cb\u00cc"+
		"\u0001\u0000\u0000\u0000\u00cc-\u0001\u0000\u0000\u0000\u00cd\u00ce\u0005"+
		"\u001a\u0000\u0000\u00ce\u00d2\u0003,\u0016\u0000\u00cf\u00d0\u0005\u001b"+
		"\u0000\u0000\u00d0\u00d2\u0003,\u0016\u0000\u00d1\u00cd\u0001\u0000\u0000"+
		"\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d2/\u0001\u0000\u0000\u0000"+
		"\u00d3\u00d6\u00032\u0019\u0000\u00d4\u00d6\u00034\u001a\u0000\u00d5\u00d3"+
		"\u0001\u0000\u0000\u0000\u00d5\u00d4\u0001\u0000\u0000\u0000\u00d61\u0001"+
		"\u0000\u0000\u0000\u00d7\u00d8\u0005\r\u0000\u0000\u00d8\u00d9\u0003\u000e"+
		"\u0007\u0000\u00d9\u00da\u0005\u000e\u0000\u0000\u00da3\u0001\u0000\u0000"+
		"\u0000\u00db\u00dc\u0005\u000b\u0000\u0000\u00dc\u00e4\u0005\u001c\u0000"+
		"\u0000\u00dd\u00de\u0005\u000b\u0000\u0000\u00de\u00e4\u0003\u0012\t\u0000"+
		"\u00df\u00e0\u0005\f\u0000\u0000\u00e0\u00e4\u0005\u001c\u0000\u0000\u00e1"+
		"\u00e2\u0005\f\u0000\u0000\u00e2\u00e4\u0003\u0012\t\u0000\u00e3\u00db"+
		"\u0001\u0000\u0000\u0000\u00e3\u00dd\u0001\u0000\u0000\u0000\u00e3\u00df"+
		"\u0001\u0000\u0000\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e45\u0001"+
		"\u0000\u0000\u0000\u00e5\u00e6\u0005\r\u0000\u0000\u00e6\u00e7\u00038"+
		"\u001c\u0000\u00e7\u00e8\u0005\u000e\u0000\u0000\u00e8\u00e9\u0005\u0002"+
		"\u0000\u0000\u00e97\u0001\u0000\u0000\u0000\u00ea\u00eb\u0003:\u001d\u0000"+
		"\u00eb9\u0001\u0000\u0000\u0000\u00ec\u00ee\u0003\u000e\u0007\u0000\u00ed"+
		"\u00ef\u0003<\u001e\u0000\u00ee\u00ed\u0001\u0000\u0000\u0000\u00ee\u00ef"+
		"\u0001\u0000\u0000\u0000\u00ef;\u0001\u0000\u0000\u0000\u00f0\u00f1\u0005"+
		"\u0010\u0000\u0000\u00f1\u00f3\u0003\u000e\u0007\u0000\u00f2\u00f4\u0003"+
		"<\u001e\u0000\u00f3\u00f2\u0001\u0000\u0000\u0000\u00f3\u00f4\u0001\u0000"+
		"\u0000\u0000\u00f4=\u0001\u0000\u0000\u0000\u0014BHNU\\ju\u0085\u008e"+
		"\u009a\u00a9\u00ad\u00b2\u00c2\u00cb\u00d1\u00d5\u00e3\u00ee\u00f3";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}