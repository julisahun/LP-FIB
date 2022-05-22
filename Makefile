SHELL = /bin/bash

all: clear compile execute

compile: Expr.g
	antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g

compilesimple: Expr.g
	antlr4 -Dlanguage=Python3 -no-listener Expr.g
clear: 
	clear

ultraclean:
	bash -c $$'shopt -s extglob\n rm -rf !("EvalVisitor.py"|"code.txt"|"Expr.g"|"Makefile"|"README.md"|"script.py")'; rm -r .vscode; rm -r .antlr

clean:
	rm *.midi *.pdf *.lily *.ly *.mp3 *.wav
	
execute: script.py
	python3 script.py code.txt
