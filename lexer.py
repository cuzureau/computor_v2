from global_variables import tokens
import ply.lex as lex

t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_TIMES    = r'\*'
t_DIVIDE   = r'\/'
t_MODULO   = r'\%'
t_EQUALS   = r'\='
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_POWER    = r'\^'
t_QUESTION = r'\?'
t_NAME     = r'[a-zA-Z]{2,}|[a-hj-zA-HJ-Z]' # all names except 'i' alone
t_COMMAND  = r'![\x00-\x7F]*'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    try:
        t.value = int(t.value)
    except:
        t.value = float(t.value)
    return t

t_ignore = " \t"

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex() 