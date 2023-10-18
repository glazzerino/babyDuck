import sys
from antlr4 import *
from output.baby_duck_grammarLexer import baby_duck_grammarLexer
from output.baby_duck_grammarParser import baby_duck_grammarParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = baby_duck_grammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = baby_duck_grammarParser(stream)
    tree = parser.program()
    if tree.exception is None:
        print("No errors found")
    else:
        print("Syntax errors found")
    

if __name__ == '__main__':
    main(sys.argv)