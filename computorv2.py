from global_variables import tokens
from lexer import lexer
from parser import parser

from test import add_test # to be deleted
from test import add_answer # to be deleted
from test import sub_test # to be deleted
from test import sub_answer # to be deleted
from test import mul_test # to be deleted
from test import mul_answer # to be deleted
from test import div_test # to be deleted
from test import div_answer # to be deleted
from test import floordiv_test # to be deleted
from test import floordiv_answer # to be deleted
from test import modulo_test # to be deleted
from test import modulo_answer # to be deleted
from global_variables import prLightPurple # to be deleted
from global_variables import prGreen # to be deleted




for test,answer in zip(modulo_test.split(";"), modulo_answer.split(";")):
	prLightPurple(test)
	parser.parse(test)
	prGreen(answer)
	print("")

# while True:
# 	try:
# 		s = raw_input('> ')
# 	except:
# 		s = input('> ')
# 	if s:

# 		# lexer.input(s)
# 		# while True:
# 		#     tok = lexer.token()
# 		#     if not tok: 
# 		#         break
# 		#     print(tok)


# 		parser.parse(s)



