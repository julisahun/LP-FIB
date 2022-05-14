# Generated from Expr.g by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\7\3*\n\3\f\3\16\3-\13\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\7\5\65\n\5\f\5\16\58\13\5\3\5\3\5\3\6\7\6=\n\6\f\6")
        buf.write("\16\6@\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7W\n\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\be\n")
        buf.write("\b\3\b\2\3\4\t\2\4\6\b\n\f\16\2\3\3\2\26\27\2n\2\23\3")
        buf.write("\2\2\2\4\33\3\2\2\2\6.\3\2\2\2\b\62\3\2\2\2\n>\3\2\2\2")
        buf.write("\fV\3\2\2\2\16d\3\2\2\2\20\22\5\6\4\2\21\20\3\2\2\2\22")
        buf.write("\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\26\3\2\2\2")
        buf.write("\25\23\3\2\2\2\26\27\7\2\2\3\27\3\3\2\2\2\30\31\b\3\1")
        buf.write("\2\31\34\7\23\2\2\32\34\7\22\2\2\33\30\3\2\2\2\33\32\3")
        buf.write("\2\2\2\34+\3\2\2\2\35\36\f\b\2\2\36\37\7\30\2\2\37*\5")
        buf.write("\4\3\b !\f\7\2\2!\"\t\2\2\2\"*\5\4\3\b#$\f\6\2\2$%\7\24")
        buf.write("\2\2%*\5\4\3\7&\'\f\5\2\2\'(\7\25\2\2(*\5\4\3\5)\35\3")
        buf.write("\2\2\2) \3\2\2\2)#\3\2\2\2)&\3\2\2\2*-\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,\5\3\2\2\2-+\3\2\2\2./\7\22\2\2/\60\5\n\6")
        buf.write("\2\60\61\5\b\5\2\61\7\3\2\2\2\62\66\7\5\2\2\63\65\5\f")
        buf.write("\7\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\679\3\2\2\28\66\3\2\2\29:\7\6\2\2:\t\3\2\2\2;=\7")
        buf.write("\22\2\2<;\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\13\3")
        buf.write("\2\2\2@>\3\2\2\2AB\7\20\2\2BW\5\4\3\2CD\7\b\2\2DE\5\16")
        buf.write("\b\2EF\5\b\5\2FW\3\2\2\2GH\7\b\2\2HI\5\16\b\2IJ\5\b\5")
        buf.write("\2JK\7\t\2\2KL\5\b\5\2LW\3\2\2\2MN\7\n\2\2NO\5\16\b\2")
        buf.write("OP\5\b\5\2PW\3\2\2\2QR\7\22\2\2RS\7\21\2\2SW\5\4\3\2T")
        buf.write("U\7\22\2\2UW\5\n\6\2VA\3\2\2\2VC\3\2\2\2VG\3\2\2\2VM\3")
        buf.write("\2\2\2VQ\3\2\2\2VT\3\2\2\2W\r\3\2\2\2XY\5\4\3\2YZ\7\r")
        buf.write("\2\2Z[\5\4\3\2[e\3\2\2\2\\]\5\4\3\2]^\7\13\2\2^_\5\4\3")
        buf.write("\2_e\3\2\2\2`a\5\4\3\2ab\7\f\2\2bc\5\4\3\2ce\3\2\2\2d")
        buf.write("X\3\2\2\2d\\\3\2\2\2d`\3\2\2\2e\17\3\2\2\2\n\23\33)+\66")
        buf.write(">Vd")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'|:'", "':|'", "'   '", 
                     "'if'", "'else'", "'while'", "'>'", "'<'", "'='", "'then'", 
                     "'end'", "'write'", "'<-'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "OP", "CP", "OB", "CB", "IDENT", "IF", 
                      "ELSE", "WHILE", "GT", "LT", "EQ", "THEN", "END", 
                      "WRITE", "ASSIG", "VAR", "NUM", "MES", "SUB", "MULT", 
                      "DIV", "POW", "WS" ]

    RULE_root = 0
    RULE_expr = 1
    RULE_meth = 2
    RULE_body = 3
    RULE_params = 4
    RULE_instr = 5
    RULE_cond = 6

    ruleNames =  [ "root", "expr", "meth", "body", "params", "instr", "cond" ]

    EOF = Token.EOF
    OP=1
    CP=2
    OB=3
    CB=4
    IDENT=5
    IF=6
    ELSE=7
    WHILE=8
    GT=9
    LT=10
    EQ=11
    THEN=12
    END=13
    WRITE=14
    ASSIG=15
    VAR=16
    NUM=17
    MES=18
    SUB=19
    MULT=20
    DIV=21
    POW=22
    WS=23

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

        def meth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MethContext)
            else:
                return self.getTypedRuleContext(ExprParser.MethContext,i)


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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.VAR:
                self.state = 14
                self.meth()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.NUM]:
                localctx = ExprParser.ValorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(ExprParser.NUM)
                pass
            elif token in [ExprParser.VAR]:
                localctx = ExprParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(ExprParser.VAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.PowerContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 28
                        self.match(ExprParser.POW)
                        self.state = 29
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MultContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.MULT or _la==ExprParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.SumaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        self.match(ExprParser.MES)
                        self.state = 35
                        self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.RestaContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(ExprParser.SUB)
                        self.state = 38
                        self.expr(3)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MethContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_meth

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MethodContext(MethContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.MethContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)
        def params(self):
            return self.getTypedRuleContext(ExprParser.ParamsContext,0)

        def body(self):
            return self.getTypedRuleContext(ExprParser.BodyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)



    def meth(self):

        localctx = ExprParser.MethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_meth)
        try:
            localctx = ExprParser.MethodContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.VAR)
            self.state = 45
            self.params()
            self.state = 46
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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

        def OB(self):
            return self.getToken(ExprParser.OB, 0)
        def CB(self):
            return self.getToken(ExprParser.CB, 0)
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
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            localctx = ExprParser.ExecuteBodyContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ExprParser.OB)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.IF) | (1 << ExprParser.WHILE) | (1 << ExprParser.WRITE) | (1 << ExprParser.VAR))) != 0):
                self.state = 49
                self.instr()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(ExprParser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.VAR)
            else:
                return self.getToken(ExprParser.VAR, i)

        def getRuleIndex(self):
            return ExprParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ExprParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.match(ExprParser.VAR) 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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

        def body(self):
            return self.getTypedRuleContext(ExprParser.BodyContext,0)


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

        def body(self):
            return self.getTypedRuleContext(ExprParser.BodyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class ElseBoolContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def cond(self):
            return self.getTypedRuleContext(ExprParser.CondContext,0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BodyContext)
            else:
                return self.getTypedRuleContext(ExprParser.BodyContext,i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBool" ):
                return visitor.visitElseBool(self)
            else:
                return visitor.visitChildren(self)


    class InvokeContext(InstrContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.InstrContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)
        def params(self):
            return self.getTypedRuleContext(ExprParser.ParamsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvoke" ):
                return visitor.visitInvoke(self)
            else:
                return visitor.visitChildren(self)



    def instr(self):

        localctx = ExprParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instr)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = ExprParser.EscriuContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(ExprParser.WRITE)
                self.state = 64
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.BoolContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(ExprParser.IF)
                self.state = 66
                self.cond()
                self.state = 67
                self.body()
                pass

            elif la_ == 3:
                localctx = ExprParser.ElseBoolContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(ExprParser.IF)
                self.state = 70
                self.cond()
                self.state = 71
                self.body()
                self.state = 72
                self.match(ExprParser.ELSE)
                self.state = 73
                self.body()
                pass

            elif la_ == 4:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(ExprParser.WHILE)
                self.state = 76
                self.cond()
                self.state = 77
                self.body()
                pass

            elif la_ == 5:
                localctx = ExprParser.AssigContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 79
                self.match(ExprParser.VAR)
                self.state = 80
                self.match(ExprParser.ASSIG)
                self.state = 81
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = ExprParser.InvokeContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 82
                self.match(ExprParser.VAR)
                self.state = 83
                self.params()
                pass


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
        self.enterRule(localctx, 12, self.RULE_cond)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = ExprParser.EqualContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(ExprParser.EQ)
                self.state = 88
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = ExprParser.MoreContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(ExprParser.GT)
                self.state = 92
                self.expr(0)
                pass

            elif la_ == 3:
                localctx = ExprParser.LessContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(ExprParser.LT)
                self.state = 96
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
         




