# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\2\3\2\3\3\3\3\3\3\5\3\30\n\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3&\n\3")
        buf.write("\f\3\16\3)\13\3\3\4\7\4,\n\4\f\4\16\4/\13\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5B\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6P\n\6\3\6\2\3\4\7\2\4\6\b\n\2\3\3\2\25\26")
        buf.write("\2X\2\17\3\2\2\2\4\27\3\2\2\2\6-\3\2\2\2\bA\3\2\2\2\n")
        buf.write("O\3\2\2\2\f\16\5\b\5\2\r\f\3\2\2\2\16\21\3\2\2\2\17\r")
        buf.write("\3\2\2\2\17\20\3\2\2\2\20\22\3\2\2\2\21\17\3\2\2\2\22")
        buf.write("\23\7\2\2\3\23\3\3\2\2\2\24\25\b\3\1\2\25\30\7\22\2\2")
        buf.write("\26\30\7\21\2\2\27\24\3\2\2\2\27\26\3\2\2\2\30\'\3\2\2")
        buf.write("\2\31\32\f\b\2\2\32\33\7\27\2\2\33&\5\4\3\b\34\35\f\7")
        buf.write("\2\2\35\36\t\2\2\2\36&\5\4\3\b\37 \f\6\2\2 !\7\23\2\2")
        buf.write("!&\5\4\3\7\"#\f\5\2\2#$\7\24\2\2$&\5\4\3\5%\31\3\2\2\2")
        buf.write("%\34\3\2\2\2%\37\3\2\2\2%\"\3\2\2\2&)\3\2\2\2\'%\3\2\2")
        buf.write("\2\'(\3\2\2\2(\5\3\2\2\2)\'\3\2\2\2*,\5\b\5\2+*\3\2\2")
        buf.write("\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\7\3\2\2\2/-\3\2\2\2")
        buf.write("\60\61\7\17\2\2\61B\5\4\3\2\62\63\7\b\2\2\63\64\5\n\6")
        buf.write("\2\64\65\7\r\2\2\65\66\5\6\4\2\66\67\7\16\2\2\67B\3\2")
        buf.write("\2\289\7\t\2\29:\5\n\6\2:;\7\r\2\2;<\5\6\4\2<=\7\16\2")
        buf.write("\2=B\3\2\2\2>?\7\21\2\2?@\7\20\2\2@B\5\4\3\2A\60\3\2\2")
        buf.write("\2A\62\3\2\2\2A8\3\2\2\2A>\3\2\2\2B\t\3\2\2\2CD\5\4\3")
        buf.write("\2DE\7\f\2\2EF\5\4\3\2FP\3\2\2\2GH\5\4\3\2HI\7\n\2\2I")
        buf.write("J\5\4\3\2JP\3\2\2\2KL\5\4\3\2LM\7\13\2\2MN\5\4\3\2NP\3")
        buf.write("\2\2\2OC\3\2\2\2OG\3\2\2\2OK\3\2\2\2P\13\3\2\2\2\t\17")
        buf.write("\27%\'-AO")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'|:'", "':|'", "'   '", 
                     "'if'", "'while'", "'>'", "'<'", "'='", "'then'", "'end'", 
                     "'write'", "':='", "<INVALID>", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "OP", "CP", "OB", "CB", "IDENT", "IF", 
                      "WHILE", "GT", "LT", "EQ", "THEN", "END", "WRITE", 
                      "ASSIG", "VAR", "NUM", "MES", "SUB", "MULT", "DIV", 
                      "POW", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_body = 2
    RULE_instr = 3
    RULE_cond = 4

    ruleNames =  [ "root", "expr", "body", "instr", "cond" ]

    EOF = Token.EOF
    OP=1
    CP=2
    OB=3
    CB=4
    IDENT=5
    IF=6
    WHILE=7
    GT=8
    LT=9
    EQ=10
    THEN=11
    END=12
    WRITE=13
    ASSIG=14
    VAR=15
    NUM=16
    MES=17
    SUB=18
    MULT=19
    DIV=20
    POW=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstrContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstrContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.IF) | (1 << ExprParser.WHILE) | (1 << ExprParser.WRITE) | (1 << ExprParser.VAR))) != 0):
                self.state = 10
                self.instr()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SumaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MES(self):
            return self.getToken(ExprParser.MES, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuma" ):
                return visitor.visitSuma(self)
            else:
                return visitor.visitChildren(self)


    class MultContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ValorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)


    class PowerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)


    class RestaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResta" ):
                return visitor.visitResta(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.NUM]:
                localctx = ExprParser.ValorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(ExprParser.NUM)
                pass
            elif token in [ExprParser.VAR]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(ExprParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 35
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.PowerContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        self.match(ExprParser.POW)
                        self.state = 25
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.MULT or _la==ExprParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.SumaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        self.match(ExprParser.MES)
                        self.state = 31
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.RestaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        self.match(ExprParser.SUB)
                        self.state = 34
                        self.expr(3)
                        pass

             
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_body

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExecuteBodyContext(BodyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.BodyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.InstrContext)
            else:
                return self.getTypedRuleContext(ExprParser.InstrContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecuteBody" ):
                return visitor.visitExecuteBody(self)
            else:
                return visitor.visitChildren(self)



    def body(self):

        localctx = ExprParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.ExecuteBodyContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.IF) | (1 << ExprParser.WHILE) | (1 << ExprParser.WRITE) | (1 << ExprParser.VAR))) != 0):
                self.state = 40
                self.instr()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_instr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)

        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)
        def body(self):
            return self.getTypedRuleContext(ExprParser.BodyContext,0)

        def END(self):
            return self.getToken(ExprParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class AssigContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)
        def ASSIG(self):
            return self.getToken(ExprParser.ASSIG, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig" ):
                return visitor.visitAssig(self)
            else:
                return visitor.visitChildren(self)


    class EscriuContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscriu" ):
                return visitor.visitEscriu(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)

        def THEN(self):
            return self.getToken(ExprParser.THEN, 0)
        def body(self):
            return self.getTypedRuleContext(ExprParser.BodyContext,0)

        def END(self):
            return self.getToken(ExprParser.END, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)



    def instr(self):

        localctx = ExprParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instr)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.WRITE]:
                localctx = ExprParser.EscriuContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(ExprParser.WRITE)
                self.state = 47
                self.expr(0)
                pass
            elif token in [ExprParser.IF]:
                localctx = ExprParser.BoolContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(ExprParser.IF)
                self.state = 49
                self.cond()
                self.state = 50
                self.match(ExprParser.THEN)
                self.state = 51
                self.body()
                self.state = 52
                self.match(ExprParser.END)
                pass
            elif token in [ExprParser.WHILE]:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(ExprParser.WHILE)
                self.state = 55
                self.cond()
                self.state = 56
                self.match(ExprParser.THEN)
                self.state = 57
                self.body()
                self.state = 58
                self.match(ExprParser.END)
                pass
            elif token in [ExprParser.VAR]:
                localctx = ExprParser.AssigContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.match(ExprParser.VAR)
                self.state = 61
                self.match(ExprParser.ASSIG)
                self.state = 62
                self.expr(0)
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

    class CondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MoreContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def GT(self):
            return self.getToken(ExprParser.GT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMore" ):
                return visitor.visitMore(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class LessContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LT(self):
            return self.getToken(ExprParser.LT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLess" ):
                return visitor.visitLess(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = ExprParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cond)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(ExprParser.EQ)
                self.state = 67
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.MoreContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.match(ExprParser.GT)
                self.state = 71
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.match(ExprParser.LT)
                self.state = 75
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




