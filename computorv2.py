from global_variables import tokens
from lexer import lexer
from parser import parser

from test import add_test # to be deleted
from test import sub_test # to be deleted
from test import mul_test # to be deleted
from test import div_test # to be deleted
from test import floordiv_test # to be deleted
from test import modulo_test # to be deleted
from global_variables import prLightPurple # to be deleted
from global_variables import prGreen # to be deleted
import requests # to be deleted





for test in add_test.split(";"):
	prLightPurple(test)
	parser.parse(test)

	query = test.replace('%', 'mod').replace('+', '%2B').replace(' ', '+').replace('//', '\\')
	prGreen(query)
	response = requests.get("http://api.wolframalpha.com/v2/query?appid=4Y4WJV-P38KAYTHV8&input=" +  query + "&includepodid=Result&format=plaintext")
	# print(response.status_code)
	# print(response.text)
	try:
		print(str(response.text).split("<plaintext>")[1].split("</plaintext>")[0])
	except:
		print("bro, something went wrong")
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



