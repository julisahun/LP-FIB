if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

dick = {}

class EvalVisitor(ExprVisitor):


    def visitRoot(self, ctx):
        l = list(ctx.getChildren())        
        self.visit(l[0])

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        dick[l[0].getText()] = self.visit(l[2])

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())
        
    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) + self.visit(l[2])
    
    def visitResta(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) - self.visit(l[2]) 

    def visitMult(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getText() == '*':
            return self.visit(l[0]) * self.visit(l[2]) 
        else:
            return self.visit(l[0]) / self.visit(l[2]) 
    def visitPower(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) ** self.visit(l[2]) 

