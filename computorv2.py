from global_variables import tokens
from lexer import lexer
from parser import parser

from test import add_test # to be deleted
from test import sub_test # to be deleted
from test import mul_test # to be deleted
from test import div_test # to be deleted
from test import floordiv_test # to be deleted
from test import floordiv_test_online # to be deleted
from test import modulo_test # to be deleted
from global_variables import prLightPurple # to be deleted
from global_variables import prGreen # to be deleted
from global_variables import prRed # to be deleted
import requests # to be deleted

import sys



# test = modulo_test
# for t in test.split(";"):
# 	prLightPurple(t)
# 	parser.parse(t)

# 	query = t.replace('%', 'mod').replace('+', '%2B').replace('42i // 4', 'Quotient[42i,4]').replace('4 // 42i', 'Quotient[4,42i]').replace('4 // 4', 'Quotient[4,4]').replace(' ', '+')
# 	prGreen(query)
# 	response = requests.get("http://api.wolframalpha.com/v2/query?appid=4Y4WJV-P38KAYTHV8&input=" +  query + "&includepodid=Result&format=plaintext")
# 	# print(response.status_code)
# 	# print(response.text)
# 	try:
# 		print(str(response.text).split("<plaintext>")[1].split("</plaintext>")[0])
# 	except:
# 		print("something went wrong")
# 	print("")


# for test,online in zip(floordiv_test.split(";"), floordiv_test_online.split(";")):
# 	prLightPurple(test)
# 	parser.parse(test)

# 	query = online.replace('%', 'mod').replace('+', '%2B').replace('42i // 4', 'Quotient[42i,4]').replace('4 // 42i', 'Quotient[4,42i]').replace('4 // 4', 'Quotient[4,4]').replace(' ', '+')
# 	prGreen(query)
# 	response = requests.get("http://api.wolframalpha.com/v2/query?appid=4Y4WJV-P38KAYTHV8&input=" +  query + "&includepodid=Result&format=plaintext")
# 	# print(response.status_code)
# 	# print(response.text)
# 	try:
# 		print(str(response.text).split("<plaintext>")[1].split("</plaintext>")[0])
# 	except:
# 		print("something went wrong")
# 	print("")


while True:
	try:
		s = raw_input('> ')
	except:
		s = input('> ')
	
	try:
		print(parser.parse(s))
	except EOFError:
		break
	except:
		print(sys.exc_info()[1])


	query = s.replace('%', '%25').replace('+', '%2B').replace('42i // 4', 'Quotient[42i,4]').replace('4 // 42i', 'Quotient[4,42i]').replace('4 // 4', 'Quotient[4,4]').replace(' ', '+')
	response = requests.get("http://api.wolframalpha.com/v2/query?appid=4Y4WJV-P38KAYTHV8&input=" +  query + "&includepodid=Result&format=plaintext")
	try:
		prGreen(str(response.text).split("<plaintext>")[1].split("</plaintext>")[0])
	except:
		prRed("something went wrong")



