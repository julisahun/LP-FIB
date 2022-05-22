from re import L
import os
import functools


if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor

varsDict = [{}]
methDict = {}
notes = dict(A=0, B=1, C=2, D=3, E=4, F=5, G=6)
header = "\x5c\x76\x65\x72\x73\x69\x6f\x6e\x20\x22\x32\x2e\x32\x32\x2e\x31\x22\x0a\x5c\x73\x63\x6f\x72\x65\x20\x7b\x0a\x20\x20\x20\x20\x5c\x61\x62\x73\x6f\x6c\x75\x74\x65\x20\x7b\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x5c\x74\x65\x6d\x70\x6f\x20\x34\x20\x3d\x20\x31\x32\x30\x0a\x20\x20\x20\x20\x20\x20\x20\x20"
tail = "\x0a\x20\x20\x20\x20\x7d\x0a\x20\x20\x20\x20\x5c\x6c\x61\x79\x6f\x75\x74\x20\x7b\x20\x7d\x0a\x20\x20\x20\x20\x5c\x6d\x69\x64\x69\x20\x7b\x20\x7d\x0a\x7d"

class EvalVisitor(ExprVisitor):
    sheet = ""

    def getVar(self, var):
        # print("getting variable " + var)
        if varsDict[len(varsDict)-1].get(var) is not None:
            return varsDict[len(varsDict)-1][var]
        else:
            raise Exception("Variable not declared at this scope")

    def setVar(self, var, value):
        # print("Setting variable", var, " to ", value)
        varsDict[len(varsDict)-1][var] = value

    def isVar(self, var):
        return varsDict[len(varsDict)-1].get(var) is not None

    def smartPrint(self, obj):
        if type(obj) == list:
            for o in obj:
                if type(o) == int:
                    print(o, end =" ")
                elif self.isVar(o):
                    print(self.getVar(o), end =" ")
                else:
                    print(o, end =" ")

        elif type(obj) == int or obj.isnumeric():
            print(obj, end =" ")
        elif obj[0] == '"' and obj[len(obj) - 1] == '"':
            print(obj[1:len(obj)-1],end = " ")
        else:
            print(obj, end = " ")

    def nota2Int(self, nota):
        if len(nota) == 1:
             nota.append(4)
        if nota == 'A0': return 0
        if nota == 'B0': return 1
        return notes[nota[0]]+7*(int(nota[1])-1)

    def int2Nota(self, nota):
        if nota == 0: return 'A0'
        if nota == 1: return 'B0'
        octave = int(nota/7) + 1
        tone = list(notes.keys())[list(notes.values()).index(nota % 7)]
        return tone+str(octave)

    def nota2lilypond(self, nota):
        n = str(nota[0]).lower()
        if len(nota) == 1: return n
        i = int(nota[1])
        while i < 3:
            n += ","
            i += 1
        while i > 3:
            n += "'"
            i -= 1
        return str(n + "4")

    
    def isNote(self, nota):
        return (len(nota) > 0 and str(nota[0]) >= 'A' and str(nota[0]) <= 'G') and (len(nota) == 1 or (len(nota) == 2 and int(nota[1]) >= 0 and int(nota[1]) <= 8))

    def getNotes(self, value):
        ret = ""
        for val in value:
            ret += self.nota2lilypond(self.int2Nota(val))
            ret += ' '
        return ret
        

    def visitMain(self, ctx):
        l = list(ctx.getChildren())
        for i in l:
            self.visit(i)
        self.visit(methDict['Main'][1])


    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitParaula(self, ctx):
        l = list(ctx.getChildren())
        return l[0].getText()

    def visitNota(self, ctx):
        return self.nota2Int(list(ctx.getChildren())[0].getText())

    def visitLlista(self, ctx):
        l = list(ctx.getChildren())
        ret = []
        for i in l[1:len(l)-1]:
            if i.getText().isnumeric():
                ret.append(int(i.getText()))
            elif self.isNote(i.getText()):
                ret.append(self.nota2Int(i.getText()))
            else:
                ret.append(i.getText())
        return ret

    def visitLength(self, ctx):
        l = list(ctx.getChildren())
        return len(self.getVar(l[1].getText()))

    def visitAcces(self, ctx):
        l = list(ctx.getChildren())
        array = self.getVar(l[0].getText())
        val = array[self.visit(l[2])- 1]
        return  val if type(val) == int else self.getVar(val)

    def visitAppend(self, ctx):
        l = list(ctx.getChildren())
        array = self.getVar(l[0].getText())
        array.append(l[2].getText() if self.isVar(l[2].getText()) else self.visit(l[2]))
        self.setVar(l[0].getText(), array)
        
    def visitCut(self, ctx):
        l = list(ctx.getChildren())
        array = self.getVar(l[0].getText())
        array.pop(self.visit(l[2]) - 1)
        self.setVar(l[0].getText(), array)


    def visitMethod(self, ctx):
        l = list(ctx.getChildren())
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
            self.setVar(val.getText(), varsDict[len(varsDict)-2][l[i+1].getText()])
            i = i+1
        
        self.visit(methDict.get(l[0].getText())[1])
        varsDict.pop()

    def visitExecuteBody(self, ctx):
        l = list(ctx.getChildren())
        for ins in l[1:len(l)-1]:
            self.visit(ins)
        
    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        return self.getVar(l[0].getText())


    def visitIf(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            self.visit(l[2])
    
    def visitElseIf(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]):
            self.visit(l[2])
        else:
            self.visit(l[4])

    def visitWhile(self, ctx):
        l = list(ctx.getChildren())
        while self.visit(l[1]):
            self.visit(l[2])



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

    def visitGreaterEqual(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) >= self.visit(l[2]) 

    def visitLessEqual(self, ctx): 
        l = list(ctx.getChildren())
        return self.visit(l[0]) <= self.visit(l[2])



    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        self.setVar(l[0].getText(),self.visit(l[2]))
    
    def visitEscriu(self, ctx):
        
        l = list(ctx.getChildren())
        for i in l[1:]:
            self.smartPrint(self.visit(i))
        print()

    def visitLlegeix(self, ctx):
        l = list(ctx.getChildren())
        var = input()
        self.setVar(l[1].getText(), int(var) if var.isnumeric() else var)

    def visitPlay(self, ctx):
        l = list(ctx.getChildren())
        f = open("music.ly", "w", encoding="utf-8")   
        f.write(header + self.getNotes(self.visit(l[1])) + tail)
        f.close()
        os.system('lilypond music.ly')
        os.system('timidity -Ow -o music.wav music.midi')
        os.system('ffmpeg -i music.wav -codec:a libmp3lame -qscale:a 2 music.mp3')



            
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
