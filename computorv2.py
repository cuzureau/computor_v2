from global_variables import tokens
from lexer import lexer
from parser import parser


while True:
    s = raw_input('> ')
    if s:

        lexer.input(s)
        while True:
            tok = lexer.token()
            if not tok: 
                break
            print(tok)

        parser.parse(s)
