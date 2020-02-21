from global_variables import tokens
from global_variables import variables
from global_variables import prRed
from global_variables import prGreen
from global_variables import prLightPurple
import ply.yacc as yacc


precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    print("assign")
    variables[t[1].lower()] = t[3]
    print(t[3])

def p_statement_expr(t):
    '''statement : expression
                 | expression EQUALS QUESTION'''
    print(t[1])

# def p_expression_binop_imagine(t):
#     '''expression : NUMBER TIMES IMAGINE
#                   | IMAGINE TIMES NUMBER
#                   | NUMBER IMAGINE
#                   | IMAGINE NUMBER'''
#     print("binop_imagine")
#     count = (len(t) - 1)
#     if count == 3:
#         if t[1] == 'i' : t[0] = str(t[3]) + 'i'
#         else : t[0] = str(t[1]) + 'i'
#     else:
#         if t[1] == 'i' : t[0] = str(t[2]) + 'i'
#         else : t[0] = str(t[1]) + 'i'
#     if t[2] == '+'  : t[0] = t[1] + t[3]
#     elif t[2] == '-': t[0] = t[1] - t[3]
#     elif t[2] == '*': t[0] = t[1] * t[3]
#     elif t[2] == '%': t[0] = t[1] % t[3]
#     elif t[2] == '^': t[0] = t[1] ** t[3]
#     elif t[2] == '/': t[0] = float(t[1]) / float(t[3])

    # if t[0] % 1 == 0:
    #     t[0] = int(t[0])
    # else:
    #     t[0] = float(t[0])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression
                  | expression MODULO expression'''
    print("binop_reals")
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '%': t[0] = t[1] % t[3]
    elif t[2] == '^': t[0] = t[1] ** t[3]
    elif t[2] == '/': t[0] = float(t[1]) / float(t[3])

    if t[0] % 1 == 0:
        t[0] = int(t[0])
    else:
        t[0] = float(t[0])


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    '''expression : NUMBER
                  | IMAGINE'''
    t[0] = t[1]

def p_expression_name(t):
    '''expression : NAME
                  | NAME EQUALS QUESTION'''
    print("solve name")
    try:
        t[0] = variables[t[1].lower()]
    except LookupError:
        prRed("Undefined name '%s'" % t[1])
        t[0] = 0

def p_execute_command(t):
    'statement : COMMAND'
    letter = t[1].split('!')[1]
    if letter == '':
        print("Type '!h' for help.")
    elif letter == 'h':
        prGreen("Help:")
        print("    - !p = print all variables")
        print("    - !q = quit the computor")
    elif letter == 'p':
        if variables:
            prGreen("Variables:")
            for key,value in variables.items():
                print("     {} = {}".format(key, value))
        else:
            prRed("Variables:")
            print("     There are no variables")
    elif letter == 'q':
        prGreen("Bye bye!")
        exit()


def p_error(t):
    if t:
        print("Syntax error at '%s'" % t.value)  
    else:
        print("Syntax error!")


parser = yacc.yacc()