from global_variables import tokens
from global_variables import variables
from global_variables import prRed
from global_variables import prGreen
from global_variables import prLightPurple
import ply.yacc as yacc
from complex import Complex


def p_operations(p): 
	""" expression : fifth
	fifth : fourth
	fourth : third
	third : second
	second : first
	first : RATIONAL
	first : IMAGINE
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

def p_divide(p):
	""" fourth : fourth '/' third """
	p[0] = p[1] / p[3]

def p_unary_minus(p):
	""" third : '-' second """
	p[0] = -p[2]

def p_power(p):
	""" second : first '^' second """
	print(p[1], p[2], p[3])
	p[0] = p[1] ** p[3]

def p_paren(p):
	""" first : '(' expression ')' """
	p[0] = p[2]


















# def p_statement_assign(t):
# 	'''statement : NAME EQUALS expression'''
# 	if type(t[3]) == tuple:
# 		t[3] = list(t[3])
# 	variables[t[1].lower()] = t[3]
	
# 	if type(t[3]) == list and type(t[3][0]) == list:
# 		for r in t[3]:
# 			print(str(r).replace('j', 'i'))
# 	else:
# 		print(str(t[3]).replace('j', 'i'))
	

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

# def p_execute_command(t):
# 	'''statement : expression
# 	expression : COMMAND'''
# 	letter = t[1].split('!')[1]
# 	if letter == 'h':
# 		prGreen("Help:")
# 		print("    - !p = print all variables")
# 		print("    - !q = quit the computor")
# 	elif letter == 'p':
# 		if variables:
# 			prGreen("Variables:")
# 			for key,value in variables.items():
# 				value = str(value).replace('j', 'i')
# 				print("     {} = {}".format(key, value))
# 		else:
# 			prRed("Variables:")
# 			print("     There are no variables")
# 	elif letter == 'q':
# 		prGreen("Bye bye!")
# 		exit()
# 	else:
# 		print("Type '!h' for help.")

def p_error(t):
	if t:
		print("Syntax error at '%s'" % t.value)  
	else:
		print("Syntax error!")


parser = yacc.yacc()