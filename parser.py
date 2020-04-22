from Global import tokens
from Global import variables
import ply.yacc as yacc
import Complex
import Number
import Matrix
import Error
import Global as G

def p_operations(p): 
	""" expression : sixth
	sixth : fifth
	fifth : fourth
	fourth : third
	third : second
	second : first
	first : NUMBER
	first : IMAGINE
	first : matrix
	"""
	p[0] = p[1]

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

def p_dot_product(p):
	""" fourth : fourth '*' '*' matrix """
	p[0] = p[1].dot_product(p[4])

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

def p_block(p):
	""" first : '(' expression ')'
		vector : '[' value_list ']' """
	p[0] = p[2]

def p_list(p):
    """value_list : expression
       vector_list : vector
    """
    p[0] = [p[1]]

def p_list_extend(p):
    """value_list : value_list ','  expression
       vector_list : vector_list ';' vector
    """
    p[0] = p[1]
    p[0].append(p[3])

def p_matrix(p):
    """matrix : '[' vector_list ']' """
    p[0] = Matrix.Matrix(p[2])






def p_test(p):
	""" expression : expression '@' expression """
	
	print("Addition")
	print ('{}+{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] + p[1]))

	print ('{}+{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] + p[3]))

	print ('{}+{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] + p[1]))

	print ('{}+{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] + p[3]))



	print("Multiplication")
	print ('{}*{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] * p[1]))

	print ('{}*{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] * p[3]))

	print ('{}*{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] * p[1]))

	print ('{}*{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] * p[3]))



	print("Substraction")
	print ('{}-{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] - p[1]))

	print ('{}-{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] - p[3]))

	print ('{}-{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] - p[1]))

	print ('{}-{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] - p[3]))



	print("Division")
	print ('{}/{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] / p[1]))

	print ('{}/{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] / p[3]))

	print ('{}/{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] / p[1]))

	print ('{}/{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] / p[3]))



	print("Floor Division")
	print ('{}//{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] // p[1]))

	print ('{}//{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] // p[3]))

	print ('{}//{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] // p[1]))

	print ('{}//{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] // p[3]))



	print("Modulo")
	print ('{}%{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] % p[1]))

	print ('{}%{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] % p[3]))

	print ('{}%{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] % p[1]))

	print ('{}%{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] % p[3]))



	print("Power")
	print ('{}**{} = '.format(p[1], p[1]))
	G.prGreen('	' + str(p[1] ** p[1]))

	print ('{}**{} = '.format(p[1], p[3]))
	G.prGreen('	' + str(p[1] ** p[3]))

	print ('{}**{} = '.format(p[3], p[1]))
	G.prGreen('	' + str(p[3] ** p[1]))

	print ('{}**{} = '.format(p[3], p[3]))
	G.prGreen('	' + str(p[3] ** p[3]))



	# print("Greater than")
	# print ('{}>{} = '.format(p[1], p[1]))
	# G.prGreen('	' + str(p[1] > p[1]))

	# print ('{}>{} = '.format(p[1], p[3]))
	# G.prGreen('	' + str(p[1] > p[3]))

	# print ('{}>{} = '.format(p[3], p[1]))
	# G.prGreen('	' + str(p[3] > p[1]))

	# print ('{}>{} = '.format(p[3], p[3]))
	# G.prGreen('	' + str(p[3] > p[3]))


	# print("Lower than")
	# print ('{}<{} = '.format(p[1], p[1]))
	# G.prGreen('	' + str(p[1] < p[1]))

	# print ('{}<{} = '.format(p[1], p[3]))
	# G.prGreen('	' + str(p[1] < p[3]))

	# print ('{}<{} = '.format(p[3], p[1]))
	# G.prGreen('	' + str(p[3] < p[1]))

	# print ('{}<{} = '.format(p[3], p[3]))
	# G.prGreen('	' + str(p[3] < p[3]))




















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
			G.prGreen("Variables:")
			for key,value in variables.items():
				print("     {} = {}".format(key, value))
		else:
			G.prRed("Variables:")
			print("     There are no variables")
	elif letter == 'q':
		G.prGreen("Bye bye!")
		exit()
	elif letter == 's':
		G.wolframalpha = not G.wolframalpha
		if G.wolframalpha is True:
			G.prGreen("Solver activated!")
		else:
			G.prRed("Solver deactivated!")
	else:
		print("Type '!h' for help.")

def p_error(t):
	if t:
		G.prRed("Syntax error at '%s'" % t.value)  
	else:
		G.prRed("Syntax error!")


parser = yacc.yacc()