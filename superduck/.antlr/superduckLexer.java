// Generated from c:/Users/fztmo/code/babyDuck/superduck/superduck.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class superduckLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, NUMBER=16, 
		STRING=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "NUMBER", "STRING", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'!='", "'=='", "'>'", "'>='", "'<'", "'<='", "'-'", "'+'", "'/'", 
			"'*'", "'!'", "'true'", "'false'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "NUMBER", "STRING", "WS"
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


	public superduckLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "superduck.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0012k\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f"+
		"\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e"+
		"\u0001\u000f\u0004\u000fP\b\u000f\u000b\u000f\f\u000fQ\u0001\u000f\u0001"+
		"\u000f\u0004\u000fV\b\u000f\u000b\u000f\f\u000fW\u0003\u000fZ\b\u000f"+
		"\u0001\u0010\u0001\u0010\u0005\u0010^\b\u0010\n\u0010\f\u0010a\t\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0004\u0011f\b\u0011\u000b\u0011"+
		"\f\u0011g\u0001\u0011\u0001\u0011\u0000\u0000\u0012\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010"+
		"!\u0011#\u0012\u0001\u0000\u0003\u0001\u000009\u0001\u0000\"\"\u0003\u0000"+
		"\t\n\r\r  o\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0001%"+
		"\u0001\u0000\u0000\u0000\u0003(\u0001\u0000\u0000\u0000\u0005+\u0001\u0000"+
		"\u0000\u0000\u0007-\u0001\u0000\u0000\u0000\t0\u0001\u0000\u0000\u0000"+
		"\u000b2\u0001\u0000\u0000\u0000\r5\u0001\u0000\u0000\u0000\u000f7\u0001"+
		"\u0000\u0000\u0000\u00119\u0001\u0000\u0000\u0000\u0013;\u0001\u0000\u0000"+
		"\u0000\u0015=\u0001\u0000\u0000\u0000\u0017?\u0001\u0000\u0000\u0000\u0019"+
		"D\u0001\u0000\u0000\u0000\u001bJ\u0001\u0000\u0000\u0000\u001dL\u0001"+
		"\u0000\u0000\u0000\u001fO\u0001\u0000\u0000\u0000![\u0001\u0000\u0000"+
		"\u0000#e\u0001\u0000\u0000\u0000%&\u0005!\u0000\u0000&\'\u0005=\u0000"+
		"\u0000\'\u0002\u0001\u0000\u0000\u0000()\u0005=\u0000\u0000)*\u0005=\u0000"+
		"\u0000*\u0004\u0001\u0000\u0000\u0000+,\u0005>\u0000\u0000,\u0006\u0001"+
		"\u0000\u0000\u0000-.\u0005>\u0000\u0000./\u0005=\u0000\u0000/\b\u0001"+
		"\u0000\u0000\u000001\u0005<\u0000\u00001\n\u0001\u0000\u0000\u000023\u0005"+
		"<\u0000\u000034\u0005=\u0000\u00004\f\u0001\u0000\u0000\u000056\u0005"+
		"-\u0000\u00006\u000e\u0001\u0000\u0000\u000078\u0005+\u0000\u00008\u0010"+
		"\u0001\u0000\u0000\u00009:\u0005/\u0000\u0000:\u0012\u0001\u0000\u0000"+
		"\u0000;<\u0005*\u0000\u0000<\u0014\u0001\u0000\u0000\u0000=>\u0005!\u0000"+
		"\u0000>\u0016\u0001\u0000\u0000\u0000?@\u0005t\u0000\u0000@A\u0005r\u0000"+
		"\u0000AB\u0005u\u0000\u0000BC\u0005e\u0000\u0000C\u0018\u0001\u0000\u0000"+
		"\u0000DE\u0005f\u0000\u0000EF\u0005a\u0000\u0000FG\u0005l\u0000\u0000"+
		"GH\u0005s\u0000\u0000HI\u0005e\u0000\u0000I\u001a\u0001\u0000\u0000\u0000"+
		"JK\u0005(\u0000\u0000K\u001c\u0001\u0000\u0000\u0000LM\u0005)\u0000\u0000"+
		"M\u001e\u0001\u0000\u0000\u0000NP\u0007\u0000\u0000\u0000ON\u0001\u0000"+
		"\u0000\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000RY\u0001\u0000\u0000\u0000SU\u0005.\u0000\u0000TV\u0007"+
		"\u0000\u0000\u0000UT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000"+
		"WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000XZ\u0001\u0000\u0000"+
		"\u0000YS\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z \u0001\u0000"+
		"\u0000\u0000[_\u0005\"\u0000\u0000\\^\b\u0001\u0000\u0000]\\\u0001\u0000"+
		"\u0000\u0000^a\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001"+
		"\u0000\u0000\u0000`b\u0001\u0000\u0000\u0000a_\u0001\u0000\u0000\u0000"+
		"bc\u0005\"\u0000\u0000c\"\u0001\u0000\u0000\u0000df\u0007\u0002\u0000"+
		"\u0000ed\u0001\u0000\u0000\u0000fg\u0001\u0000\u0000\u0000ge\u0001\u0000"+
		"\u0000\u0000gh\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0006"+
		"\u0011\u0000\u0000j$\u0001\u0000\u0000\u0000\u0006\u0000QWY_g\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}