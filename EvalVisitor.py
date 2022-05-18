if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

varsDict = [{}]
methDict = {}

class EvalVisitor(ExprVisitor):


    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitLlista(self, ctx):
        l = list(ctx.getChildren())
        return list(map(lambda x: x.getText(), l[1:len(l)-1]))) 

    def visitMethod(self, ctx):
        l = list(ctx.getChildren())
        if (l[0].getText() == 'main'):
            self.visit(l[len(l)-1])
            return
        if methDict.get(l[0].getText()) is not None:
            raise Exception("funcio ja declarada")
        params = l[1:len(l) - 1]
        methDict[l[0].getText()] = [params,l[len(l)-1]]

    
    def visitInvoke(self, ctx):
        l = list(ctx.getChildren())
        if methDict.get(l[0].getText()) is None:
            raise Exception("la funcio no existeix")
        i = 0
        varsDict.append({})
        for val in methDict.get(l[0].getText())[0]:
            varsDict[len(varsDict)-1][val.getText()] = varsDict[len(varsDict)-2][l[i+1].getText()]
            i = i+1
        
        self.visit(methDict.get(l[0].getText())[1])
        varsDict.pop()
        

    def visitExecuteBody(self, ctx):
        l = list(ctx.getChildren())
        for ins in l[1:len(l)-1]:
            self.visit(ins)
        
    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        return varsDict[len(varsDict)-1][l[0].getText()]


    def visitBool(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            self.visit(l[3])

    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            self.visit(l[3])



    def visitEqual(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) == self.visit(l[2])  

    def visitNotEqual(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) != self.visit(l[2])

    def visitMore(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) > self.visit(l[2]) 

    def visitLess(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) < self.visit(l[2])        




    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        varsDict[len(varsDict)-1][l[0].getText()] = self.visit(l[2])             
    
    def visitEscriu(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[1]))
            
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
        
    def visitPow(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) ** self.visit(l[2])
