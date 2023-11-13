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
		RULE_cte = 8, RULE_print = 9, RULE_print_helper = 10, RULE_f_param_list = 11, 
		RULE_f_param_list_helper = 12, RULE_funcs = 13, RULE_vars = 14, RULE_vars_declarations = 15, 
		RULE_cycle = 16, RULE_while_keyword = 17, RULE_condition = 18, RULE_condition_else = 19, 
		RULE_operator = 20, RULE_exp = 21, RULE_term = 22, RULE_term_operator = 23, 
		RULE_factor = 24, RULE_factor_operator = 25, RULE_parenthesized_expression = 26, 
		RULE_f_call = 27, RULE_f_call_helper = 28;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "program_post_var", "body", "statement", "type", "assign", 
			"expression", "rel_op", "cte", "print", "print_helper", "f_param_list", 
			"f_param_list_helper", "funcs", "vars", "vars_declarations", "cycle", 
			"while_keyword", "condition", "condition_else", "operator", "exp", "term", 
			"term_operator", "factor", "factor_operator", "parenthesized_expression", 
			"f_call", "f_call_helper"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'program'", "';'", "'main'", "'end'", "'{'", "'}'", "'int'", "'float'", 
			"'bool'", "'void'", "'='", "'<'", "'>'", "'!='", "'print'", "'('", "')'", 
			"','", "':'", "'['", "']'", "'var'", "'do'", "'while'", "'if'", "'else'", 
			"'+'", "'-'", "'*'", "'/'"
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
			setState(58);
			match(T__0);
			setState(59);
			match(ID);
			setState(60);
			match(T__1);
			setState(62);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__21) {
				{
				setState(61);
				vars();
				}
			}

			setState(64);
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
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1920L) != 0)) {
				{
				{
				setState(66);
				funcs();
				}
				}
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(72);
			match(T__2);
			setState(73);
			body();
			setState(74);
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
			setState(76);
			match(T__4);
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2197848064L) != 0)) {
				{
				{
				setState(77);
				statement();
				}
				}
				setState(82);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(83);
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
			setState(90);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(85);
				assign();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(86);
				condition();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(87);
				cycle();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(88);
				f_call();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(89);
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
			setState(92);
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
			setState(94);
			match(ID);
			setState(95);
			match(T__10);
			setState(96);
			expression();
			setState(97);
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
		enterRule(_localctx, 12, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			exp();
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 28672L) != 0)) {
				{
				setState(100);
				rel_op();
				setState(101);
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
		enterRule(_localctx, 14, RULE_rel_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
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
			setState(107);
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
		enterRule(_localctx, 18, RULE_print);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(109);
			match(T__14);
			setState(110);
			match(T__15);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 58384777216L) != 0)) {
				{
				setState(111);
				print_helper();
				}
			}

			setState(114);
			match(T__16);
			setState(115);
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
		enterRule(_localctx, 20, RULE_print_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
			case T__26:
			case T__27:
			case ID:
			case INT:
			case FLOAT:
				{
				setState(117);
				expression();
				}
				break;
			case STRING:
				{
				setState(118);
				match(STRING);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(128);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17) {
				{
				{
				setState(121);
				match(T__17);
				setState(124);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__15:
				case T__26:
				case T__27:
				case ID:
				case INT:
				case FLOAT:
					{
					setState(122);
					expression();
					}
					break;
				case STRING:
					{
					setState(123);
					match(STRING);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(130);
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
		enterRule(_localctx, 22, RULE_f_param_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(131);
				f_param_list_helper();
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__17) {
					{
					{
					setState(132);
					match(T__17);
					setState(133);
					f_param_list_helper();
					}
					}
					setState(138);
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
		enterRule(_localctx, 24, RULE_f_param_list_helper);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(141);
			match(ID);
			setState(142);
			match(T__18);
			setState(143);
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
		enterRule(_localctx, 26, RULE_funcs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			type();
			setState(146);
			match(ID);
			setState(147);
			match(T__15);
			setState(148);
			f_param_list();
			setState(149);
			match(T__16);
			setState(150);
			match(T__19);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__21) {
				{
				setState(151);
				vars();
				}
			}

			setState(154);
			body();
			setState(155);
			match(T__20);
			setState(156);
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
		enterRule(_localctx, 28, RULE_vars);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(T__21);
			setState(160); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(159);
				vars_declarations();
				}
				}
				setState(162); 
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
		enterRule(_localctx, 30, RULE_vars_declarations);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(164);
			match(ID);
			setState(169);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17) {
				{
				{
				setState(165);
				match(T__17);
				setState(166);
				match(ID);
				}
				}
				setState(171);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(172);
			match(T__18);
			setState(173);
			type();
			setState(174);
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
		public While_keywordContext while_keyword() {
			return getRuleContext(While_keywordContext.class,0);
		}
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
		enterRule(_localctx, 32, RULE_cycle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			while_keyword();
			setState(177);
			body();
			setState(178);
			match(T__22);
			setState(179);
			match(T__15);
			setState(180);
			expression();
			setState(181);
			match(T__16);
			setState(182);
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
	public static class While_keywordContext extends ParserRuleContext {
		public While_keywordContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_keyword; }
	}

	public final While_keywordContext while_keyword() throws RecognitionException {
		While_keywordContext _localctx = new While_keywordContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_while_keyword);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			match(T__23);
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
			setState(186);
			match(T__24);
			setState(187);
			match(T__15);
			setState(188);
			expression();
			setState(189);
			match(T__16);
			setState(190);
			body();
			setState(192);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25) {
				{
				setState(191);
				condition_else();
				}
			}

			setState(194);
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
			setState(196);
			match(T__25);
			setState(197);
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
		enterRule(_localctx, 40, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(199);
			_la = _input.LA(1);
			if ( !(_la==T__26 || _la==T__27) ) {
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
		enterRule(_localctx, 42, RULE_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(201);
			term();
			setState(205);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__26 || _la==T__27) {
				{
				setState(202);
				operator();
				setState(203);
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
		enterRule(_localctx, 44, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			factor();
			setState(211);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__28 || _la==T__29) {
				{
				setState(208);
				term_operator();
				setState(209);
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
		enterRule(_localctx, 46, RULE_term_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(213);
			_la = _input.LA(1);
			if ( !(_la==T__28 || _la==T__29) ) {
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
		enterRule(_localctx, 48, RULE_factor);
		int _la;
		try {
			setState(223);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				enterOuterAlt(_localctx, 1);
				{
				setState(215);
				parenthesized_expression();
				}
				break;
			case T__26:
			case T__27:
			case ID:
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(217);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__26 || _la==T__27) {
					{
					setState(216);
					factor_operator();
					}
				}

				setState(221);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case ID:
					{
					setState(219);
					match(ID);
					}
					break;
				case INT:
				case FLOAT:
					{
					setState(220);
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
		enterRule(_localctx, 50, RULE_factor_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			_la = _input.LA(1);
			if ( !(_la==T__26 || _la==T__27) ) {
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
		enterRule(_localctx, 52, RULE_parenthesized_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(227);
			match(T__15);
			setState(228);
			expression();
			setState(229);
			match(T__16);
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
		enterRule(_localctx, 54, RULE_f_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(231);
			match(ID);
			setState(232);
			match(T__15);
			setState(234);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 24025038848L) != 0)) {
				{
				setState(233);
				f_call_helper();
				}
			}

			setState(236);
			match(T__16);
			setState(237);
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
		enterRule(_localctx, 56, RULE_f_call_helper);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(239);
			expression();
			setState(244);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__17) {
				{
				{
				setState(240);
				match(T__17);
				setState(241);
				expression();
				}
				}
				setState(246);
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
		"\u0004\u0001#\u00f8\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0003\u0000?\b\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0005\u0001"+
		"D\b\u0001\n\u0001\f\u0001G\t\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0005\u0002O\b\u0002\n\u0002\f\u0002"+
		"R\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0003\u0003[\b\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006h\b\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0003\tq\b\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0003\nx\b\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n}\b\n\u0005\n\u007f\b\n\n\n\f\n\u0082\t\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0005\u000b\u0087\b\u000b\n\u000b\f\u000b\u008a\t\u000b"+
		"\u0003\u000b\u008c\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0099\b\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0004\u000e\u00a1\b\u000e\u000b"+
		"\u000e\f\u000e\u00a2\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00a8"+
		"\b\u000f\n\u000f\f\u000f\u00ab\t\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012"+
		"\u00c1\b\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0003\u0015\u00ce\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0003\u0016\u00d4\b\u0016\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018"+
		"\u0003\u0018\u00da\b\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u00de\b"+
		"\u0018\u0003\u0018\u00e0\b\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0003"+
		"\u001b\u00eb\b\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0005\u001c\u00f3\b\u001c\n\u001c\f\u001c\u00f6\t\u001c"+
		"\u0001\u001c\u0000\u0000\u001d\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010"+
		"\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468\u0000\u0005\u0001"+
		"\u0000\u0007\n\u0001\u0000\f\u000e\u0002\u0000  \"\"\u0001\u0000\u001b"+
		"\u001c\u0001\u0000\u001d\u001e\u00f3\u0000:\u0001\u0000\u0000\u0000\u0002"+
		"E\u0001\u0000\u0000\u0000\u0004L\u0001\u0000\u0000\u0000\u0006Z\u0001"+
		"\u0000\u0000\u0000\b\\\u0001\u0000\u0000\u0000\n^\u0001\u0000\u0000\u0000"+
		"\fc\u0001\u0000\u0000\u0000\u000ei\u0001\u0000\u0000\u0000\u0010k\u0001"+
		"\u0000\u0000\u0000\u0012m\u0001\u0000\u0000\u0000\u0014w\u0001\u0000\u0000"+
		"\u0000\u0016\u008b\u0001\u0000\u0000\u0000\u0018\u008d\u0001\u0000\u0000"+
		"\u0000\u001a\u0091\u0001\u0000\u0000\u0000\u001c\u009e\u0001\u0000\u0000"+
		"\u0000\u001e\u00a4\u0001\u0000\u0000\u0000 \u00b0\u0001\u0000\u0000\u0000"+
		"\"\u00b8\u0001\u0000\u0000\u0000$\u00ba\u0001\u0000\u0000\u0000&\u00c4"+
		"\u0001\u0000\u0000\u0000(\u00c7\u0001\u0000\u0000\u0000*\u00c9\u0001\u0000"+
		"\u0000\u0000,\u00cf\u0001\u0000\u0000\u0000.\u00d5\u0001\u0000\u0000\u0000"+
		"0\u00df\u0001\u0000\u0000\u00002\u00e1\u0001\u0000\u0000\u00004\u00e3"+
		"\u0001\u0000\u0000\u00006\u00e7\u0001\u0000\u0000\u00008\u00ef\u0001\u0000"+
		"\u0000\u0000:;\u0005\u0001\u0000\u0000;<\u0005\u001f\u0000\u0000<>\u0005"+
		"\u0002\u0000\u0000=?\u0003\u001c\u000e\u0000>=\u0001\u0000\u0000\u0000"+
		">?\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000\u0000@A\u0003\u0002\u0001"+
		"\u0000A\u0001\u0001\u0000\u0000\u0000BD\u0003\u001a\r\u0000CB\u0001\u0000"+
		"\u0000\u0000DG\u0001\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001"+
		"\u0000\u0000\u0000FH\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000"+
		"HI\u0005\u0003\u0000\u0000IJ\u0003\u0004\u0002\u0000JK\u0005\u0004\u0000"+
		"\u0000K\u0003\u0001\u0000\u0000\u0000LP\u0005\u0005\u0000\u0000MO\u0003"+
		"\u0006\u0003\u0000NM\u0001\u0000\u0000\u0000OR\u0001\u0000\u0000\u0000"+
		"PN\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QS\u0001\u0000\u0000"+
		"\u0000RP\u0001\u0000\u0000\u0000ST\u0005\u0006\u0000\u0000T\u0005\u0001"+
		"\u0000\u0000\u0000U[\u0003\n\u0005\u0000V[\u0003$\u0012\u0000W[\u0003"+
		" \u0010\u0000X[\u00036\u001b\u0000Y[\u0003\u0012\t\u0000ZU\u0001\u0000"+
		"\u0000\u0000ZV\u0001\u0000\u0000\u0000ZW\u0001\u0000\u0000\u0000ZX\u0001"+
		"\u0000\u0000\u0000ZY\u0001\u0000\u0000\u0000[\u0007\u0001\u0000\u0000"+
		"\u0000\\]\u0007\u0000\u0000\u0000]\t\u0001\u0000\u0000\u0000^_\u0005\u001f"+
		"\u0000\u0000_`\u0005\u000b\u0000\u0000`a\u0003\f\u0006\u0000ab\u0005\u0002"+
		"\u0000\u0000b\u000b\u0001\u0000\u0000\u0000cg\u0003*\u0015\u0000de\u0003"+
		"\u000e\u0007\u0000ef\u0003\f\u0006\u0000fh\u0001\u0000\u0000\u0000gd\u0001"+
		"\u0000\u0000\u0000gh\u0001\u0000\u0000\u0000h\r\u0001\u0000\u0000\u0000"+
		"ij\u0007\u0001\u0000\u0000j\u000f\u0001\u0000\u0000\u0000kl\u0007\u0002"+
		"\u0000\u0000l\u0011\u0001\u0000\u0000\u0000mn\u0005\u000f\u0000\u0000"+
		"np\u0005\u0010\u0000\u0000oq\u0003\u0014\n\u0000po\u0001\u0000\u0000\u0000"+
		"pq\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000rs\u0005\u0011\u0000"+
		"\u0000st\u0005\u0002\u0000\u0000t\u0013\u0001\u0000\u0000\u0000ux\u0003"+
		"\f\u0006\u0000vx\u0005#\u0000\u0000wu\u0001\u0000\u0000\u0000wv\u0001"+
		"\u0000\u0000\u0000x\u0080\u0001\u0000\u0000\u0000y|\u0005\u0012\u0000"+
		"\u0000z}\u0003\f\u0006\u0000{}\u0005#\u0000\u0000|z\u0001\u0000\u0000"+
		"\u0000|{\u0001\u0000\u0000\u0000}\u007f\u0001\u0000\u0000\u0000~y\u0001"+
		"\u0000\u0000\u0000\u007f\u0082\u0001\u0000\u0000\u0000\u0080~\u0001\u0000"+
		"\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0015\u0001\u0000"+
		"\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000\u0083\u0088\u0003\u0018"+
		"\f\u0000\u0084\u0085\u0005\u0012\u0000\u0000\u0085\u0087\u0003\u0018\f"+
		"\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0087\u008a\u0001\u0000\u0000"+
		"\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000"+
		"\u0000\u0089\u008c\u0001\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000"+
		"\u0000\u008b\u0083\u0001\u0000\u0000\u0000\u008b\u008c\u0001\u0000\u0000"+
		"\u0000\u008c\u0017\u0001\u0000\u0000\u0000\u008d\u008e\u0005\u001f\u0000"+
		"\u0000\u008e\u008f\u0005\u0013\u0000\u0000\u008f\u0090\u0003\b\u0004\u0000"+
		"\u0090\u0019\u0001\u0000\u0000\u0000\u0091\u0092\u0003\b\u0004\u0000\u0092"+
		"\u0093\u0005\u001f\u0000\u0000\u0093\u0094\u0005\u0010\u0000\u0000\u0094"+
		"\u0095\u0003\u0016\u000b\u0000\u0095\u0096\u0005\u0011\u0000\u0000\u0096"+
		"\u0098\u0005\u0014\u0000\u0000\u0097\u0099\u0003\u001c\u000e\u0000\u0098"+
		"\u0097\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099"+
		"\u009a\u0001\u0000\u0000\u0000\u009a\u009b\u0003\u0004\u0002\u0000\u009b"+
		"\u009c\u0005\u0015\u0000\u0000\u009c\u009d\u0005\u0002\u0000\u0000\u009d"+
		"\u001b\u0001\u0000\u0000\u0000\u009e\u00a0\u0005\u0016\u0000\u0000\u009f"+
		"\u00a1\u0003\u001e\u000f\u0000\u00a0\u009f\u0001\u0000\u0000\u0000\u00a1"+
		"\u00a2\u0001\u0000\u0000\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a2"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a3\u001d\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a9\u0005\u001f\u0000\u0000\u00a5\u00a6\u0005\u0012\u0000\u0000\u00a6"+
		"\u00a8\u0005\u001f\u0000\u0000\u00a7\u00a5\u0001\u0000\u0000\u0000\u00a8"+
		"\u00ab\u0001\u0000\u0000\u0000\u00a9\u00a7\u0001\u0000\u0000\u0000\u00a9"+
		"\u00aa\u0001\u0000\u0000\u0000\u00aa\u00ac\u0001\u0000\u0000\u0000\u00ab"+
		"\u00a9\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005\u0013\u0000\u0000\u00ad"+
		"\u00ae\u0003\b\u0004\u0000\u00ae\u00af\u0005\u0002\u0000\u0000\u00af\u001f"+
		"\u0001\u0000\u0000\u0000\u00b0\u00b1\u0003\"\u0011\u0000\u00b1\u00b2\u0003"+
		"\u0004\u0002\u0000\u00b2\u00b3\u0005\u0017\u0000\u0000\u00b3\u00b4\u0005"+
		"\u0010\u0000\u0000\u00b4\u00b5\u0003\f\u0006\u0000\u00b5\u00b6\u0005\u0011"+
		"\u0000\u0000\u00b6\u00b7\u0005\u0002\u0000\u0000\u00b7!\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b9\u0005\u0018\u0000\u0000\u00b9#\u0001\u0000\u0000\u0000"+
		"\u00ba\u00bb\u0005\u0019\u0000\u0000\u00bb\u00bc\u0005\u0010\u0000\u0000"+
		"\u00bc\u00bd\u0003\f\u0006\u0000\u00bd\u00be\u0005\u0011\u0000\u0000\u00be"+
		"\u00c0\u0003\u0004\u0002\u0000\u00bf\u00c1\u0003&\u0013\u0000\u00c0\u00bf"+
		"\u0001\u0000\u0000\u0000\u00c0\u00c1\u0001\u0000\u0000\u0000\u00c1\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c2\u00c3\u0005\u0002\u0000\u0000\u00c3%\u0001"+
		"\u0000\u0000\u0000\u00c4\u00c5\u0005\u001a\u0000\u0000\u00c5\u00c6\u0003"+
		"\u0004\u0002\u0000\u00c6\'\u0001\u0000\u0000\u0000\u00c7\u00c8\u0007\u0003"+
		"\u0000\u0000\u00c8)\u0001\u0000\u0000\u0000\u00c9\u00cd\u0003,\u0016\u0000"+
		"\u00ca\u00cb\u0003(\u0014\u0000\u00cb\u00cc\u0003*\u0015\u0000\u00cc\u00ce"+
		"\u0001\u0000\u0000\u0000\u00cd\u00ca\u0001\u0000\u0000\u0000\u00cd\u00ce"+
		"\u0001\u0000\u0000\u0000\u00ce+\u0001\u0000\u0000\u0000\u00cf\u00d3\u0003"+
		"0\u0018\u0000\u00d0\u00d1\u0003.\u0017\u0000\u00d1\u00d2\u0003,\u0016"+
		"\u0000\u00d2\u00d4\u0001\u0000\u0000\u0000\u00d3\u00d0\u0001\u0000\u0000"+
		"\u0000\u00d3\u00d4\u0001\u0000\u0000\u0000\u00d4-\u0001\u0000\u0000\u0000"+
		"\u00d5\u00d6\u0007\u0004\u0000\u0000\u00d6/\u0001\u0000\u0000\u0000\u00d7"+
		"\u00e0\u00034\u001a\u0000\u00d8\u00da\u00032\u0019\u0000\u00d9\u00d8\u0001"+
		"\u0000\u0000\u0000\u00d9\u00da\u0001\u0000\u0000\u0000\u00da\u00dd\u0001"+
		"\u0000\u0000\u0000\u00db\u00de\u0005\u001f\u0000\u0000\u00dc\u00de\u0003"+
		"\u0010\b\u0000\u00dd\u00db\u0001\u0000\u0000\u0000\u00dd\u00dc\u0001\u0000"+
		"\u0000\u0000\u00de\u00e0\u0001\u0000\u0000\u0000\u00df\u00d7\u0001\u0000"+
		"\u0000\u0000\u00df\u00d9\u0001\u0000\u0000\u0000\u00e01\u0001\u0000\u0000"+
		"\u0000\u00e1\u00e2\u0007\u0003\u0000\u0000\u00e23\u0001\u0000\u0000\u0000"+
		"\u00e3\u00e4\u0005\u0010\u0000\u0000\u00e4\u00e5\u0003\f\u0006\u0000\u00e5"+
		"\u00e6\u0005\u0011\u0000\u0000\u00e65\u0001\u0000\u0000\u0000\u00e7\u00e8"+
		"\u0005\u001f\u0000\u0000\u00e8\u00ea\u0005\u0010\u0000\u0000\u00e9\u00eb"+
		"\u00038\u001c\u0000\u00ea\u00e9\u0001\u0000\u0000\u0000\u00ea\u00eb\u0001"+
		"\u0000\u0000\u0000\u00eb\u00ec\u0001\u0000\u0000\u0000\u00ec\u00ed\u0005"+
		"\u0011\u0000\u0000\u00ed\u00ee\u0005\u0002\u0000\u0000\u00ee7\u0001\u0000"+
		"\u0000\u0000\u00ef\u00f4\u0003\f\u0006\u0000\u00f0\u00f1\u0005\u0012\u0000"+
		"\u0000\u00f1\u00f3\u0003\f\u0006\u0000\u00f2\u00f0\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f6\u0001\u0000\u0000\u0000\u00f4\u00f2\u0001\u0000\u0000\u0000"+
		"\u00f4\u00f5\u0001\u0000\u0000\u0000\u00f59\u0001\u0000\u0000\u0000\u00f6"+
		"\u00f4\u0001\u0000\u0000\u0000\u0016>EPZgpw|\u0080\u0088\u008b\u0098\u00a2"+
		"\u00a9\u00c0\u00cd\u00d3\u00d9\u00dd\u00df\u00ea\u00f4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}