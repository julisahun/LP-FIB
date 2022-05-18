all: clean compile execute

compile: Expr.g
	antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g

compilesimple: Expr.g
	antlr4 -Dlanguage=Python3 -no-listener Expr.g
clean: 
	clear
	
execute: script.py
	python3 script.py code.txt
