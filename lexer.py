from global_variables import tokens
import global_variables as g
import ply.lex as lex
import Complex
import Number


t_FLOORDIV  = r'\/\/'
t_NAME      = r'[a-zA-Z]{2,}|[a-hj-zA-HJ-Z]'    # all words (only letters) except the word 'i' alone
t_COMMAND   = r'![\x00-\x7F]*'                  # all unicode characters after '!'

literals = '+-*/^()[]%=;,?@'
t_ignore = " \t"


def t_NUMBER(t):
	r'(?:\d+(?:\.\d*)?)'
	t.value = Number.Number(t.value)
	return t

def t_IMAGINE(t):
	r'i'
	t.value = Complex.Complex(0, 1)
	return t

def t_MATRIX(t):
	r'\[{2}(-?(?:\d+(?:\.\d*)?)|,|(\];\[))+\]{2}'
	print("matriiix", t.value)
	return t

def t_error(t):
	g.prRed('Illegal character \'{}\''.format(t.value[0]))
	t.lexer.skip(1)
	
lexer = lex.lex() 