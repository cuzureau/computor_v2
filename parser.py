import Global as G
from Global import tokens
import ply.yacc as yacc
import Error as E
import Matrix as M
import Number as N
import Unknown as U



def p_operations(p):
	""" statement : expression
	expression : fifth
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
	if isinstance(p[1], str) or isinstance(p[3], str):
		p[0] = str(p[1]) + p[2] + str(p[3])
	else:
		p[0] = p[1] + p[3]

def p_minus(p):
	""" fifth : fifth '-' fourth """
	if isinstance(p[1], str) or isinstance(p[3], str):
		p[0] = str(p[1]) + p[2] + str(p[3])
	else:
		p[0] = p[1] - p[3]

# def p_implicit_times(p):
# 	""" fourth : fourth second """
# 	print("-->p_implicit_times")
# 	p[0] = p[1] * p[2]

def p_times(p):
	""" fourth : fourth '*' third """
	if isinstance(p[1], str) or isinstance(p[3], str):
		p[0] = str(p[1]) + p[2] + str(p[3])
	else:
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








def p_statement_assign(p):
	''' statement : NAME '=' expression '''
	G.variables[p[1]] = p[3]

def p_function_assign(p):
	''' statement : NAME '(' NAME ')' '=' expression '''
	G.functions[p[1]] = (p[3], p[6])




def p_function_resolve(p):
	''' function : NAME '(' NUMBER ')' 
				 | NAME '(' IMAGINE ')'
				 | NAME '(' matrix ')' '''
	try : 
		function = G.functions.get(p[1])
		text = function[1].replace(function[0], p[3].__raw__())
		p[0] = yacc.yacc().parse(text, lexer=p.lexer.clone())
	except:
		raise E.Message("Function '{}' not found".format(p[1]))
	

def p_function_resolve_negative(p):
	''' function : NAME '(' '-' NUMBER ')' 
				 | NAME '(' '-' IMAGINE ')'
				 | NAME '(' '-' matrix ')' '''
	try : 
		function = G.functions.get(p[1])
		text = function[1].replace(function[0], p[4].__neg__().__raw__())
		p[0] = yacc.yacc().parse(text, lexer=p.lexer.clone())
	except:
		raise E.Message("Function '{}' not found".format(p[1]))
	


def p_variable_expr(p):
	''' first : NAME '''
	try : 
		p[0] = G.variables[p[1]]
	except:
		p[0] = p[1]

def p_function_expr(p):
	''' first : function '''
	try : 
		p[0] = G.functions[p[1]]
	except:
		p[0] = p[1]
		


















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
				print("     {}({}) = {}".format(key, value[0], value[1]))
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