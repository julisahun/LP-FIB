import os 
notes = dict(A=0, B=1, C=2, D=3, E=4, F=5, G=6)


def int2Nota(nota):
    if nota == 0: return 'A0'
    if nota == 1: return 'B0'
    octave = int(nota/7) + 1
    tone = list(notes.keys())[list(notes.values()).index(nota % 7)]
    return tone+str(octave)
