from global_variables import tokens
import ply.lex as lex
from complex import Complex


t_FLOORDIV  = r'\/\/'
t_NAME      = r'[a-zA-Z]{2,}|[a-hj-zA-HJ-Z]'    # all words (only letters) except the word 'i' alone
t_COMMAND   = r'![\x00-\x7F]*'                  # all unicode characters after '!'

literals = '+-*/^()[]%=;,?'
t_ignore = " \t"


def t_RATIONAL(t):
	r"(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?"
	try:
		t.value = int(t.value)
	except:
		t.value = float(t.value)
	return t

def t_IMAGINE(t):
	r'i'
	t.value = Complex(0, 1)
	return t

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	
lexer = lex.lex() 