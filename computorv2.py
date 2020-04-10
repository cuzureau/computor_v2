from global_variables import tokens
from global_variables import prGreen
from global_variables import prRed
from lexer import lexer
from parser import parser
import sys
import global_variables as g
import wolframalpha


app_id = "9T72LH-QWT7RJHW4W"
client = wolframalpha.Client(app_id)

print("ComputorV2 [42born2code, 03/2020]")
print("Type \"!h\" for help.")
while True:
	try:
		question = raw_input('>>> ')
	except:
		question = input('>>> ')
	
	try:
		answer = parser.parse(question)
		if g.error is not "":
			g.prRed(g.error)
			g.error = ""
		elif answer is not None:
			print(answer)
	except EOFError:
		break

	if g.wolframalpha is True and question[0] != '!':
		new = question.replace("%", " mod ")
		res = client.query(new)
		try:
			online_answer = res.details
			if 'Rational form' in online_answer and g.fraction_form == True:
				prGreen(res.details['Rational form'])
			elif 'Rational approximation' in online_answer and g.fraction_form == True:
				prGreen(res.details['Rational approximation'])
			elif 'Decimal form' in online_answer:
				prGreen(res.details['Decimal form'])
			elif 'Decimal approximation' in online_answer:
				prGreen(res.details['Decimal approximation'])
			elif 'Result' in online_answer:
				prGreen(res.details['Result'])
			elif 'Scientific notation' in online_answer:
				prGreen(res.details['Scientific notation'])
			elif 'Exact result' in online_answer:
				prGreen(res.details['Exact result'])
			elif 'Input' in online_answer:
				prGreen(res.details['Input'])
		except:
			prRed("No result")



# from test import basic_tests
# from global_variables import prLightPurple
# import random


# tests_count = 0

# for operator in "+-*/":
# 	for test in basic_tests:
# 		A = random.randint(0,1000)
# 		B = random.randint(0,1000)
# 		for first in [A, -A]:
# 			for second in [B, -B]:
# 					t = test.replace('@', operator).replace('A', str(first)).replace('B', str(second))
# 					res = client.query(t)
# 					try:
# 						online_answer = res.details
						# if 'Rational form' in online_answer and g.fraction_form == True:
						# 	prGreen(res.details['Rational form'])
						# elif 'Rational approximation' in online_answer and g.fraction_form == True:
						# 	prGreen(res.details['Rational approximation'])
						# elif 'Result' in online_answer:
						# 	prGreen(res.details['Result'])
						# elif 'Exact result' in online_answer:
						# 	prGreen(res.details['Exact result'])
						# elif 'Input' in online_answer:
						# 	prGreen(res.details['Input'])
# 					except:
# 						online_answer = "no result"

# 					my_answer = parser.parse(t)

# 					if str(my_answer).replace(' ', '') != str(online_answer).replace(' ', ''):
# 						prRed(">>> " + t)
# 						print(my_answer)
# 						prGreen(online_answer)
# 					tests_count += 1
# print(tests_count)




