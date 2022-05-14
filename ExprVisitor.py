# Generated from Expr.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Suma.
    def visitSuma(self, ctx:ExprParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Mult.
    def visitMult(self, ctx:ExprParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Var.
    def visitVar(self, ctx:ExprParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Valor.
    def visitValor(self, ctx:ExprParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Power.
    def visitPower(self, ctx:ExprParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Resta.
    def visitResta(self, ctx:ExprParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Method.
    def visitMethod(self, ctx:ExprParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ExecuteBody.
    def visitExecuteBody(self, ctx:ExprParser.ExecuteBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#params.
    def visitParams(self, ctx:ExprParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Escriu.
    def visitEscriu(self, ctx:ExprParser.EscriuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Bool.
    def visitBool(self, ctx:ExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ElseBool.
    def visitElseBool(self, ctx:ExprParser.ElseBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#While.
    def visitWhile(self, ctx:ExprParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Assig.
    def visitAssig(self, ctx:ExprParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Invoke.
    def visitInvoke(self, ctx:ExprParser.InvokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Equal.
    def visitEqual(self, ctx:ExprParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#More.
    def visitMore(self, ctx:ExprParser.MoreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#Less.
    def visitLess(self, ctx:ExprParser.LessContext):
        return self.visitChildren(ctx)



del ExprParser