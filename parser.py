from global_variables import tokens
from global_variables import variables
from global_variables import prRed
from global_variables import prGreen
from global_variables import prLightPurple
import ply.yacc as yacc


class Complex(object):
	def __init__(self, real=0, imag=0):
		self.real = real
		self.imag = imag

	def __add__(self, other):
		# if isinstance(other, (float,int)):
		# 	other = Complex(other)
		return Complex(self.real + other.real,
					   self.imag + other.imag)

	def __radd__(self, other):
		return self.__add__(other) 

	def __mul__(self, other):
		# if isinstance(other, (float,int)):
		# 	other = Complex(other)
		return Complex(self.real*other.real - self.imag*other.imag,
					   self.imag*other.real + self.real*other.imag)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __sub__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return Complex(self.real - other.real,
					   self.imag - other.imag)

	def __rsub__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__sub__(self)

	def __div__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
		r = float(o1**2 + o2**2)
		try: 
			return Complex((s1*o1+s2*o2)/r, (s2*o1-s1*o2)/r)
		except ZeroDivisionError as e:
			print e
			return None

	def __rdiv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__div__(other)

	def __floordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
		r = float(o1**2 + o2**2)
		try: 
			return Complex((s1*o1+s2*o2)//r, (s2*o1-s1*o2)//r)
		except ZeroDivisionError as e:
			print e
			return None

	def __mod__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		try:
			return self - self.__floordiv__(other) * other
		except ZeroDivisionError as e:
			print e
			return None

	def __rmod__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__mod__(other)


	def __pow__(self, power):
		if power == 0:
			return 1
		elif power == 1:
			return self
		for i in range(power - 1):
			self.real *= power
			self.imag *= power
		return self


	







	# def __abs__(self):
	# 	return sqrt(self.real**2 + self.imag**2)



	def __neg__(self):   # defines -c (c is Complex)
		return Complex(-self.real, -self.imag)

	# def __eq__(self, other):
	# 	return self.real == other.real and self.imag == other.imag

	def __ne__(self, other):
		return not self.__eq__(other)

	def __str__(self):
		string = ''
		if self.real != 0:
			if self.real % 1 == 0 : self.real = int(self.real)
			string += str(self.real)
		if self.imag != 0:
			if self.imag % 1 == 0 : self.imag = int(self.imag)
			if self.real != 0:
				string += ' + ' if self.imag > 0 else ' - '
			else:
				string += '' if self.imag > 0 else '-'
			string += str(abs(self.imag)) + 'i'
		return string or '0'

	def __repr__(self):
		return 'Complex' + str(self)

	

	def _illegal(self, op):
		print 'illegal operation "%s" for complex numbers' % op



precedence = (
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE','POWER'),
	('right','UMINUS'),
	)

def p_statement_assign(t):
	'''statement : NAME EQUALS expression'''
	if type(t[3]) == tuple:
		t[3] = list(t[3])
	variables[t[1].lower()] = t[3]
	
	if type(t[3]) == list and type(t[3][0]) == list:
		for r in t[3]:
			print(str(r).replace('j', 'i'))
	else:
		print(str(t[3]).replace('j', 'i'))
	

def p_statement_expr(t):
	'''statement : expression
				 | expression EQUALS QUESTION'''
	t[1] = str(t[1]).replace('j', 'i').replace('(', '[').replace(')', ']')
	print(t[1])


def p_expression_imaginary(t):
	'''expression : NUMBER IMAGINE
				  | IMAGINE NUMBER'''
	t[0] = Complex(t[1]) * t[2]
	# compy = compy * 

def p_test3(t):
	'''expression : expression SEMICOLON expression'''
	t[0] = []
	t[0].append(t[1])
	if type(t[3][0]) == list:
		for num in t[3]:
			t[0].append(num)
	else:
		t[0].append(t[3])
	# print("({}){}   +   ({}){}".format(type(t[1]), t[1], type(t[3]), t[3]))
	# print("								==={}".format(t[0]))


def p_test2(t):
	'''expression : LBRACK expression RBRACK'''
	try:
		t[0] = list(t[2])
	except:
		t[0] = [t[2]]


def p_test(t):
	'''expression : expression COMMA expression'''
	# print("{}({}) + {}({})".format(t[1], type(t[1]), t[3], type(t[3])))
	while type(t[1]) == list:
		t[1] = t[1][0]
	t[0] = (t[1],)

	
	if type(t[3]) == tuple:
		for num in t[3]:
			t[0] += (num,)
	elif type(t[3]) == list:
		t[0] += (t[3][0],)
	else:
		t[0] += (t[3],)
	# print("========={}".format(t[0]))


def p_expression_binop(t):
	'''expression : expression PLUS expression
				  | expression MINUS expression
				  | expression TIMES expression
				  | expression DIVIDE expression
				  | expression FLOORDIV expression
				  | expression POWER expression
				  | expression MODULO expression'''

	if type(t[1]) == list:
		if type(t[3]) == int:
			if t[2] == '+'      : t[0]  = [i + t[3] for i in t[1]]
			# elif t[2] == '-'    : t[0]  = t[1] - t[3]
			# elif t[2] == '*'    : t[0]  = t[1] * t[3]
			# elif t[2] == '%'    : t[0]  = t[1] % t[3]
			# elif t[2] == '^'    : t[0]  = t[1] ** t[3]
			# elif t[2] == '/'    : t[0]  = t[1] / t[3]

		
	else:
		if t[2] == '+'      : t[0]  = t[1] + t[3]
		elif t[2] == '-'    : t[0]  = t[1] - t[3]
		elif t[2] == '*'    : t[0]  = t[1] * t[3]
		elif t[2] == '%'    : t[0]  = t[1] % t[3]
		elif t[2] == '^'    : 
			if type(t[3]) == int and t[3] >= 0:
				t[0]  = t[1] ** t[3]
			else:
				prRed("eroooooor")
		elif t[2] == '/'    : t[0]  = t[1] / t[3]
		elif t[2] == '//'   : t[0]  = t[1] // t[3]

		# if type(t[0]) != complex:
		# 	if t[0] % 1 == 0  	: t[0]  = int(t[0])
		# 	else                : t[0]  = float(t[0])


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
	try:
		t[0] = variables[t[1].lower()]
	except LookupError:
		prRed("Undefined name '%s'" % t[1])
		t[0] = 0

def p_execute_command(t):
	'statement : COMMAND'
	letter = t[1].split('!')[1]
	if letter == 'h':
		prGreen("Help:")
		print("    - !p = print all variables")
		print("    - !q = quit the computor")
	elif letter == 'p':
		if variables:
			prGreen("Variables:")
			for key,value in variables.items():
				value = str(value).replace('j', 'i')
				print("     {} = {}".format(key, value))
		else:
			prRed("Variables:")
			print("     There are no variables")
	elif letter == 'q':
		prGreen("Bye bye!")
		exit()
	else:
		print("Type '!h' for help.")


def p_error(t):
	if t:
		print("Syntax error at '%s'" % t.value)  
	else:
		print("Syntax error!")


parser = yacc.yacc()