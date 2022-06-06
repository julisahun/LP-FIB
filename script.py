from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
import sys

method = sys.argv[2] if len(sys.argv) > 2 else "Main"  
input_stream = FileStream(sys.argv[1])
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root() 

evaluator = EvalVisitor(method)
evaluator.visit(tree)
