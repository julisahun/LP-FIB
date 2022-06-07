SHELL = /bin/bash

all: clear compile execute

compile: Expr.jsb
	antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.jsb

compilesimple: Expr.g
	antlr4 -Dlanguage=Python3 -no-listener Expr.jsb

clear: 
	clear

ultraclean:
	bash -c $$'shopt -s extglob\n rm -rf !("EvalVisitor.py"|"code.jsb"|"Expr.jsb"|"Makefile"|"README.md")'; rm -r .vscode; rm -r .antlr

clean:
	rm *.midi *.pdf *.lily *.ly *.mp3 *.wav
	
execute: EvalVisitor.py
	python3 EvalVisitor.py code.jsb

executeMethod: EvalVisitor.py
	python3 EvalVisitor.py code.jsb Hanoi
