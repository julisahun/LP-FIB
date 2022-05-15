if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor
    


class TreeVisitor(ExprVisitor):
           
    
    def visitEscriu(self, ctx):
        l = list(ctx.getChildren())
        # print(self.visit(l[1]))

        


