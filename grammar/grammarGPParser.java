// Generated from C:/Users/emili/Desktop/gene2/genetic_programming/grammar/grammarGP.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class grammarGPParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMA=1, DOT=2, LPAREN=3, RPAREN=4, LBRACE=5, RBRACE=6, PLUS=7, MINUS=8, 
		TIMES=9, DIV=10, ASSIGN=11, SEMI=12, INTEGER_LITERAL=13, FLOAT_LITERAL=14, 
		IF=15, ELSE=16, WHILE=17, READ=18, WRITE=19, AND=20, OR=21, INT=22, FLOAT=23, 
		EQ=24, NE=25, LT=26, GT=27, LE=28, GE=29, NOT=30, IDENTIFIER=31, WS=32, 
		DIGIT=33, LETTER=34;
	public static final int
		RULE_program = 0, RULE_block = 1, RULE_statement = 2, RULE_assignmentStatement = 3, 
		RULE_ifStatement = 4, RULE_loopStatement = 5, RULE_read = 6, RULE_write = 7, 
		RULE_primaryExpression = 8, RULE_unaryExpression = 9, RULE_multiplicativeExpression = 10, 
		RULE_additiveExpression = 11, RULE_relationalExpression = 12, RULE_equalityExpression = 13, 
		RULE_logicalAndExpression = 14, RULE_logicalOrExpression = 15, RULE_expression = 16, 
		RULE_castExpression = 17, RULE_relation = 18, RULE_equalityRelation = 19, 
		RULE_unaryOperator = 20, RULE_literal = 21, RULE_identifier = 22, RULE_typeSpecifier = 23;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "block", "statement", "assignmentStatement", "ifStatement", 
			"loopStatement", "read", "write", "primaryExpression", "unaryExpression", 
			"multiplicativeExpression", "additiveExpression", "relationalExpression", 
			"equalityExpression", "logicalAndExpression", "logicalOrExpression", 
			"expression", "castExpression", "relation", "equalityRelation", "unaryOperator", 
			"literal", "identifier", "typeSpecifier"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", "'.'", "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", 
			"'/'", "'='", "';'", null, null, "'if'", "'else'", "'while'", "'read'", 
			"'write'", "'&&'", "'||'", "'int'", "'float'", "'=='", "'!='", "'<'", 
			"'>'", "'<='", "'>='", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMA", "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", 
			"MINUS", "TIMES", "DIV", "ASSIGN", "SEMI", "INTEGER_LITERAL", "FLOAT_LITERAL", 
			"IF", "ELSE", "WHILE", "READ", "WRITE", "AND", "OR", "INT", "FLOAT", 
			"EQ", "NE", "LT", "GT", "LE", "GE", "NOT", "IDENTIFIER", "WS", "DIGIT", 
			"LETTER"
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
	public String getGrammarFileName() { return "grammarGP.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public grammarGPParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(grammarGPParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2148433952L) != 0)) {
				{
				{
				setState(48);
				statement();
				}
				}
				setState(53);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(54);
			match(EOF);
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
	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LBRACE() { return getToken(grammarGPParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(grammarGPParser.RBRACE, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(LBRACE);
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 2148433952L) != 0)) {
				{
				{
				setState(57);
				statement();
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
			match(RBRACE);
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
		public AssignmentStatementContext assignmentStatement() {
			return getRuleContext(AssignmentStatementContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(grammarGPParser.SEMI, 0); }
		public LoopStatementContext loopStatement() {
			return getRuleContext(LoopStatementContext.class,0);
		}
		public IfStatementContext ifStatement() {
			return getRuleContext(IfStatementContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public WriteContext write() {
			return getRuleContext(WriteContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(65);
				assignmentStatement();
				setState(66);
				match(SEMI);
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 2);
				{
				setState(68);
				loopStatement();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(69);
				ifStatement();
				}
				break;
			case READ:
				enterOuterAlt(_localctx, 4);
				{
				setState(70);
				read();
				}
				break;
			case WRITE:
				enterOuterAlt(_localctx, 5);
				{
				setState(71);
				write();
				}
				break;
			case LBRACE:
				enterOuterAlt(_localctx, 6);
				{
				setState(72);
				block();
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
	public static class AssignmentStatementContext extends ParserRuleContext {
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(grammarGPParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public AssignmentStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterAssignmentStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitAssignmentStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitAssignmentStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssignmentStatementContext assignmentStatement() throws RecognitionException {
		AssignmentStatementContext _localctx = new AssignmentStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_assignmentStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			identifier();
			setState(76);
			match(ASSIGN);
			setState(77);
			expression();
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
	public static class IfStatementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(grammarGPParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(grammarGPParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarGPParser.RPAREN, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(grammarGPParser.ELSE, 0); }
		public IfStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterIfStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitIfStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitIfStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfStatementContext ifStatement() throws RecognitionException {
		IfStatementContext _localctx = new IfStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_ifStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(IF);
			setState(80);
			match(LPAREN);
			setState(81);
			expression();
			setState(82);
			match(RPAREN);
			setState(83);
			statement();
			setState(86);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				{
				setState(84);
				match(ELSE);
				setState(85);
				statement();
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
	public static class LoopStatementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(grammarGPParser.WHILE, 0); }
		public TerminalNode LPAREN() { return getToken(grammarGPParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarGPParser.RPAREN, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public LoopStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loopStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterLoopStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitLoopStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitLoopStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LoopStatementContext loopStatement() throws RecognitionException {
		LoopStatementContext _localctx = new LoopStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_loopStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(WHILE);
			setState(89);
			match(LPAREN);
			setState(90);
			expression();
			setState(91);
			match(RPAREN);
			setState(92);
			statement();
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
	public static class ReadContext extends ParserRuleContext {
		public TerminalNode READ() { return getToken(grammarGPParser.READ, 0); }
		public TerminalNode LPAREN() { return getToken(grammarGPParser.LPAREN, 0); }
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarGPParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(grammarGPParser.SEMI, 0); }
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterRead(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitRead(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitRead(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_read);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(READ);
			setState(95);
			match(LPAREN);
			setState(96);
			identifier();
			setState(97);
			match(RPAREN);
			setState(98);
			match(SEMI);
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
	public static class WriteContext extends ParserRuleContext {
		public TerminalNode WRITE() { return getToken(grammarGPParser.WRITE, 0); }
		public TerminalNode LPAREN() { return getToken(grammarGPParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarGPParser.RPAREN, 0); }
		public TerminalNode SEMI() { return getToken(grammarGPParser.SEMI, 0); }
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterWrite(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitWrite(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitWrite(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_write);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(100);
			match(WRITE);
			setState(101);
			match(LPAREN);
			setState(102);
			expression();
			setState(103);
			match(RPAREN);
			setState(104);
			match(SEMI);
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
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public IdentifierContext identifier() {
			return getRuleContext(IdentifierContext.class,0);
		}
		public CastExpressionContext castExpression() {
			return getRuleContext(CastExpressionContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(grammarGPParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarGPParser.RPAREN, 0); }
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterPrimaryExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitPrimaryExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitPrimaryExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_primaryExpression);
		try {
			setState(113);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTEGER_LITERAL:
			case FLOAT_LITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				literal();
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(107);
				identifier();
				}
				break;
			case INT:
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(108);
				castExpression();
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 4);
				{
				setState(109);
				match(LPAREN);
				setState(110);
				expression();
				setState(111);
				match(RPAREN);
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
	public static class UnaryExpressionContext extends ParserRuleContext {
		public UnaryOperatorContext unaryOperator() {
			return getRuleContext(UnaryOperatorContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public UnaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterUnaryExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitUnaryExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitUnaryExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UnaryExpressionContext unaryExpression() throws RecognitionException {
		UnaryExpressionContext _localctx = new UnaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_unaryExpression);
		try {
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(115);
				unaryOperator();
				setState(116);
				primaryExpression();
				}
				break;
			case LPAREN:
			case INTEGER_LITERAL:
			case FLOAT_LITERAL:
			case INT:
			case FLOAT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(118);
				primaryExpression();
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
	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public List<UnaryExpressionContext> unaryExpression() {
			return getRuleContexts(UnaryExpressionContext.class);
		}
		public UnaryExpressionContext unaryExpression(int i) {
			return getRuleContext(UnaryExpressionContext.class,i);
		}
		public List<TerminalNode> TIMES() { return getTokens(grammarGPParser.TIMES); }
		public TerminalNode TIMES(int i) {
			return getToken(grammarGPParser.TIMES, i);
		}
		public List<TerminalNode> DIV() { return getTokens(grammarGPParser.DIV); }
		public TerminalNode DIV(int i) {
			return getToken(grammarGPParser.DIV, i);
		}
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterMultiplicativeExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitMultiplicativeExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitMultiplicativeExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_multiplicativeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			unaryExpression();
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==TIMES || _la==DIV) {
				{
				{
				setState(122);
				_la = _input.LA(1);
				if ( !(_la==TIMES || _la==DIV) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(123);
				unaryExpression();
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
	public static class AdditiveExpressionContext extends ParserRuleContext {
		public List<MultiplicativeExpressionContext> multiplicativeExpression() {
			return getRuleContexts(MultiplicativeExpressionContext.class);
		}
		public MultiplicativeExpressionContext multiplicativeExpression(int i) {
			return getRuleContext(MultiplicativeExpressionContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(grammarGPParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(grammarGPParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(grammarGPParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(grammarGPParser.MINUS, i);
		}
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterAdditiveExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitAdditiveExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitAdditiveExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			multiplicativeExpression();
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(130);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(131);
				multiplicativeExpression();
				}
				}
				setState(136);
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
	public static class RelationalExpressionContext extends ParserRuleContext {
		public List<AdditiveExpressionContext> additiveExpression() {
			return getRuleContexts(AdditiveExpressionContext.class);
		}
		public AdditiveExpressionContext additiveExpression(int i) {
			return getRuleContext(AdditiveExpressionContext.class,i);
		}
		public RelationContext relation() {
			return getRuleContext(RelationContext.class,0);
		}
		public RelationalExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterRelationalExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitRelationalExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitRelationalExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RelationalExpressionContext relationalExpression() throws RecognitionException {
		RelationalExpressionContext _localctx = new RelationalExpressionContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_relationalExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			additiveExpression();
			setState(141);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1006632960L) != 0)) {
				{
				setState(138);
				relation();
				setState(139);
				additiveExpression();
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
	public static class EqualityExpressionContext extends ParserRuleContext {
		public List<RelationalExpressionContext> relationalExpression() {
			return getRuleContexts(RelationalExpressionContext.class);
		}
		public RelationalExpressionContext relationalExpression(int i) {
			return getRuleContext(RelationalExpressionContext.class,i);
		}
		public EqualityRelationContext equalityRelation() {
			return getRuleContext(EqualityRelationContext.class,0);
		}
		public EqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterEqualityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitEqualityExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitEqualityExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EqualityExpressionContext equalityExpression() throws RecognitionException {
		EqualityExpressionContext _localctx = new EqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_equalityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			relationalExpression();
			setState(147);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQ || _la==NE) {
				{
				setState(144);
				equalityRelation();
				setState(145);
				relationalExpression();
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
	public static class LogicalAndExpressionContext extends ParserRuleContext {
		public List<EqualityExpressionContext> equalityExpression() {
			return getRuleContexts(EqualityExpressionContext.class);
		}
		public EqualityExpressionContext equalityExpression(int i) {
			return getRuleContext(EqualityExpressionContext.class,i);
		}
		public TerminalNode AND() { return getToken(grammarGPParser.AND, 0); }
		public LogicalAndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterLogicalAndExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitLogicalAndExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitLogicalAndExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LogicalAndExpressionContext logicalAndExpression() throws RecognitionException {
		LogicalAndExpressionContext _localctx = new LogicalAndExpressionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_logicalAndExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			equalityExpression();
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AND) {
				{
				setState(150);
				match(AND);
				setState(151);
				equalityExpression();
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
	public static class LogicalOrExpressionContext extends ParserRuleContext {
		public List<LogicalAndExpressionContext> logicalAndExpression() {
			return getRuleContexts(LogicalAndExpressionContext.class);
		}
		public LogicalAndExpressionContext logicalAndExpression(int i) {
			return getRuleContext(LogicalAndExpressionContext.class,i);
		}
		public TerminalNode OR() { return getToken(grammarGPParser.OR, 0); }
		public LogicalOrExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterLogicalOrExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitLogicalOrExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitLogicalOrExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LogicalOrExpressionContext logicalOrExpression() throws RecognitionException {
		LogicalOrExpressionContext _localctx = new LogicalOrExpressionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_logicalOrExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(154);
			logicalAndExpression();
			setState(157);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OR) {
				{
				setState(155);
				match(OR);
				setState(156);
				logicalAndExpression();
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
	public static class ExpressionContext extends ParserRuleContext {
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			logicalOrExpression();
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
	public static class CastExpressionContext extends ParserRuleContext {
		public TypeSpecifierContext typeSpecifier() {
			return getRuleContext(TypeSpecifierContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(grammarGPParser.LPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarGPParser.RPAREN, 0); }
		public CastExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_castExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterCastExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitCastExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitCastExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final CastExpressionContext castExpression() throws RecognitionException {
		CastExpressionContext _localctx = new CastExpressionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_castExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			typeSpecifier();
			setState(162);
			match(LPAREN);
			setState(163);
			expression();
			setState(164);
			match(RPAREN);
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
	public static class RelationContext extends ParserRuleContext {
		public TerminalNode LT() { return getToken(grammarGPParser.LT, 0); }
		public TerminalNode LE() { return getToken(grammarGPParser.LE, 0); }
		public TerminalNode GT() { return getToken(grammarGPParser.GT, 0); }
		public TerminalNode GE() { return getToken(grammarGPParser.GE, 0); }
		public RelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterRelation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitRelation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitRelation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RelationContext relation() throws RecognitionException {
		RelationContext _localctx = new RelationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_relation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1006632960L) != 0)) ) {
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
	public static class EqualityRelationContext extends ParserRuleContext {
		public TerminalNode EQ() { return getToken(grammarGPParser.EQ, 0); }
		public TerminalNode NE() { return getToken(grammarGPParser.NE, 0); }
		public EqualityRelationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityRelation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterEqualityRelation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitEqualityRelation(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitEqualityRelation(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EqualityRelationContext equalityRelation() throws RecognitionException {
		EqualityRelationContext _localctx = new EqualityRelationContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_equalityRelation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			_la = _input.LA(1);
			if ( !(_la==EQ || _la==NE) ) {
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
	public static class UnaryOperatorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(grammarGPParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(grammarGPParser.MINUS, 0); }
		public TerminalNode NOT() { return getToken(grammarGPParser.NOT, 0); }
		public UnaryOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterUnaryOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitUnaryOperator(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitUnaryOperator(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UnaryOperatorContext unaryOperator() throws RecognitionException {
		UnaryOperatorContext _localctx = new UnaryOperatorContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_unaryOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1073742208L) != 0)) ) {
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
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INTEGER_LITERAL() { return getToken(grammarGPParser.INTEGER_LITERAL, 0); }
		public TerminalNode FLOAT_LITERAL() { return getToken(grammarGPParser.FLOAT_LITERAL, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitLiteral(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitLiteral(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			_la = _input.LA(1);
			if ( !(_la==INTEGER_LITERAL || _la==FLOAT_LITERAL) ) {
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
	public static class IdentifierContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(grammarGPParser.IDENTIFIER, 0); }
		public IdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterIdentifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitIdentifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IdentifierContext identifier() throws RecognitionException {
		IdentifierContext _localctx = new IdentifierContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_identifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(IDENTIFIER);
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
	public static class TypeSpecifierContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(grammarGPParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(grammarGPParser.FLOAT, 0); }
		public TypeSpecifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSpecifier; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).enterTypeSpecifier(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof grammarGPListener ) ((grammarGPListener)listener).exitTypeSpecifier(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof grammarGPVisitor ) return ((grammarGPVisitor<? extends T>)visitor).visitTypeSpecifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeSpecifierContext typeSpecifier() throws RecognitionException {
		TypeSpecifierContext _localctx = new TypeSpecifierContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_typeSpecifier);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
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

	public static final String _serializedATN =
		"\u0004\u0001\"\u00b3\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0001\u0000\u0005\u0000"+
		"2\b\u0000\n\u0000\f\u00005\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0005\u0001;\b\u0001\n\u0001\f\u0001>\t\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002J\b\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004W\b\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\br\b\b"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tx\b\t\u0001\n\u0001\n\u0001\n"+
		"\u0005\n}\b\n\n\n\f\n\u0080\t\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005"+
		"\u000b\u0085\b\u000b\n\u000b\f\u000b\u0088\t\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0003\f\u008e\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u0094"+
		"\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u0099\b\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u009e\b\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0000\u0000\u0018\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.\u0000\u0007\u0001\u0000"+
		"\t\n\u0001\u0000\u0007\b\u0001\u0000\u001a\u001d\u0001\u0000\u0018\u0019"+
		"\u0002\u0000\u0007\b\u001e\u001e\u0001\u0000\r\u000e\u0001\u0000\u0016"+
		"\u0017\u00ac\u00003\u0001\u0000\u0000\u0000\u00028\u0001\u0000\u0000\u0000"+
		"\u0004I\u0001\u0000\u0000\u0000\u0006K\u0001\u0000\u0000\u0000\bO\u0001"+
		"\u0000\u0000\u0000\nX\u0001\u0000\u0000\u0000\f^\u0001\u0000\u0000\u0000"+
		"\u000ed\u0001\u0000\u0000\u0000\u0010q\u0001\u0000\u0000\u0000\u0012w"+
		"\u0001\u0000\u0000\u0000\u0014y\u0001\u0000\u0000\u0000\u0016\u0081\u0001"+
		"\u0000\u0000\u0000\u0018\u0089\u0001\u0000\u0000\u0000\u001a\u008f\u0001"+
		"\u0000\u0000\u0000\u001c\u0095\u0001\u0000\u0000\u0000\u001e\u009a\u0001"+
		"\u0000\u0000\u0000 \u009f\u0001\u0000\u0000\u0000\"\u00a1\u0001\u0000"+
		"\u0000\u0000$\u00a6\u0001\u0000\u0000\u0000&\u00a8\u0001\u0000\u0000\u0000"+
		"(\u00aa\u0001\u0000\u0000\u0000*\u00ac\u0001\u0000\u0000\u0000,\u00ae"+
		"\u0001\u0000\u0000\u0000.\u00b0\u0001\u0000\u0000\u000002\u0003\u0004"+
		"\u0002\u000010\u0001\u0000\u0000\u000025\u0001\u0000\u0000\u000031\u0001"+
		"\u0000\u0000\u000034\u0001\u0000\u0000\u000046\u0001\u0000\u0000\u0000"+
		"53\u0001\u0000\u0000\u000067\u0005\u0000\u0000\u00017\u0001\u0001\u0000"+
		"\u0000\u00008<\u0005\u0005\u0000\u00009;\u0003\u0004\u0002\u0000:9\u0001"+
		"\u0000\u0000\u0000;>\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000"+
		"<=\u0001\u0000\u0000\u0000=?\u0001\u0000\u0000\u0000><\u0001\u0000\u0000"+
		"\u0000?@\u0005\u0006\u0000\u0000@\u0003\u0001\u0000\u0000\u0000AB\u0003"+
		"\u0006\u0003\u0000BC\u0005\f\u0000\u0000CJ\u0001\u0000\u0000\u0000DJ\u0003"+
		"\n\u0005\u0000EJ\u0003\b\u0004\u0000FJ\u0003\f\u0006\u0000GJ\u0003\u000e"+
		"\u0007\u0000HJ\u0003\u0002\u0001\u0000IA\u0001\u0000\u0000\u0000ID\u0001"+
		"\u0000\u0000\u0000IE\u0001\u0000\u0000\u0000IF\u0001\u0000\u0000\u0000"+
		"IG\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000\u0000J\u0005\u0001\u0000"+
		"\u0000\u0000KL\u0003,\u0016\u0000LM\u0005\u000b\u0000\u0000MN\u0003 \u0010"+
		"\u0000N\u0007\u0001\u0000\u0000\u0000OP\u0005\u000f\u0000\u0000PQ\u0005"+
		"\u0003\u0000\u0000QR\u0003 \u0010\u0000RS\u0005\u0004\u0000\u0000SV\u0003"+
		"\u0004\u0002\u0000TU\u0005\u0010\u0000\u0000UW\u0003\u0004\u0002\u0000"+
		"VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000W\t\u0001\u0000\u0000"+
		"\u0000XY\u0005\u0011\u0000\u0000YZ\u0005\u0003\u0000\u0000Z[\u0003 \u0010"+
		"\u0000[\\\u0005\u0004\u0000\u0000\\]\u0003\u0004\u0002\u0000]\u000b\u0001"+
		"\u0000\u0000\u0000^_\u0005\u0012\u0000\u0000_`\u0005\u0003\u0000\u0000"+
		"`a\u0003,\u0016\u0000ab\u0005\u0004\u0000\u0000bc\u0005\f\u0000\u0000"+
		"c\r\u0001\u0000\u0000\u0000de\u0005\u0013\u0000\u0000ef\u0005\u0003\u0000"+
		"\u0000fg\u0003 \u0010\u0000gh\u0005\u0004\u0000\u0000hi\u0005\f\u0000"+
		"\u0000i\u000f\u0001\u0000\u0000\u0000jr\u0003*\u0015\u0000kr\u0003,\u0016"+
		"\u0000lr\u0003\"\u0011\u0000mn\u0005\u0003\u0000\u0000no\u0003 \u0010"+
		"\u0000op\u0005\u0004\u0000\u0000pr\u0001\u0000\u0000\u0000qj\u0001\u0000"+
		"\u0000\u0000qk\u0001\u0000\u0000\u0000ql\u0001\u0000\u0000\u0000qm\u0001"+
		"\u0000\u0000\u0000r\u0011\u0001\u0000\u0000\u0000st\u0003(\u0014\u0000"+
		"tu\u0003\u0010\b\u0000ux\u0001\u0000\u0000\u0000vx\u0003\u0010\b\u0000"+
		"ws\u0001\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000x\u0013\u0001\u0000"+
		"\u0000\u0000y~\u0003\u0012\t\u0000z{\u0007\u0000\u0000\u0000{}\u0003\u0012"+
		"\t\u0000|z\u0001\u0000\u0000\u0000}\u0080\u0001\u0000\u0000\u0000~|\u0001"+
		"\u0000\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0015\u0001\u0000"+
		"\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0081\u0086\u0003\u0014\n"+
		"\u0000\u0082\u0083\u0007\u0001\u0000\u0000\u0083\u0085\u0003\u0014\n\u0000"+
		"\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0088\u0001\u0000\u0000\u0000"+
		"\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000"+
		"\u0087\u0017\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000"+
		"\u0089\u008d\u0003\u0016\u000b\u0000\u008a\u008b\u0003$\u0012\u0000\u008b"+
		"\u008c\u0003\u0016\u000b\u0000\u008c\u008e\u0001\u0000\u0000\u0000\u008d"+
		"\u008a\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e"+
		"\u0019\u0001\u0000\u0000\u0000\u008f\u0093\u0003\u0018\f\u0000\u0090\u0091"+
		"\u0003&\u0013\u0000\u0091\u0092\u0003\u0018\f\u0000\u0092\u0094\u0001"+
		"\u0000\u0000\u0000\u0093\u0090\u0001\u0000\u0000\u0000\u0093\u0094\u0001"+
		"\u0000\u0000\u0000\u0094\u001b\u0001\u0000\u0000\u0000\u0095\u0098\u0003"+
		"\u001a\r\u0000\u0096\u0097\u0005\u0014\u0000\u0000\u0097\u0099\u0003\u001a"+
		"\r\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000"+
		"\u0000\u0099\u001d\u0001\u0000\u0000\u0000\u009a\u009d\u0003\u001c\u000e"+
		"\u0000\u009b\u009c\u0005\u0015\u0000\u0000\u009c\u009e\u0003\u001c\u000e"+
		"\u0000\u009d\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000"+
		"\u0000\u009e\u001f\u0001\u0000\u0000\u0000\u009f\u00a0\u0003\u001e\u000f"+
		"\u0000\u00a0!\u0001\u0000\u0000\u0000\u00a1\u00a2\u0003.\u0017\u0000\u00a2"+
		"\u00a3\u0005\u0003\u0000\u0000\u00a3\u00a4\u0003 \u0010\u0000\u00a4\u00a5"+
		"\u0005\u0004\u0000\u0000\u00a5#\u0001\u0000\u0000\u0000\u00a6\u00a7\u0007"+
		"\u0002\u0000\u0000\u00a7%\u0001\u0000\u0000\u0000\u00a8\u00a9\u0007\u0003"+
		"\u0000\u0000\u00a9\'\u0001\u0000\u0000\u0000\u00aa\u00ab\u0007\u0004\u0000"+
		"\u0000\u00ab)\u0001\u0000\u0000\u0000\u00ac\u00ad\u0007\u0005\u0000\u0000"+
		"\u00ad+\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\u001f\u0000\u0000\u00af"+
		"-\u0001\u0000\u0000\u0000\u00b0\u00b1\u0007\u0006\u0000\u0000\u00b1/\u0001"+
		"\u0000\u0000\u0000\f3<IVqw~\u0086\u008d\u0093\u0098\u009d";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}