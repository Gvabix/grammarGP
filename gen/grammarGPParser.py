# Generated from grammarGP.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,208,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,5,0,56,8,0,10,0,12,0,59,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
        68,8,1,1,2,1,2,5,2,72,8,2,10,2,12,2,75,9,2,1,2,1,2,1,3,3,3,80,8,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,95,8,4,
        10,4,12,4,98,9,4,1,4,3,4,101,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,3,6,116,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,3,11,143,8,11,1,12,1,12,1,12,1,12,3,12,149,8,12,1,
        13,1,13,1,13,5,13,154,8,13,10,13,12,13,157,9,13,1,14,1,14,1,14,5,
        14,162,8,14,10,14,12,14,165,9,14,1,15,1,15,1,15,1,15,3,15,171,8,
        15,1,16,1,16,1,16,1,16,3,16,177,8,16,1,17,1,17,1,17,3,17,182,8,17,
        1,18,1,18,1,18,3,18,187,8,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,
        1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,26,
        0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,0,7,1,0,9,10,1,0,7,8,1,0,28,31,1,0,26,27,2,0,7,
        8,32,32,1,0,13,14,1,0,24,25,205,0,57,1,0,0,0,2,67,1,0,0,0,4,69,1,
        0,0,0,6,79,1,0,0,0,8,86,1,0,0,0,10,102,1,0,0,0,12,115,1,0,0,0,14,
        117,1,0,0,0,16,120,1,0,0,0,18,123,1,0,0,0,20,129,1,0,0,0,22,142,
        1,0,0,0,24,148,1,0,0,0,26,150,1,0,0,0,28,158,1,0,0,0,30,166,1,0,
        0,0,32,172,1,0,0,0,34,178,1,0,0,0,36,183,1,0,0,0,38,188,1,0,0,0,
        40,190,1,0,0,0,42,195,1,0,0,0,44,197,1,0,0,0,46,199,1,0,0,0,48,201,
        1,0,0,0,50,203,1,0,0,0,52,205,1,0,0,0,54,56,3,2,1,0,55,54,1,0,0,
        0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,
        1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,68,3,6,3,0,63,68,3,10,5,0,
        64,68,3,8,4,0,65,68,3,18,9,0,66,68,3,20,10,0,67,62,1,0,0,0,67,63,
        1,0,0,0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,
        73,5,5,0,0,70,72,3,12,6,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,0,
        0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,6,0,0,77,5,
        1,0,0,0,78,80,3,52,26,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,
        0,81,82,3,50,25,0,82,83,5,11,0,0,83,84,3,38,19,0,84,85,5,12,0,0,
        85,7,1,0,0,0,86,87,5,15,0,0,87,88,5,3,0,0,88,89,3,38,19,0,89,90,
        5,4,0,0,90,100,3,4,2,0,91,92,5,16,0,0,92,96,5,5,0,0,93,95,3,12,6,
        0,94,93,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,
        1,0,0,0,98,96,1,0,0,0,99,101,5,6,0,0,100,91,1,0,0,0,100,101,1,0,
        0,0,101,9,1,0,0,0,102,103,5,17,0,0,103,104,5,3,0,0,104,105,3,38,
        19,0,105,106,5,4,0,0,106,107,3,4,2,0,107,11,1,0,0,0,108,116,3,6,
        3,0,109,116,3,8,4,0,110,116,3,18,9,0,111,116,3,20,10,0,112,116,3,
        14,7,0,113,116,3,16,8,0,114,116,3,10,5,0,115,108,1,0,0,0,115,109,
        1,0,0,0,115,110,1,0,0,0,115,111,1,0,0,0,115,112,1,0,0,0,115,113,
        1,0,0,0,115,114,1,0,0,0,116,13,1,0,0,0,117,118,5,20,0,0,118,119,
        5,12,0,0,119,15,1,0,0,0,120,121,5,21,0,0,121,122,5,12,0,0,122,17,
        1,0,0,0,123,124,5,18,0,0,124,125,5,3,0,0,125,126,3,50,25,0,126,127,
        5,4,0,0,127,128,5,12,0,0,128,19,1,0,0,0,129,130,5,19,0,0,130,131,
        5,3,0,0,131,132,3,38,19,0,132,133,5,4,0,0,133,134,5,12,0,0,134,21,
        1,0,0,0,135,143,3,48,24,0,136,143,3,50,25,0,137,143,3,40,20,0,138,
        139,5,3,0,0,139,140,3,38,19,0,140,141,5,4,0,0,141,143,1,0,0,0,142,
        135,1,0,0,0,142,136,1,0,0,0,142,137,1,0,0,0,142,138,1,0,0,0,143,
        23,1,0,0,0,144,145,3,46,23,0,145,146,3,22,11,0,146,149,1,0,0,0,147,
        149,3,22,11,0,148,144,1,0,0,0,148,147,1,0,0,0,149,25,1,0,0,0,150,
        155,3,24,12,0,151,152,7,0,0,0,152,154,3,24,12,0,153,151,1,0,0,0,
        154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,27,1,0,0,0,157,
        155,1,0,0,0,158,163,3,26,13,0,159,160,7,1,0,0,160,162,3,26,13,0,
        161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,
        164,29,1,0,0,0,165,163,1,0,0,0,166,170,3,28,14,0,167,168,3,42,21,
        0,168,169,3,28,14,0,169,171,1,0,0,0,170,167,1,0,0,0,170,171,1,0,
        0,0,171,31,1,0,0,0,172,176,3,30,15,0,173,174,3,44,22,0,174,175,3,
        30,15,0,175,177,1,0,0,0,176,173,1,0,0,0,176,177,1,0,0,0,177,33,1,
        0,0,0,178,181,3,32,16,0,179,180,5,22,0,0,180,182,3,32,16,0,181,179,
        1,0,0,0,181,182,1,0,0,0,182,35,1,0,0,0,183,186,3,34,17,0,184,185,
        5,23,0,0,185,187,3,34,17,0,186,184,1,0,0,0,186,187,1,0,0,0,187,37,
        1,0,0,0,188,189,3,36,18,0,189,39,1,0,0,0,190,191,3,52,26,0,191,192,
        5,3,0,0,192,193,3,38,19,0,193,194,5,4,0,0,194,41,1,0,0,0,195,196,
        7,2,0,0,196,43,1,0,0,0,197,198,7,3,0,0,198,45,1,0,0,0,199,200,7,
        4,0,0,200,47,1,0,0,0,201,202,7,5,0,0,202,49,1,0,0,0,203,204,5,33,
        0,0,204,51,1,0,0,0,205,206,7,6,0,0,206,53,1,0,0,0,15,57,67,73,79,
        96,100,115,142,148,155,163,170,176,181,186
    ]

class grammarGPParser ( Parser ):

    grammarFileName = "grammarGP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'.'", "'('", "')'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "';'", "<INVALID>", 
                     "<INVALID>", "'if'", "'else'", "'while'", "'read'", 
                     "'write'", "'break'", "'continue'", "'&&'", "'||'", 
                     "'int'", "'float'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'!'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "DOT", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "PLUS", "MINUS", "TIMES", "DIV", "ASSIGN", 
                      "SEMI", "INTEGER_LITERAL", "FLOAT_LITERAL", "IF", 
                      "ELSE", "WHILE", "READ", "WRITE", "BREAK", "CONTINUE", 
                      "AND", "OR", "INT", "FLOAT", "EQ", "NE", "LT", "GT", 
                      "LE", "GE", "NOT", "IDENTIFIER", "WS", "DIGIT", "LETTER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block = 2
    RULE_assignmentStatement = 3
    RULE_ifStatement = 4
    RULE_loopStatement = 5
    RULE_loopStatementContent = 6
    RULE_breakStatement = 7
    RULE_continueStatement = 8
    RULE_read = 9
    RULE_write = 10
    RULE_primaryExpression = 11
    RULE_unaryExpression = 12
    RULE_multiplicativeExpression = 13
    RULE_additiveExpression = 14
    RULE_relationalExpression = 15
    RULE_equalityExpression = 16
    RULE_logicalAndExpression = 17
    RULE_logicalOrExpression = 18
    RULE_expression = 19
    RULE_castExpression = 20
    RULE_relation = 21
    RULE_equalityRelation = 22
    RULE_unaryOperator = 23
    RULE_literal = 24
    RULE_identifier = 25
    RULE_typeSpecifier = 26

    ruleNames =  [ "program", "statement", "block", "assignmentStatement", 
                   "ifStatement", "loopStatement", "loopStatementContent", 
                   "breakStatement", "continueStatement", "read", "write", 
                   "primaryExpression", "unaryExpression", "multiplicativeExpression", 
                   "additiveExpression", "relationalExpression", "equalityExpression", 
                   "logicalAndExpression", "logicalOrExpression", "expression", 
                   "castExpression", "relation", "equalityRelation", "unaryOperator", 
                   "literal", "identifier", "typeSpecifier" ]

    EOF = Token.EOF
    COMMA=1
    DOT=2
    LPAREN=3
    RPAREN=4
    LBRACE=5
    RBRACE=6
    PLUS=7
    MINUS=8
    TIMES=9
    DIV=10
    ASSIGN=11
    SEMI=12
    INTEGER_LITERAL=13
    FLOAT_LITERAL=14
    IF=15
    ELSE=16
    WHILE=17
    READ=18
    WRITE=19
    BREAK=20
    CONTINUE=21
    AND=22
    OR=23
    INT=24
    FLOAT=25
    EQ=26
    NE=27
    LT=28
    GT=29
    LE=30
    GE=31
    NOT=32
    IDENTIFIER=33
    WS=34
    DIGIT=35
    LETTER=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(grammarGPParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarGPParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = grammarGPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8641216512) != 0):
                self.state = 54
                self.statement()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(grammarGPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(grammarGPParser.AssignmentStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(grammarGPParser.LoopStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(grammarGPParser.IfStatementContext,0)


        def read(self):
            return self.getTypedRuleContext(grammarGPParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(grammarGPParser.WriteContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = grammarGPParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.assignmentStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.loopStatement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.ifStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.read()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.write()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(grammarGPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(grammarGPParser.RBRACE, 0)

        def loopStatementContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.LoopStatementContentContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.LoopStatementContentContext,i)


        def getRuleIndex(self):
            return grammarGPParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = grammarGPParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(grammarGPParser.LBRACE)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8644362240) != 0):
                self.state = 70
                self.loopStatementContent()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(grammarGPParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(grammarGPParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(grammarGPParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarGPParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(grammarGPParser.SEMI, 0)

        def typeSpecifier(self):
            return self.getTypedRuleContext(grammarGPParser.TypeSpecifierContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = grammarGPParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24 or _la==25:
                self.state = 78
                self.typeSpecifier()


            self.state = 81
            self.identifier()
            self.state = 82
            self.match(grammarGPParser.ASSIGN)
            self.state = 83
            self.expression()
            self.state = 84
            self.match(grammarGPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(grammarGPParser.IF, 0)

        def LPAREN(self):
            return self.getToken(grammarGPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarGPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarGPParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(grammarGPParser.BlockContext,0)


        def ELSE(self):
            return self.getToken(grammarGPParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(grammarGPParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(grammarGPParser.RBRACE, 0)

        def loopStatementContent(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.LoopStatementContentContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.LoopStatementContentContext,i)


        def getRuleIndex(self):
            return grammarGPParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = grammarGPParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(grammarGPParser.IF)
            self.state = 87
            self.match(grammarGPParser.LPAREN)
            self.state = 88
            self.expression()
            self.state = 89
            self.match(grammarGPParser.RPAREN)
            self.state = 90
            self.block()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 91
                self.match(grammarGPParser.ELSE)
                self.state = 92
                self.match(grammarGPParser.LBRACE)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8644362240) != 0):
                    self.state = 93
                    self.loopStatementContent()
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 99
                self.match(grammarGPParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(grammarGPParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(grammarGPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarGPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarGPParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(grammarGPParser.BlockContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_loopStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatement" ):
                listener.enterLoopStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatement" ):
                listener.exitLoopStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatement" ):
                return visitor.visitLoopStatement(self)
            else:
                return visitor.visitChildren(self)




    def loopStatement(self):

        localctx = grammarGPParser.LoopStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_loopStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(grammarGPParser.WHILE)
            self.state = 103
            self.match(grammarGPParser.LPAREN)
            self.state = 104
            self.expression()
            self.state = 105
            self.match(grammarGPParser.RPAREN)
            self.state = 106
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStatementContentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(grammarGPParser.AssignmentStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(grammarGPParser.IfStatementContext,0)


        def read(self):
            return self.getTypedRuleContext(grammarGPParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(grammarGPParser.WriteContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(grammarGPParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(grammarGPParser.ContinueStatementContext,0)


        def loopStatement(self):
            return self.getTypedRuleContext(grammarGPParser.LoopStatementContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_loopStatementContent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopStatementContent" ):
                listener.enterLoopStatementContent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopStatementContent" ):
                listener.exitLoopStatementContent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStatementContent" ):
                return visitor.visitLoopStatementContent(self)
            else:
                return visitor.visitChildren(self)




    def loopStatementContent(self):

        localctx = grammarGPParser.LoopStatementContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopStatementContent)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.assignmentStatement()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.ifStatement()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.read()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.write()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.breakStatement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.continueStatement()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.loopStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(grammarGPParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(grammarGPParser.SEMI, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = grammarGPParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(grammarGPParser.BREAK)
            self.state = 118
            self.match(grammarGPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(grammarGPParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(grammarGPParser.SEMI, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = grammarGPParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(grammarGPParser.CONTINUE)
            self.state = 121
            self.match(grammarGPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(grammarGPParser.READ, 0)

        def LPAREN(self):
            return self.getToken(grammarGPParser.LPAREN, 0)

        def identifier(self):
            return self.getTypedRuleContext(grammarGPParser.IdentifierContext,0)


        def RPAREN(self):
            return self.getToken(grammarGPParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(grammarGPParser.SEMI, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = grammarGPParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(grammarGPParser.READ)
            self.state = 124
            self.match(grammarGPParser.LPAREN)
            self.state = 125
            self.identifier()
            self.state = 126
            self.match(grammarGPParser.RPAREN)
            self.state = 127
            self.match(grammarGPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(grammarGPParser.WRITE, 0)

        def LPAREN(self):
            return self.getToken(grammarGPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarGPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarGPParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(grammarGPParser.SEMI, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = grammarGPParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(grammarGPParser.WRITE)
            self.state = 130
            self.match(grammarGPParser.LPAREN)
            self.state = 131
            self.expression()
            self.state = 132
            self.match(grammarGPParser.RPAREN)
            self.state = 133
            self.match(grammarGPParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(grammarGPParser.LiteralContext,0)


        def identifier(self):
            return self.getTypedRuleContext(grammarGPParser.IdentifierContext,0)


        def castExpression(self):
            return self.getTypedRuleContext(grammarGPParser.CastExpressionContext,0)


        def LPAREN(self):
            return self.getToken(grammarGPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarGPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarGPParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = grammarGPParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primaryExpression)
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.literal()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.identifier()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.castExpression()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 138
                self.match(grammarGPParser.LPAREN)
                self.state = 139
                self.expression()
                self.state = 140
                self.match(grammarGPParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOperator(self):
            return self.getTypedRuleContext(grammarGPParser.UnaryOperatorContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(grammarGPParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpression(self):

        localctx = grammarGPParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unaryExpression)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.unaryOperator()
                self.state = 145
                self.primaryExpression()
                pass
            elif token in [3, 13, 14, 24, 25, 33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.UnaryExpressionContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGPParser.TIMES)
            else:
                return self.getToken(grammarGPParser.TIMES, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGPParser.DIV)
            else:
                return self.getToken(grammarGPParser.DIV, i)

        def getRuleIndex(self):
            return grammarGPParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = grammarGPParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.unaryExpression()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 151
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 152
                self.unaryExpression()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGPParser.PLUS)
            else:
                return self.getToken(grammarGPParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammarGPParser.MINUS)
            else:
                return self.getToken(grammarGPParser.MINUS, i)

        def getRuleIndex(self):
            return grammarGPParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = grammarGPParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.multiplicativeExpression()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 159
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 160
                self.multiplicativeExpression()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.AdditiveExpressionContext,i)


        def relation(self):
            return self.getTypedRuleContext(grammarGPParser.RelationContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = grammarGPParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.additiveExpression()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0):
                self.state = 167
                self.relation()
                self.state = 168
                self.additiveExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.RelationalExpressionContext,i)


        def equalityRelation(self):
            return self.getTypedRuleContext(grammarGPParser.EqualityRelationContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = grammarGPParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.relationalExpression()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 173
                self.equalityRelation()
                self.state = 174
                self.relationalExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.EqualityExpressionContext,i)


        def AND(self):
            return self.getToken(grammarGPParser.AND, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = grammarGPParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.equalityExpression()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 179
                self.match(grammarGPParser.AND)
                self.state = 180
                self.equalityExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarGPParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(grammarGPParser.LogicalAndExpressionContext,i)


        def OR(self):
            return self.getToken(grammarGPParser.OR, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = grammarGPParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.logicalAndExpression()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 184
                self.match(grammarGPParser.OR)
                self.state = 185
                self.logicalAndExpression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(grammarGPParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return grammarGPParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = grammarGPParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CastExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpecifier(self):
            return self.getTypedRuleContext(grammarGPParser.TypeSpecifierContext,0)


        def LPAREN(self):
            return self.getToken(grammarGPParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarGPParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarGPParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_castExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCastExpression" ):
                listener.enterCastExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCastExpression" ):
                listener.exitCastExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCastExpression" ):
                return visitor.visitCastExpression(self)
            else:
                return visitor.visitChildren(self)




    def castExpression(self):

        localctx = grammarGPParser.CastExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_castExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.typeSpecifier()
            self.state = 191
            self.match(grammarGPParser.LPAREN)
            self.state = 192
            self.expression()
            self.state = 193
            self.match(grammarGPParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(grammarGPParser.LT, 0)

        def LE(self):
            return self.getToken(grammarGPParser.LE, 0)

        def GT(self):
            return self.getToken(grammarGPParser.GT, 0)

        def GE(self):
            return self.getToken(grammarGPParser.GE, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)




    def relation(self):

        localctx = grammarGPParser.RelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityRelationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(grammarGPParser.EQ, 0)

        def NE(self):
            return self.getToken(grammarGPParser.NE, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_equalityRelation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityRelation" ):
                listener.enterEqualityRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityRelation" ):
                listener.exitEqualityRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityRelation" ):
                return visitor.visitEqualityRelation(self)
            else:
                return visitor.visitChildren(self)




    def equalityRelation(self):

        localctx = grammarGPParser.EqualityRelationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_equalityRelation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(grammarGPParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(grammarGPParser.MINUS, 0)

        def NOT(self):
            return self.getToken(grammarGPParser.NOT, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperator" ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperator" ):
                listener.exitUnaryOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOperator" ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryOperator(self):

        localctx = grammarGPParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4294967680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(grammarGPParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(grammarGPParser.FLOAT_LITERAL, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = grammarGPParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(grammarGPParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = grammarGPParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(grammarGPParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(grammarGPParser.INT, 0)

        def FLOAT(self):
            return self.getToken(grammarGPParser.FLOAT, 0)

        def getRuleIndex(self):
            return grammarGPParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = grammarGPParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_typeSpecifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





