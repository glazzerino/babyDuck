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
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, ID=31, INT=32, 
		WS=33, FLOAT=34, STRING=35;
	public static final int
		RULE_program = 0, RULE_program_post_var = 1, RULE_body = 2, RULE_statement = 3, 
		RULE_type = 4, RULE_assign = 5, RULE_expression = 6, RULE_rel_op = 7, 
		RULE_cte = 8, RULE_exp = 9, RULE_print = 10, RULE_print_helper = 11, RULE_f_param_list = 12, 
		RULE_f_param_list_helper = 13, RULE_funcs = 14, RULE_vars = 15, RULE_vars_declarations = 16, 
		RULE_cycle = 17, RULE_condition = 18, RULE_condition_else = 19, RULE_term = 20, 
		RULE_factor = 21, RULE_f_call = 22, RULE_f_call_helper = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "program_post_var", "body", "statement", "type", "assign", 
			"expression", "rel_op", "cte", "exp", "print", "print_helper", "f_param_list", 
			"f_param_list_helper", "funcs", "vars", "vars_declarations", "cycle", 
			"condition", "condition_else", "term", "factor", "f_call", "f_call_helper"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "';'", "'main'", "'end'", "'{'", "'}'", "'int'", "'float'", 
			"'bool'", "'void'", "'='", "'<'", "'>'", "'!='", "'+'", "'-'", "'print'", 
			"'('", "')'", "','", "':'", "'['", "']'", "'var'", "'while'", "'do'", 
			"'if'", "'else'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, "ID", "INT", "WS", "FLOAT", 
			"STRING"
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
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(T__0);
			setState(49);
			match(ID);
			setState(50);
			match(T__1);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__23) {
				{
				setState(51);
				vars();
				}
			}

			setState(54);
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
		enterRule(_localctx, 2, RULE_program_post_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) {
				{
				{
				setState(56);
				funcs();
				}
				}
				setState(61);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(62);
			match(T__2);
			setState(63);
			body();
			setState(64);
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
			setState(66);
			match(T__4);
			setState(70);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2315386880L) != 0)) {
				{
				{
				setState(67);
				statement();
				}
				}
				setState(72);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(73);
			match(T__5);
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
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(80);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(75);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(76);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(77);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(78);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(79);
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
		enterRule(_localctx, 8, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) ) {
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
		enterRule(_localctx, 10, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(ID);
			setState(85);
			match(T__10);
			setState(86);
			expression();
			setState(87);
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
		enterRule(_localctx, 12, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			exp();
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 28672L) != 0)) {
				{
				setState(90);
				rel_op();
				setState(91);
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
	public static class Rel_opContext extends ParserRuleContext {
		public Rel_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rel_op; }
	}

	public final Rel_opContext rel_op() throws RecognitionException {
		Rel_opContext _localctx = new Rel_opContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 28672L) != 0)) ) {
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
		enterRule(_localctx, 16, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
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
		enterRule(_localctx, 18, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			term();
			setState(104);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14 || _la==T__15) {
				{
				{
				setState(100);
				_la = _input.LA(1);
				if ( !(_la==T__14 || _la==T__15) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(101);
				term();
				}
				}
				setState(106);
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
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(T__16);
			setState(108);
			match(T__17);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 57982418944L) != 0)) {
				{
				setState(109);
				print_helper();
				}
			}

			setState(112);
			match(T__18);
			setState(113);
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
	public static class Print_helperContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public List<TerminalNode> STRING() { return getTokens(baby_duck_grammarParser.STRING); }
		public TerminalNode STRING(int i) {
			return getToken(baby_duck_grammarParser.STRING, i);
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
			setState(117);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__14:
			case T__15:
			case T__17:
			case ID:
			case INT:
			case FLOAT:
				{
				setState(115);
				expression();
				}
				break;
			case STRING:
				{
				setState(116);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__19) {
				{
				{
				setState(119);
				match(T__19);
				setState(122);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__14:
				case T__15:
				case T__17:
				case ID:
				case INT:
				case FLOAT:
					{
					setState(120);
					expression();
					}
					break;
				case STRING:
					{
					setState(121);
					match(STRING);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(128);
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
			setState(137);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(129);
				f_param_list_helper();
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__19) {
					{
					{
					setState(130);
					match(T__19);
					setState(131);
					f_param_list_helper();
					}
					}
					setState(136);
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
			setState(139);
			match(ID);
			setState(140);
			match(T__20);
			setState(141);
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
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
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
		enterRule(_localctx, 28, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			type();
			setState(144);
			match(ID);
			setState(145);
			match(T__17);
			setState(146);
			f_param_list();
			setState(147);
			match(T__18);
			setState(148);
			match(T__21);
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__23) {
				{
				setState(149);
				vars();
				}
			}

			setState(152);
			body();
			setState(153);
			match(T__22);
			setState(154);
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
		enterRule(_localctx, 30, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(T__23);
			setState(158); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(157);
				vars_declarations();
				}
				}
				setState(160); 
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
		enterRule(_localctx, 32, RULE_vars_declarations);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(162);
			match(ID);
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__19) {
				{
				{
				setState(163);
				match(T__19);
				setState(164);
				match(ID);
				}
				}
				setState(169);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(170);
			match(T__20);
			setState(171);
			type();
			setState(172);
			match(T__1);
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
		enterRule(_localctx, 34, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(T__24);
			setState(175);
			body();
			setState(176);
			match(T__25);
			setState(177);
			match(T__17);
			setState(178);
			expression();
			setState(179);
			match(T__18);
			setState(180);
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
		enterRule(_localctx, 36, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			match(T__26);
			setState(183);
			match(T__17);
			setState(184);
			expression();
			setState(185);
			match(T__18);
			setState(186);
			body();
			setState(188);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__27) {
				{
				setState(187);
				condition_else();
				}
			}

			setState(190);
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
		enterRule(_localctx, 38, RULE_condition_else);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			match(T__27);
			setState(193);
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
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			factor();
			setState(198);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__28 || _la==T__29) {
				{
				setState(196);
				_la = _input.LA(1);
				if ( !(_la==T__28 || _la==T__29) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(197);
				factor();
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
	public static class FactorContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode ID() { return getToken(baby_duck_grammarParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_factor);
		int _la;
		try {
			setState(211);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__17:
				enterOuterAlt(_localctx, 1);
				{
				setState(200);
				match(T__17);
				setState(201);
				expression();
				setState(202);
				match(T__18);
				}
				break;
			case T__14:
			case T__15:
			case ID:
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(205);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__14 || _la==T__15) {
					{
					setState(204);
					_la = _input.LA(1);
					if ( !(_la==T__14 || _la==T__15) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
				}

				setState(209);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(207);
					match(ID);
					}
					break;
				case INT:
				case FLOAT:
					{
					setState(208);
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
		enterRule(_localctx, 44, RULE_f_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			match(ID);
			setState(214);
			match(T__17);
			setState(216);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 23622680576L) != 0)) {
				{
				setState(215);
				f_call_helper();
				}
			}

			setState(218);
			match(T__18);
			setState(219);
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
		enterRule(_localctx, 46, RULE_f_call_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			expression();
			setState(226);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__19) {
				{
				{
				setState(222);
				match(T__19);
				setState(223);
				expression();
				}
				}
				setState(228);
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
		"\u0004\u0001#\u00e6\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0003\u00005\b\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0005\u0001:\b\u0001\n\u0001\f\u0001=\t\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0005\u0002"+
		"E\b\u0002\n\u0002\f\u0002H\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003Q\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"^\b\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0005\tg\b\t\n\t\f\tj\t\t\u0001\n\u0001\n\u0001\n\u0003\no\b\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0003\u000bv\b\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0003\u000b{\b\u000b\u0005\u000b}\b\u000b"+
		"\n\u000b\f\u000b\u0080\t\u000b\u0001\f\u0001\f\u0001\f\u0005\f\u0085\b"+
		"\f\n\f\f\f\u0088\t\f\u0003\f\u008a\b\f\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u0097\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0004\u000f\u009f\b\u000f\u000b\u000f"+
		"\f\u000f\u00a0\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u00a6\b"+
		"\u0010\n\u0010\f\u0010\u00a9\t\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00bd\b\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u00c7\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0003\u0015\u00ce\b\u0015\u0001\u0015\u0001\u0015"+
		"\u0003\u0015\u00d2\b\u0015\u0003\u0015\u00d4\b\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0003\u0016\u00d9\b\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u00e1\b\u0017\n"+
		"\u0017\f\u0017\u00e4\t\u0017\u0001\u0017\u0000\u0000\u0018\u0000\u0002"+
		"\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e"+
		" \"$&(*,.\u0000\u0005\u0001\u0000\u0007\n\u0001\u0000\f\u000e\u0002\u0000"+
		"  \"\"\u0001\u0000\u000f\u0010\u0001\u0000\u001d\u001e\u00e6\u00000\u0001"+
		"\u0000\u0000\u0000\u0002;\u0001\u0000\u0000\u0000\u0004B\u0001\u0000\u0000"+
		"\u0000\u0006P\u0001\u0000\u0000\u0000\bR\u0001\u0000\u0000\u0000\nT\u0001"+
		"\u0000\u0000\u0000\fY\u0001\u0000\u0000\u0000\u000e_\u0001\u0000\u0000"+
		"\u0000\u0010a\u0001\u0000\u0000\u0000\u0012c\u0001\u0000\u0000\u0000\u0014"+
		"k\u0001\u0000\u0000\u0000\u0016u\u0001\u0000\u0000\u0000\u0018\u0089\u0001"+
		"\u0000\u0000\u0000\u001a\u008b\u0001\u0000\u0000\u0000\u001c\u008f\u0001"+
		"\u0000\u0000\u0000\u001e\u009c\u0001\u0000\u0000\u0000 \u00a2\u0001\u0000"+
		"\u0000\u0000\"\u00ae\u0001\u0000\u0000\u0000$\u00b6\u0001\u0000\u0000"+
		"\u0000&\u00c0\u0001\u0000\u0000\u0000(\u00c3\u0001\u0000\u0000\u0000*"+
		"\u00d3\u0001\u0000\u0000\u0000,\u00d5\u0001\u0000\u0000\u0000.\u00dd\u0001"+
		"\u0000\u0000\u000001\u0005\u0001\u0000\u000012\u0005\u001f\u0000\u0000"+
		"24\u0005\u0002\u0000\u000035\u0003\u001e\u000f\u000043\u0001\u0000\u0000"+
		"\u000045\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u000067\u0003\u0002"+
		"\u0001\u00007\u0001\u0001\u0000\u0000\u00008:\u0003\u001c\u000e\u0000"+
		"98\u0001\u0000\u0000\u0000:=\u0001\u0000\u0000\u0000;9\u0001\u0000\u0000"+
		"\u0000;<\u0001\u0000\u0000\u0000<>\u0001\u0000\u0000\u0000=;\u0001\u0000"+
		"\u0000\u0000>?\u0005\u0003\u0000\u0000?@\u0003\u0004\u0002\u0000@A\u0005"+
		"\u0004\u0000\u0000A\u0003\u0001\u0000\u0000\u0000BF\u0005\u0005\u0000"+
		"\u0000CE\u0003\u0006\u0003\u0000DC\u0001\u0000\u0000\u0000EH\u0001\u0000"+
		"\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GI\u0001"+
		"\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000IJ\u0005\u0006\u0000\u0000"+
		"J\u0005\u0001\u0000\u0000\u0000KQ\u0003\n\u0005\u0000LQ\u0003$\u0012\u0000"+
		"MQ\u0003\"\u0011\u0000NQ\u0003,\u0016\u0000OQ\u0003\u0014\n\u0000PK\u0001"+
		"\u0000\u0000\u0000PL\u0001\u0000\u0000\u0000PM\u0001\u0000\u0000\u0000"+
		"PN\u0001\u0000\u0000\u0000PO\u0001\u0000\u0000\u0000Q\u0007\u0001\u0000"+
		"\u0000\u0000RS\u0007\u0000\u0000\u0000S\t\u0001\u0000\u0000\u0000TU\u0005"+
		"\u001f\u0000\u0000UV\u0005\u000b\u0000\u0000VW\u0003\f\u0006\u0000WX\u0005"+
		"\u0002\u0000\u0000X\u000b\u0001\u0000\u0000\u0000Y]\u0003\u0012\t\u0000"+
		"Z[\u0003\u000e\u0007\u0000[\\\u0003\u0012\t\u0000\\^\u0001\u0000\u0000"+
		"\u0000]Z\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\r\u0001\u0000"+
		"\u0000\u0000_`\u0007\u0001\u0000\u0000`\u000f\u0001\u0000\u0000\u0000"+
		"ab\u0007\u0002\u0000\u0000b\u0011\u0001\u0000\u0000\u0000ch\u0003(\u0014"+
		"\u0000de\u0007\u0003\u0000\u0000eg\u0003(\u0014\u0000fd\u0001\u0000\u0000"+
		"\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001\u0000"+
		"\u0000\u0000i\u0013\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000"+
		"kl\u0005\u0011\u0000\u0000ln\u0005\u0012\u0000\u0000mo\u0003\u0016\u000b"+
		"\u0000nm\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000op\u0001\u0000"+
		"\u0000\u0000pq\u0005\u0013\u0000\u0000qr\u0005\u0002\u0000\u0000r\u0015"+
		"\u0001\u0000\u0000\u0000sv\u0003\f\u0006\u0000tv\u0005#\u0000\u0000us"+
		"\u0001\u0000\u0000\u0000ut\u0001\u0000\u0000\u0000v~\u0001\u0000\u0000"+
		"\u0000wz\u0005\u0014\u0000\u0000x{\u0003\f\u0006\u0000y{\u0005#\u0000"+
		"\u0000zx\u0001\u0000\u0000\u0000zy\u0001\u0000\u0000\u0000{}\u0001\u0000"+
		"\u0000\u0000|w\u0001\u0000\u0000\u0000}\u0080\u0001\u0000\u0000\u0000"+
		"~|\u0001\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0017"+
		"\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0081\u0086\u0003"+
		"\u001a\r\u0000\u0082\u0083\u0005\u0014\u0000\u0000\u0083\u0085\u0003\u001a"+
		"\r\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0088\u0001\u0000\u0000"+
		"\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000"+
		"\u0000\u0087\u008a\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000"+
		"\u0000\u0089\u0081\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000\u0000"+
		"\u0000\u008a\u0019\u0001\u0000\u0000\u0000\u008b\u008c\u0005\u001f\u0000"+
		"\u0000\u008c\u008d\u0005\u0015\u0000\u0000\u008d\u008e\u0003\b\u0004\u0000"+
		"\u008e\u001b\u0001\u0000\u0000\u0000\u008f\u0090\u0003\b\u0004\u0000\u0090"+
		"\u0091\u0005\u001f\u0000\u0000\u0091\u0092\u0005\u0012\u0000\u0000\u0092"+
		"\u0093\u0003\u0018\f\u0000\u0093\u0094\u0005\u0013\u0000\u0000\u0094\u0096"+
		"\u0005\u0016\u0000\u0000\u0095\u0097\u0003\u001e\u000f\u0000\u0096\u0095"+
		"\u0001\u0000\u0000\u0000\u0096\u0097\u0001\u0000\u0000\u0000\u0097\u0098"+
		"\u0001\u0000\u0000\u0000\u0098\u0099\u0003\u0004\u0002\u0000\u0099\u009a"+
		"\u0005\u0017\u0000\u0000\u009a\u009b\u0005\u0002\u0000\u0000\u009b\u001d"+
		"\u0001\u0000\u0000\u0000\u009c\u009e\u0005\u0018\u0000\u0000\u009d\u009f"+
		"\u0003 \u0010\u0000\u009e\u009d\u0001\u0000\u0000\u0000\u009f\u00a0\u0001"+
		"\u0000\u0000\u0000\u00a0\u009e\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001"+
		"\u0000\u0000\u0000\u00a1\u001f\u0001\u0000\u0000\u0000\u00a2\u00a7\u0005"+
		"\u001f\u0000\u0000\u00a3\u00a4\u0005\u0014\u0000\u0000\u00a4\u00a6\u0005"+
		"\u001f\u0000\u0000\u00a5\u00a3\u0001\u0000\u0000\u0000\u00a6\u00a9\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001"+
		"\u0000\u0000\u0000\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001"+
		"\u0000\u0000\u0000\u00aa\u00ab\u0005\u0015\u0000\u0000\u00ab\u00ac\u0003"+
		"\b\u0004\u0000\u00ac\u00ad\u0005\u0002\u0000\u0000\u00ad!\u0001\u0000"+
		"\u0000\u0000\u00ae\u00af\u0005\u0019\u0000\u0000\u00af\u00b0\u0003\u0004"+
		"\u0002\u0000\u00b0\u00b1\u0005\u001a\u0000\u0000\u00b1\u00b2\u0005\u0012"+
		"\u0000\u0000\u00b2\u00b3\u0003\f\u0006\u0000\u00b3\u00b4\u0005\u0013\u0000"+
		"\u0000\u00b4\u00b5\u0005\u0002\u0000\u0000\u00b5#\u0001\u0000\u0000\u0000"+
		"\u00b6\u00b7\u0005\u001b\u0000\u0000\u00b7\u00b8\u0005\u0012\u0000\u0000"+
		"\u00b8\u00b9\u0003\f\u0006\u0000\u00b9\u00ba\u0005\u0013\u0000\u0000\u00ba"+
		"\u00bc\u0003\u0004\u0002\u0000\u00bb\u00bd\u0003&\u0013\u0000\u00bc\u00bb"+
		"\u0001\u0000\u0000\u0000\u00bc\u00bd\u0001\u0000\u0000\u0000\u00bd\u00be"+
		"\u0001\u0000\u0000\u0000\u00be\u00bf\u0005\u0002\u0000\u0000\u00bf%\u0001"+
		"\u0000\u0000\u0000\u00c0\u00c1\u0005\u001c\u0000\u0000\u00c1\u00c2\u0003"+
		"\u0004\u0002\u0000\u00c2\'\u0001\u0000\u0000\u0000\u00c3\u00c6\u0003*"+
		"\u0015\u0000\u00c4\u00c5\u0007\u0004\u0000\u0000\u00c5\u00c7\u0003*\u0015"+
		"\u0000\u00c6\u00c4\u0001\u0000\u0000\u0000\u00c6\u00c7\u0001\u0000\u0000"+
		"\u0000\u00c7)\u0001\u0000\u0000\u0000\u00c8\u00c9\u0005\u0012\u0000\u0000"+
		"\u00c9\u00ca\u0003\f\u0006\u0000\u00ca\u00cb\u0005\u0013\u0000\u0000\u00cb"+
		"\u00d4\u0001\u0000\u0000\u0000\u00cc\u00ce\u0007\u0003\u0000\u0000\u00cd"+
		"\u00cc\u0001\u0000\u0000\u0000\u00cd\u00ce\u0001\u0000\u0000\u0000\u00ce"+
		"\u00d1\u0001\u0000\u0000\u0000\u00cf\u00d2\u0005\u001f\u0000\u0000\u00d0"+
		"\u00d2\u0003\u0010\b\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000\u00d1\u00d0"+
		"\u0001\u0000\u0000\u0000\u00d2\u00d4\u0001\u0000\u0000\u0000\u00d3\u00c8"+
		"\u0001\u0000\u0000\u0000\u00d3\u00cd\u0001\u0000\u0000\u0000\u00d4+\u0001"+
		"\u0000\u0000\u0000\u00d5\u00d6\u0005\u001f\u0000\u0000\u00d6\u00d8\u0005"+
		"\u0012\u0000\u0000\u00d7\u00d9\u0003.\u0017\u0000\u00d8\u00d7\u0001\u0000"+
		"\u0000\u0000\u00d8\u00d9\u0001\u0000\u0000\u0000\u00d9\u00da\u0001\u0000"+
		"\u0000\u0000\u00da\u00db\u0005\u0013\u0000\u0000\u00db\u00dc\u0005\u0002"+
		"\u0000\u0000\u00dc-\u0001\u0000\u0000\u0000\u00dd\u00e2\u0003\f\u0006"+
		"\u0000\u00de\u00df\u0005\u0014\u0000\u0000\u00df\u00e1\u0003\f\u0006\u0000"+
		"\u00e0\u00de\u0001\u0000\u0000\u0000\u00e1\u00e4\u0001\u0000\u0000\u0000"+
		"\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e2\u00e3\u0001\u0000\u0000\u0000"+
		"\u00e3/\u0001\u0000\u0000\u0000\u00e4\u00e2\u0001\u0000\u0000\u0000\u0016"+
		"4;FP]hnuz~\u0086\u0089\u0096\u00a0\u00a7\u00bc\u00c6\u00cd\u00d1\u00d3"+
		"\u00d8\u00e2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}