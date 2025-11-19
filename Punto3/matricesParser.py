# Generated from matrices.g4 by ANTLR 4.13.1
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
        4,1,15,74,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,0,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,5,3,39,8,3,10,3,12,3,42,
        9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,54,8,6,10,6,12,6,
        57,9,6,1,7,1,7,1,7,5,7,62,8,7,10,7,12,7,65,9,7,1,8,1,8,1,8,1,8,1,
        8,3,8,72,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,1,1,0,6,7,69,0,18,
        1,0,0,0,2,25,1,0,0,0,4,28,1,0,0,0,6,40,1,0,0,0,8,43,1,0,0,0,10,46,
        1,0,0,0,12,50,1,0,0,0,14,58,1,0,0,0,16,71,1,0,0,0,18,19,3,2,1,0,
        19,20,3,6,3,0,20,21,5,0,0,1,21,1,1,0,0,0,22,24,3,4,2,0,23,22,1,0,
        0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,25,
        1,0,0,0,28,29,5,11,0,0,29,30,5,12,0,0,30,31,5,1,0,0,31,32,5,13,0,
        0,32,33,5,2,0,0,33,34,5,13,0,0,34,35,5,3,0,0,35,36,5,4,0,0,36,5,
        1,0,0,0,37,39,3,8,4,0,38,37,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,
        40,41,1,0,0,0,41,7,1,0,0,0,42,40,1,0,0,0,43,44,3,10,5,0,44,45,5,
        4,0,0,45,9,1,0,0,0,46,47,5,12,0,0,47,48,5,5,0,0,48,49,3,12,6,0,49,
        11,1,0,0,0,50,55,3,14,7,0,51,52,7,0,0,0,52,54,3,14,7,0,53,51,1,0,
        0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,13,1,0,0,0,57,55,
        1,0,0,0,58,63,3,16,8,0,59,60,5,8,0,0,60,62,3,16,8,0,61,59,1,0,0,
        0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,15,1,0,0,0,65,63,
        1,0,0,0,66,72,5,12,0,0,67,68,5,9,0,0,68,69,3,12,6,0,69,70,5,10,0,
        0,70,72,1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,72,17,1,0,0,0,5,25,40,
        55,63,71
    ]

class matricesParser ( Parser ):

    grammarFileName = "matrices.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "','", "']'", "';'", "'='", "'+'", 
                     "'-'", "'*'", "'('", "')'", "'mat'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MAT", "ID", 
                      "NUM", "WS", "LINE_COMMENT" ]

    RULE_prog = 0
    RULE_declList = 1
    RULE_decl = 2
    RULE_stmtList = 3
    RULE_stmt = 4
    RULE_assign = 5
    RULE_expr = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "prog", "declList", "decl", "stmtList", "stmt", "assign", 
                   "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    MAT=11
    ID=12
    NUM=13
    WS=14
    LINE_COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declList(self):
            return self.getTypedRuleContext(matricesParser.DeclListContext,0)


        def stmtList(self):
            return self.getTypedRuleContext(matricesParser.StmtListContext,0)


        def EOF(self):
            return self.getToken(matricesParser.EOF, 0)

        def getRuleIndex(self):
            return matricesParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = matricesParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.declList()
            self.state = 19
            self.stmtList()
            self.state = 20
            self.match(matricesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.DeclContext)
            else:
                return self.getTypedRuleContext(matricesParser.DeclContext,i)


        def getRuleIndex(self):
            return matricesParser.RULE_declList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclList" ):
                listener.enterDeclList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclList" ):
                listener.exitDeclList(self)




    def declList(self):

        localctx = matricesParser.DeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 22
                self.decl()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAT(self):
            return self.getToken(matricesParser.MAT, 0)

        def ID(self):
            return self.getToken(matricesParser.ID, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(matricesParser.NUM)
            else:
                return self.getToken(matricesParser.NUM, i)

        def getRuleIndex(self):
            return matricesParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = matricesParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(matricesParser.MAT)
            self.state = 29
            self.match(matricesParser.ID)
            self.state = 30
            self.match(matricesParser.T__0)
            self.state = 31
            self.match(matricesParser.NUM)
            self.state = 32
            self.match(matricesParser.T__1)
            self.state = 33
            self.match(matricesParser.NUM)
            self.state = 34
            self.match(matricesParser.T__2)
            self.state = 35
            self.match(matricesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.StmtContext)
            else:
                return self.getTypedRuleContext(matricesParser.StmtContext,i)


        def getRuleIndex(self):
            return matricesParser.RULE_stmtList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtList" ):
                listener.enterStmtList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtList" ):
                listener.exitStmtList(self)




    def stmtList(self):

        localctx = matricesParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 37
                self.stmt()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(matricesParser.AssignContext,0)


        def getRuleIndex(self):
            return matricesParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = matricesParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.assign()
            self.state = 44
            self.match(matricesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(matricesParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(matricesParser.ExprContext,0)


        def getRuleIndex(self):
            return matricesParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = matricesParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(matricesParser.ID)
            self.state = 47
            self.match(matricesParser.T__4)
            self.state = 48
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.TermContext)
            else:
                return self.getTypedRuleContext(matricesParser.TermContext,i)


        def getRuleIndex(self):
            return matricesParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = matricesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.term()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52
                self.term()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(matricesParser.FactorContext)
            else:
                return self.getTypedRuleContext(matricesParser.FactorContext,i)


        def getRuleIndex(self):
            return matricesParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = matricesParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.factor()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 59
                self.match(matricesParser.T__7)
                self.state = 60
                self.factor()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(matricesParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(matricesParser.ExprContext,0)


        def getRuleIndex(self):
            return matricesParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = matricesParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(matricesParser.ID)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.match(matricesParser.T__8)
                self.state = 68
                self.expr()
                self.state = 69
                self.match(matricesParser.T__9)
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





