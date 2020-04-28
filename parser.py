import Global as G
from Global import tokens
import ply.yacc as yacc
import Error as E
import Matrix as M
import Unknown as U

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
	first : variable
	first : function
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
	""" fourth : matrix DOT_PRODUCT third """
	p[0] = p[1].dot_product(p[3])

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
	p[0] = M.Matrix(p[2])








# def p_test(p):
# 	""" expression : expression '@' expression """
	

# 	print("Test Matrixes")
# 	print(M.Matrix(N.Number(0)))
# 	print(M.Matrix(N.Number(2)))
# 	print(M.Matrix(C.Complex(1)))
# 	print(M.Matrix(C.Complex(-12.3)))

# 	print(M.Matrix(N.Number(0), (2, 2)))
# 	print(M.Matrix(N.Number(2), (4, 4)))
# 	print(M.Matrix(C.Complex(1), (6, 2)))
# 	print(M.Matrix(C.Complex(-12), (2, 8)))


# 	# print("Addition")
# 	# print ('{}+{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] + p[1]))

# 	# print ('{}+{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] + p[3]))

# 	# print ('{}+{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] + p[1]))

# 	# print ('{}+{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] + p[3]))



# 	# print("Multiplication")
# 	# print ('{}*{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] * p[1]))

# 	# print ('{}*{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] * p[3]))

# 	# print ('{}*{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] * p[1]))

# 	# print ('{}*{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] * p[3]))



# 	# print("Substraction")
# 	# print ('{}-{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] - p[1]))

# 	# print ('{}-{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] - p[3]))

# 	# print ('{}-{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] - p[1]))

# 	# print ('{}-{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] - p[3]))



# 	# print("Division")
# 	# print ('{}/{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] / p[1]))

# 	# print ('{}/{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] / p[3]))

# 	# print ('{}/{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] / p[1]))

# 	# print ('{}/{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] / p[3]))



# 	# print("Floor Division")
# 	# print ('{}//{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] // p[1]))

# 	# print ('{}//{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] // p[3]))

# 	# print ('{}//{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] // p[1]))

# 	# print ('{}//{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] // p[3]))



# 	# print("Modulo")
# 	# print ('{}%{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] % p[1]))

# 	# print ('{}%{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] % p[3]))

# 	# print ('{}%{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] % p[1]))

# 	# print ('{}%{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] % p[3]))



# 	# print("Power")
# 	# print ('{}**{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] ** p[1]))

# 	# print ('{}**{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] ** p[3]))

# 	# print ('{}**{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] ** p[1]))

# 	# print ('{}**{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] ** p[3]))



# 	# print("Greater than")
# 	# print ('{}>{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] > p[1]))

# 	# print ('{}>{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] > p[3]))

# 	# print ('{}>{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] > p[1]))

# 	# print ('{}>{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] > p[3]))


# 	# print("Lower than")
# 	# print ('{}<{} = '.format(p[1], p[1]))
# 	# G.prGreen('	' + str(p[1] < p[1]))

# 	# print ('{}<{} = '.format(p[1], p[3]))
# 	# G.prGreen('	' + str(p[1] < p[3]))

# 	# print ('{}<{} = '.format(p[3], p[1]))
# 	# G.prGreen('	' + str(p[3] < p[1]))

# 	# print ('{}<{} = '.format(p[3], p[3]))
# 	# G.prGreen('	' + str(p[3] < p[3]))









# def p_equa(p):
# 	'''equation : NAME '+' expression '''
# 	print("yo")
# 	p[0] = 66










def p_function_assign(p):
	'''expression : FUNCTION '=' expression'''
	# import parser as p
	# formula = str(p[3])
	# code = p.expr(formula).compile()
	# print(code)

	eq = "3*x/2"
	ast = compile(eq)
	print(ast)
	# HERE : CHECK COMPILE FUNCTION WITH AST (DATA STRUCT FOR STORING AN EQUATION)



def p_function_expr(p):
	'''function : FUNCTION
		   		| FUNCTION '=' '?' '''
	for key in G.functions.keys():
		if p[1].casefold() == key.casefold():
			p[0] = G.functions[key]
			break
	else:
		raise E.Message("Variable '{}' not found".format(p[1]))
	



def p_variable_assign(p):
	'''expression : NAME '=' expression'''
	for key in G.variables.copy().keys():
		if p[1].casefold() == key.casefold():
			del G.variables[key]
	G.variables[p[1]] = p[3]
	p[0] = p[3]

	
def p_variable_expr(p):
	'''variable : NAME
		   		| NAME '=' '?' '''
	for key in G.variables.keys():
		if p[1].casefold() == key.casefold():
			p[0] = G.variables[key]
			break
	else:
		p[0] = U.Unknown(1, 0)
		# raise E.Message("Variable '{}' not found".format(p[1]))
		# uniquement pour :  NAME '=' '?'





def p_execute_command(t):
	''' expression : COMMAND '''
	letter = t[1].split('!')[1]
	if letter == 'h':
		prGreen("Help:")
		print("    - !p = print all variables")
		print("    - !q = quit the computor")
		print("    - !s = activate/deactivate online solver [https://www.wolframalpha.com/]")
	elif letter == 'p':
		if G.variables:
			G.prGreen("Variables:")
			for key,value in G.variables.items():
				print("     {} = {}".format(key, value))
		else:
			G.prRed("Variables:")
			print("     There are no variables")
		if G.functions:
			G.prGreen("Functions:")
			for key,value in G.functions.items():
				print("     {} = {}".format(key, value))
		else:
			G.prRed("Functions:")
			print("     There are no functions")
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