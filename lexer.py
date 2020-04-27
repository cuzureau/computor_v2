from Global import tokens
import Global as G
import ply.lex as lex
import Complex as C
import Number as N

t_FLOORDIV  	= r'\/\/'
t_DOT_PRODUCT	= r'\*\*'
t_VARIABLE     	= r'[a-zA-Z]{2,}|[a-hj-zA-HJ-Z]'    # all words (only letters) except the word 'i' alone
t_COMMAND   	= r'![\x00-\x7F]*'                  # all unicode characters after '!'

literals 	= '+-*/^()[]%=;,?@'
t_ignore 	= " \t"


def t_NUMBER(t):
	r'(?:\d+(?:\.\d*)?)'
	t.value = N.Number(t.value)
	return t

def t_IMAGINE(t):
	r'i'
	t.value = C.Complex(0, 1)
	return t

def t_error(t):
	G.prRed('Illegal character \'{}\''.format(t.value[0]))
	t.lexer.skip(1)
	
lexer = lex.lex() 