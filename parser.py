from global_variables import tokens
from global_variables import variables
from global_variables import prRed
from global_variables import prGreen
from global_variables import prLightPurple
import ply.yacc as yacc


precedence = (
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE'),
	('right','UMINUS'),
	)

def p_statement_assign(t):
	'statement : NAME EQUALS expression'
	########################## to store list variables
	# try:
	# 	variables[t[1].lower()] = t[3][0]
	# 	print(t[3][0])
	# except:
	
	assignation = t[3]
	variables[t[1].lower()] = assignation
	
def p_statement_expr(t):
	'''statement : expression
				 | expression EQUALS QUESTION'''
	# try:
	#     for i in t[1]:
	#         print(i)
	# except:
	#     print(str(t[1]).replace('j', 'i'))
	
	# try:
	# 	print(t[1][0])
	# except:
	
	t[1] = str(t[1]).replace('j', 'i').replace('(', '').replace(')', '')
	print(t[1])

def p_expression_imaginary(t):
	'''expression : NUMBER IMAGINE
				  | IMAGINE NUMBER'''
	t[0] = t[1] * t[2]


def p_test3(t):
	'''expression : expression SEMICOLON expression'''
	t[0] = (t[1],) + (t[3],)
	# print("{} + {}		{}".format(t[1], t[3], t[0]))


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

	if type(t[3]) == int:
		t[0] += (t[3],)
	elif type(t[3]) == tuple:
		for num in t[3]:
			t[0] += (num,)
	elif type(t[3]) == list:
		t[0] += (t[3][0],)
	# print("========={}".format(t[0]))


def p_expression_binop(t):
	'''expression : expression PLUS expression
				  | expression MINUS expression
				  | expression TIMES expression
				  | expression DIVIDE expression
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
		elif t[2] == '^'    : t[0]  = t[1] ** t[3]
		elif t[2] == '/'    : t[0]  = t[1] / t[3]

		if type(t[0]) != complex:
			if t[0] % 1 == 0  	: t[0]  = int(t[0])
			else                : t[0]  = float(t[0])


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
				value = str(value).replace('j', 'i').replace('(', '').replace(')', '')
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