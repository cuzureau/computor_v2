from global_variables import tokens
import ply.lex as lex


class Complex(object):
	def __init__(self, real=0, imag=0):
		self.real = real
		self.imag = imag

	def __add__(self, other):
		return Complex(self.real + other.real,
					   self.imag + other.imag)

	def __sub__(self, other):
		return Complex(self.real - other.real,
					   self.imag - other.imag)

	def __mul__(self, other):
		return Complex(self.real*other.real - self.imag*other.imag,
					   self.imag*other.real + self.real*other.imag)

	# def __div__(self, other):
	#     sr, si, or, oi = self.real, self.imag,\
	#                      other.real, other.imag # short forms
	#     r = float(or**2 + oi**2)
	#     return Complex((sr*or+si*oi)/r, (si*or-sr*oi)/r)

	def __abs__(self):
		return sqrt(self.real**2 + self.imag**2)

	def __neg__(self):   # defines -c (c is Complex)
		return Complex(-self.real, -self.imag)

	def __eq__(self, other):
		return self.real == other.real and self.imag == other.imag

	def __ne__(self, other):
		return not self.__eq__(other)

	def __str__(self):
		return '(%g, %g)' % (self.real, self.imag)

	def __repr__(self):
		return 'Complex' + str(self)

	def __pow__(self, power):
		raise NotImplementedError\
			  ('self**power is not yet impl. for Complex')


t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_TIMES     = r'\*'
t_DIVIDE    = r'\/'
t_MODULO    = r'\%'
t_EQUALS    = r'\='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACK    = r'\['
t_RBRACK    = r'\]'
t_SEMICOLON = r'\;'
t_COMMA    	= r'\,'
t_POWER     = r'\^'
t_QUESTION  = r'\?'
t_NAME      = r'[a-zA-Z]{2,}|[a-hj-zA-HJ-Z]'    # all words (only letters) except the word 'i' alone
t_COMMAND   = r'![\x00-\x7F]*'                  # all unicode characters after '!' 

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	try:
		t.value = int(t.value)
	except:
		t.value = float(t.value)
	return t

def t_IMAGINE(t):
	r'i'
	t.value = Complex(0, 1)
	return t

t_ignore = " \t"

def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)
	
lexer = lex.lex() 