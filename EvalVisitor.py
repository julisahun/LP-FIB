from re import L
import os
import copy
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
import sys

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


class note:
    def __init__(self, tone, octave, duration, alteration):
        self.tone = tone
        self.octave = int(octave or '4')
        self.duration = int(duration or '4')
        self.alteration = ''
        if alteration:
            self.alteration = 'is'

    def print(self):
        print(self.duration, self.tone, self.alteration, self.octave)

    def toLilypond(self):
        return (self.tone.lower() +
                self.alteration + (
                "'" * (self.octave - 3) if self.octave > 3
                else "," * (3 - self.octave)) +
                str(self.duration))

    def increment(self, semitones):
        sus = bool(self.alteration)
        while semitones > 0:
            if self.tone == 'B' or self.tone == 'E':
                self.tone = chr(ord(self.tone) + 1)
            elif sus:
                self.tone = chr(ord(self.tone) + 1)
                sus = False
            else:
                sus = True
            if self.tone > 'G':
                self.tone = chr(ord(self.tone) - 7)
            if self.tone == 'C' and not sus:
                self.octave += 1
            semitones -= 1
        self.alteration = 'is' if sus else ''
        return self


class chord:
    def __init__(self, notes, mode):
        self.duration = notes[0].duration
        if len(notes) == 1:
            base = copy.deepcopy(notes[0])
            nota2 = copy.deepcopy(base).increment(4 if mode == 'M' else 3)
            nota3 = copy.deepcopy(nota2).increment(3 if mode == 'M' else 4)
            self.notes = [base, nota2, nota3]
        else:
            self.notes = notes

    def print(self):
        for nota in self.notes:
            nota.print()

    def toLilypond(self):
        res = "<"
        for nota in self.notes:
            res += nota.toLilypond()[:-1] + " "
        res = res[:-1] + ">" + str(self.duration)
        return res


class EvalVisitor(ExprVisitor):

    def __init__(self, method):
        self.method = method
        self.sheet = ""
        self.armadura = ""

    def getVar(self, var):
        if varsDict[len(varsDict)-1].get(var) is not None:
            return varsDict[len(varsDict)-1][var]
        else:
            raise Exception(var, "Variable not declared at this scope")

    def setVar(self, var, value):
        varsDict[len(varsDict)-1][var] = value

    def isVar(self, var):
        return varsDict[len(varsDict)-1].get(var) is not None

    def smartPrint(self, obj):
        if type(obj) == list:
            for o in obj:
                if type(o) == int:
                    print(o, end=" ")
                elif self.isVar(o):
                    print(self.getVar(o), end=" ")
                elif type(o) == note:
                    o.print()
                else:
                    print(o, end=" ")
        elif type(obj) == note or type(obj) == chord:
            obj.print()
        elif type(obj) == int or obj.isnumeric():
            print(obj, end=" ")
        elif obj[0] == '"' and obj[len(obj) - 1] == '"':
            print(obj[1:len(obj) - 1], end=" ")
        else:
            print(obj, end=" ")

    def isNote(self, nota):
        try:
            duration = ''
            indx = 0
            while nota[indx].isnumeric():
                duration += nota[indx]
                indx += 1
            if int(duration or '4') not in (1, 2, 4, 8, 16):
                return False
            tone = nota[indx]
            if tone not in notes:
                return False
            indx += 1
            alteration = ''
            while not(nota[indx].isnumeric()):
                alteration += nota[indx]
                indx += 1
            if alteration and alteration != '#':
                return False
            return int(nota[indx]) >= 0 and int(nota[indx]) <= 8 and len(nota) == indx + 1
        except IndexError:
            return True

    def isChord(self, chord):
        if chord[0] != '<' or chord[-1] != '>':
            return False
        if (chord[-2] == 'M' or chord[-2] == 'm') and self.isNote(chord[1:-2]):
            return True
        for nota in chord[1:-1].split():
            if not self.isNote(nota):
                return False
        return True

    def getNotes(self, value):
        ret = ""
        if type(value) == note:
            ret = value.toLilypond()
            return ret
        for val in value:
            ret += val.toLilypond()
            ret += ' '
        return ret

    def printSig(self):
        if self.armadura == '':
            return ''
        res = "\key "
        res += self.armadura[0].lower()
        res += ' \major' if self.armadura[1] == 'M' else ' \minor'
        res += '\n        '

        return res

    def visitMain(self, ctx):
        f = open("music.ly", "w")
        f.write(header)
        f.close()
        l = list(ctx.getChildren())
        for i in l:
            self.visit(i)
        self.visit(methDict[self.method][1])
        f = open("music.ly", "a")
        f.write(tail)
        f.close()
        os.system('lilypond music.ly')
        os.system('timidity -Ow -o music.wav music.midi')
        os.system('ffmpeg -i music.wav -codec:a libmp3lame -qscale:a 2 music.mp3')

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        return int(l[0].getText())

    def visitParaula(self, ctx):
        l = list(ctx.getChildren())
        return l[0].getText()

    def visitNota(self, ctx):
        l = list(ctx.getChildren())
        return self.getNote(l[0].getText())

    def visitSignature(self, ctx):
        l = list(ctx.getChildren())
        self.armadura = l[2].getText()

    def visitLlista(self, ctx):
        l = list(ctx.getChildren())
        ret = []
        for i in l[1:len(l)-1]:
            if i.getText().isnumeric():
                ret.append(int(i.getText()))
            elif self.isNote(i.getText()):
                ret.append(self.getNote(i.getText()))
            elif self.isChord(i.getText()):
                ret.append(self.getChord(i.getText()))
            elif self.isVar(i.getText()):
                ret.append(self.getVar(i.getText()))
            else:
                ret.append(i.getText())
        return ret

    def getNote(self, text):
        duration = ''
        octave = 4
        alteration = ''
        i = 0
        while text[i].isnumeric():
            duration += (text[i])
            i += 1
        tone = text[i]
        i += 1
        if i < len(text) and text[i] == '#':
            alteration = text[i]
            i += 1
        if (i < len(text)):
            octave = int(text[i])
        return note(tone, octave, duration, alteration)

    def getChord(self, text):
        notes = []
        for nota in text[1:-1].split():
            if nota[-1] == 'M' or nota[-1] == 'm':
                return chord([self.getNote(nota[:-1])], nota[-1])
            else:
                notes.append(self.getNote(nota))
        return chord(notes, '')

    def visitLength(self, ctx):
        l = list(ctx.getChildren())
        return len(self.getVar(l[1].getText()))

    def visitAcces(self, ctx):
        l = list(ctx.getChildren())
        array = self.getVar(l[0].getText())
        val = array[self.visit(l[2]) - 1]
        
        return val if type(val) == int or type(val) == note else self.getVar(val)

    def visitAppend(self, ctx):
        
        l = list(ctx.getChildren())
        array = self.getVar(l[0].getText())
        array.append(self.getVar(l[2].getText()) if self.isVar(l[2].getText()) else self.visit(l[2]))

    def visitCut(self, ctx):
        l = list(ctx.getChildren())
        array = self.getVar(l[1].getText())
        array.pop(self.visit(l[3]) - 1)

    def visitÑam(self, ctx):
        l = list(ctx.getChildren())
        llista = self.getVar(l[0].getText())
        for (inx, elem) in enumerate(llista):
            if elem == int(self.visit(l[2])):
                llista.pop(inx)
                return

    def visitMethod(self, ctx):
        l = list(ctx.getChildren())
        if methDict.get(l[0].getText()) is not None:
            raise Exception("funcio ja declarada")
        params = l[1:len(l) - 1]
        methDict[l[0].getText()] = [params, l[len(l)-1]]

    def visitInvoke(self, ctx):
        l = list(ctx.getChildren())
        if methDict.get(l[0].getText()) is None:
            raise Exception("la funcio no existeix")
        i = 0

        params = []
        for i in l[1:]:
            if self.isVar(i.getText()):
                params.append(self.getVar(i.getText()))
            elif self.isNote(i.getText()):
                params.append(self.getNote(i.getText()))
            elif self.isChord(i.getText()):
                params.append(self.getChord(i.getText()))
            else:
                params.append(self.visit(i))

        varsDict.append({})
        for (var,param) in zip(methDict.get(l[0].getText())[0], params):
            self.setVar(var.getText(), param)
        self.visit(methDict.get(l[0].getText())[1])
        varsDict.pop()
        
        # params = []
        # for i in l[1:]:
        #     if self.isVar(i.getText()):
        #         node = varsDict[len(varsDict)-1][i.getText()]
        #         if type(node) == list:
        #             llista = []
        #             for i in node:
        #                 llista.append(self.getVar(i) if self.isVar(i) else i)
        #             params.append(llista)
        #         else:
        #             params.append(self.getVar(node) if self.isVar(node) else node)
        #     else :
        #         params.append(self.visit(i))
        
        # varsDict.append({})
        # for (var,param) in zip(methDict.get(l[0].getText())[0], params):
        #     self.setVar(var.getText(), param)
        # self.visit(methDict.get(l[0].getText())[1])
        # varsDict.pop()

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

    def visitGreater(self, ctx):
        l = list(ctx.getChildren())
        a =  self.visit(l[0])
        b = self.visit(l[2])
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

    def visitAssign(self, ctx):
        l = list(ctx.getChildren())
        self.setVar(l[0].getText(), self.visit(l[2]))

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
        f = open("music.ly", "a")
        f.write(self.getNotes(self.visit(l[1])))
        f.close()



    def visitParentized(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[1])

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
            if l[2].getText() == '0':
                raise Exception("Can't devide by 0!")
            return int(self.visit(l[0]) / self.visit(l[2]))

    def visitPow(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) ** self.visit(l[2])

    def visitMod(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0]) % self.visit(l[2])


method = sys.argv[2] if len(sys.argv) > 2 else "Main"  
input_stream = FileStream(sys.argv[1])
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root() 

evaluator = EvalVisitor(method)
evaluator.visit(tree)
