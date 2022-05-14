// Generated from /home/juli/Documentos/LP/ex4/Practica/Expr.g by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IDENT=1, IF=2, GT=3, LT=4, EQ=5, THEN=6, END=7, WRITE=8, ASSIG=9, VAR=10, 
		NUM=11, MES=12, SUB=13, MULT=14, DIV=15, POW=16, WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IDENT", "IF", "GT", "LT", "EQ", "THEN", "END", "WRITE", "ASSIG", "VAR", 
			"NUM", "MES", "SUB", "MULT", "DIV", "POW", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'   '", "'if'", "'>'", "'<'", "'='", "'then'", "'end'", "'write'", 
			"':='", null, null, "'+'", "'-'", "'*'", "'/'", "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IDENT", "IF", "GT", "LT", "EQ", "THEN", "END", "WRITE", "ASSIG", 
			"VAR", "NUM", "MES", "SUB", "MULT", "DIV", "POW", "WS"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23a\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\7\13"+
		"G\n\13\f\13\16\13J\13\13\3\f\6\fM\n\f\r\f\16\fN\3\r\3\r\3\16\3\16\3\17"+
		"\3\17\3\20\3\20\3\21\3\21\3\22\6\22\\\n\22\r\22\16\22]\3\22\3\22\2\2\23"+
		"\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20"+
		"\37\21!\22#\23\3\2\5\3\2c|\3\2\62;\4\2\f\f\"\"\2c\2\3\3\2\2\2\2\5\3\2"+
		"\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5)\3\2"+
		"\2\2\7,\3\2\2\2\t.\3\2\2\2\13\60\3\2\2\2\r\62\3\2\2\2\17\67\3\2\2\2\21"+
		";\3\2\2\2\23A\3\2\2\2\25D\3\2\2\2\27L\3\2\2\2\31P\3\2\2\2\33R\3\2\2\2"+
		"\35T\3\2\2\2\37V\3\2\2\2!X\3\2\2\2#[\3\2\2\2%&\7\"\2\2&\'\7\"\2\2\'(\7"+
		"\"\2\2(\4\3\2\2\2)*\7k\2\2*+\7h\2\2+\6\3\2\2\2,-\7@\2\2-\b\3\2\2\2./\7"+
		">\2\2/\n\3\2\2\2\60\61\7?\2\2\61\f\3\2\2\2\62\63\7v\2\2\63\64\7j\2\2\64"+
		"\65\7g\2\2\65\66\7p\2\2\66\16\3\2\2\2\678\7g\2\289\7p\2\29:\7f\2\2:\20"+
		"\3\2\2\2;<\7y\2\2<=\7t\2\2=>\7k\2\2>?\7v\2\2?@\7g\2\2@\22\3\2\2\2AB\7"+
		"<\2\2BC\7?\2\2C\24\3\2\2\2DH\t\2\2\2EG\t\2\2\2FE\3\2\2\2GJ\3\2\2\2HF\3"+
		"\2\2\2HI\3\2\2\2I\26\3\2\2\2JH\3\2\2\2KM\t\3\2\2LK\3\2\2\2MN\3\2\2\2N"+
		"L\3\2\2\2NO\3\2\2\2O\30\3\2\2\2PQ\7-\2\2Q\32\3\2\2\2RS\7/\2\2S\34\3\2"+
		"\2\2TU\7,\2\2U\36\3\2\2\2VW\7\61\2\2W \3\2\2\2XY\7`\2\2Y\"\3\2\2\2Z\\"+
		"\t\4\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^_\3\2\2\2_`\b\22\2\2"+
		"`$\3\2\2\2\6\2HN]\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}