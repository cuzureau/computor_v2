from global_variables import tokens
from lexer import lexer
from parser import parser


while True:
    s = raw_input('> ')
    if s:

        # lexer.input(s)
        # while True:
        #     tok = lexer.token()
        #     if not tok: 
        #         break
        #     print(tok)

        parser.parse(s)

# [[1];[3];[5];[7];[9]]
# [[1,2];[3,4];[5,6];[7,8];[9,0]]
# [[1,2,1];[3,4,1];[5,6,1];[7,8,1];[9,0,1]]