all: compile execute

compile: Expr.g
	antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g

execute: script.py
	python3 script.py code.txt
