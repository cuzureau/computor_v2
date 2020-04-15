from global_variables import tokens
from global_variables import variables
from global_variables import prRed
from global_variables import prGreen
from global_variables import prLightPurple
import ply.yacc as yacc
import Complex
import Number
import Matrix
import Error
import global_variables as g

def p_operations(p): 
	""" expression : sixth
	sixth : fifth
	fifth : fourth
	fourth : third
	third : second
	second : first
	first : NUMBER
	first : IMAGINE
	"""
	p[0] = p[1]

def p_comma(p):
	""" sixth : sixth ',' fifth """
	if isinstance(p[1], list):
		p[1].append(p[3])
		p[0] = p[1]
	else:
		p[0] = [p[1],p[3]]

def p_semicolon(p):
	""" sixth : sixth ';' fifth """
	if isinstance(p[1], list):
		p[1].append(p[3])
		p[0] = p[1]
	else:
		p[0] = [p[1],p[3]]

def p_plus(p):
	""" fifth : fifth '+' fourth """
	p[0] = p[1] + p[3]

def p_minus(p):
	""" fifth : fifth '-' fourth """
	p[0] = p[1] - p[3]

def p_implicit_times(p):
	""" fourth : fourth second """
	p[0] = p[1] * p[2]

def p_times(p):
	""" fourth : fourth '*' third """
	p[0] = p[1] * p[3]

def p_divide(p):
	""" fourth : fourth '/' third """
	p[0] = p[1] / p[3]

def p_modulo(p):
	""" fourth : fourth '%' third """
	p[0] = p[1] % p[3]

def p_floor_divide(p):
	""" fourth : fourth FLOORDIV third """
	p[0] = p[1] // p[3]

def p_unary_minus(p):
	""" third : '-' third """
	if type(p[2]) == Number.Number:
		p[0] = Number.Number(-p[2].value)
	elif type(p[2]) == Complex.Complex:
		p[0] = Complex.Complex(-p[2].real, -p[2].imag)
	else:
		p[0] = -p[2]

def p_power(p):
	""" second : first '^' third """
	p[0] = p[1] ** p[3]

def p_paren(p):
	""" first : '(' expression ')' """
	p[0] = p[2]

def p_brack(p):
	""" first : '[' expression ']' """
	if type(p[2][0]) == Matrix.Matrix:
		# print('Matrix')
		p[0] = Matrix.Matrix(p[2])
	else:
		# print('Vector')
		p[0] = [p[2]]






# def p_test(p):
# 	""" expression : expression '@' expression """
	
# 	print("Addition")
# 	print ('+	', '{}+{} = '.format(p[1], p[1]), p[1] + p[1])
# 	print ('+	', '{}+{} = '.format(p[1], p[3]), p[1] + p[3])
# 	print ('+	', '{}+{} = '.format(p[3], p[1]), p[3] + p[1])
# 	print ('+	', '{}+{} = '.format(p[3], p[3]), p[3] + p[3])
# 	print ('+	', '{}+{} = '.format(p[3], 10), p[3] + 10)
# 	print ('+	', '{}+{} = '.format(10, p[3]), 10 + p[3])

# 	print("Multiplication")
# 	print ('*	', '{}*{} = '.format(p[1], p[1]), p[1] * p[1])
# 	print ('*	', '{}*{} = '.format(p[1], p[3]), p[1] * p[3])
# 	print ('*	', '{}*{} = '.format(p[3], p[1]), p[3] * p[1])
# 	print ('*	', '{}*{} = '.format(p[3], p[3]), p[3] * p[3])
# 	print ('*	', '{}*{} = '.format(p[1], 10), p[1] * 10)
# 	print ('*	', '{}*{} = '.format(10, p[1]), 10 * p[1])
# 	print ('*	', '{}*{} = '.format(p[3], 10), p[3] * 10)
# 	print ('*	', '{}*{} = '.format(10, p[3]), 10 * p[3])

# 	print("Substraction")
# 	print ('-	', '{}-{} = '.format(p[1], p[1]), p[1] - p[1])
# 	print ('-	', '{}-{} = '.format(p[1], p[3]), p[1] - p[3])
# 	print ('-	', '{}-{} = '.format(p[3], p[1]), p[3] - p[1])
# 	print ('-	', '{}-{} = '.format(p[3], p[3]), p[3] - p[3])
# 	print ('-	', '{}-{} = '.format(p[1], 10), p[1] - 10)
# 	print ('-	', '{}-{} = '.format(10, p[1]), 10 - p[1])
# 	print ('-	', '{}-{} = '.format(p[3], 10), p[3] - 10)
# 	print ('-	', '{}-{} = '.format(10, p[3]), 10 - p[3])

# 	print("Division")
# 	print ('/	', '{}/{} = '.format(p[1], p[1]), p[1] / p[1])
# 	print ('/	', '{}/{} = '.format(p[1], p[3]), p[1] / p[3])
# 	print ('/	', '{}/{} = '.format(p[3], p[1]), p[3] / p[1])
# 	print ('/	', '{}/{} = '.format(p[3], p[3]), p[3] / p[3])
# 	print ('/	', '{}/{} = '.format(p[1], 10), p[1] / 10)
# 	print ('/	', '{}/{} = '.format(10, p[1]), 10 / p[1])
# 	print ('/	', '{}/{} = '.format(p[3], 10), p[3] / 10)
# 	print ('/	', '{}/{} = '.format(10, p[3]), 10 / p[3])

# 	print("Floor Division")
# 	print ('//	', '{}//{} = '.format(p[1], p[1]), p[1] // p[1])
# 	print ('//	', '{}//{} = '.format(p[1], p[3]), p[1] // p[3])
# 	print ('//	', '{}//{} = '.format(p[3], p[1]), p[3] // p[1])
# 	print ('//	', '{}//{} = '.format(p[3], p[3]), p[3] // p[3])
# 	print ('//	', '{}//{} = '.format(p[1], 10), p[1] // 10)
# 	print ('//	', '{}//{} = '.format(10, p[1]), 10 // p[1])
# 	print ('//	', '{}//{} = '.format(p[3], 10), p[3] // 10)
# 	print ('//	', '{}//{} = '.format(10, p[3]), 10 // p[3])

# 	print("Modulo")
# 	print ('%	', '{}%{} = '.format(p[1], p[1]), p[1] % p[1])
# 	print ('%	', '{}%{} = '.format(p[1], p[3]), p[1] % p[3])
# 	print ('%	', '{}%{} = '.format(p[3], p[1]), p[3] % p[1])
# 	print ('%	', '{}%{} = '.format(p[3], p[3]), p[3] % p[3])
# 	print ('%	', '{}%{} = '.format(p[1], 10), p[1] % 10)
# 	print ('%	', '{}%{} = '.format(10, p[1]), 10 % p[1])
# 	print ('%	', '{}%{} = '.format(p[3], 10), p[3] % 10)
# 	print ('%	', '{}%{} = '.format(10, p[3]), 10 % p[3])

# 	print("Power")
# 	print ('**	', '{}**{} = '.format(p[1], p[1]), (p[1] ** p[1]))
# 	print ('**	', '{}**{} = '.format(p[1], p[3]), (p[1] ** p[3]))
# 	print ('**	', '{}**{} = '.format(p[3], p[1]), (p[3] ** p[1]))
# 	# print ('**	', '{}**{} = '.format(p[3], p[3]), (p[3] ** p[3]))
# 	print ('**	', '{}**{} = '.format(p[1], 10), (p[1] ** 10))
# 	print ('**	', '{}**{} = '.format(10, p[1]), (10 ** p[1]))
# 	print ('**	', '{}**{} = '.format(p[3], 10), (p[3] ** 10))
# 	print ('**	', '{}**{} = '.format(10, p[3]), (10 ** p[3]))

# 	print("Greater than")
# 	print ('>	', '{}>{} = '.format(p[1], p[1]), p[1] > p[1])
# 	print ('>	', '{}>{} = '.format(p[1], p[3]), p[1] > p[3])
# 	print ('>	', '{}>{} = '.format(p[3], p[1]), p[3] > p[1])
# 	print ('>	', '{}>{} = '.format(p[3], p[3]), p[3] > p[3])
# 	print ('>	', '{}>{} = '.format(p[3], 10), p[3] > 10)
# 	print ('>	', '{}>{} = '.format(10, p[3]), 10 > p[3])


















def p_statement_assign(t):
	'''expression : NAME '=' expression'''
	variables[t[1].lower()] = t[3]
	

# def p_statement_expr(t):
# 	'''statement : expression
# 				 | expression EQUALS QUESTION'''
# 	t[1] = str(t[1]).replace('j', 'i').replace('(', '[').replace(')', ']')
# 	print(t[1])

# def p_expression_name(t):
# 	'''expression : NAME
# 				  | NAME EQUALS QUESTION'''
# 	try:
# 		t[0] = variables[t[1].lower()]
# 	except LookupError:
# 		prRed("Undefined name '%s'" % t[1])
# 		t[0] = 0

def p_execute_command(t):
	''' expression : COMMAND '''
	letter = t[1].split('!')[1]
	if letter == 'h':
		prGreen("Help:")
		print("    - !p = print all variables")
		print("    - !q = quit the computor")
		print("    - !c = activate/deactivate online solver [https://www.wolframalpha.com/]")
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
	elif letter == 's':
		g.wolframalpha = not g.wolframalpha
		if g.wolframalpha is True:
			prGreen("Solver activated!")
		else:
			prRed("Solver deactivated!")
	elif letter == 'f':
		g.fraction_form = not g.fraction_form
		if g.fraction_form is True:
			prGreen("Fraction activated!")
		else:
			prRed("Fraction deactivated!")
	else:
		print("Type '!h' for help.")

def p_error(t):
	if t:
		g.prRed("Syntax error at '%s'" % t.value)  
	else:
		g.prRed("Syntax error!")


parser = yacc.yacc()