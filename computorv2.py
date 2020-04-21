from global_variables import tokens
from lexer import lexer
from parser import parser
import global_variables as g
import wolframalpha
import readline
import Error
import signal

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
		if answer is not None:
			print(answer)
	except Error.Error as e:
		g.prRed(e.message)


	if g.wolframalpha is True and question[0] != '!':
		new = question.replace("%", " mod ")
		new = new.replace(";", ",")
		new = new.replace("[", "{")
		new = new.replace("]", "}")
		new = new.replace("**", "*")
		res = client.query(new)
		try:
			online_answer = res.details
			if 'Rational form' in online_answer and g.fraction_form == True:
				g.prGreen(res.details['Rational form'])
			elif 'Rational approximation' in online_answer and g.fraction_form == True:
				g.prGreen(res.details['Rational approximation'])
			elif 'Decimal form' in online_answer:
				g.prGreen(res.details['Decimal form'])
			elif 'Decimal approximation' in online_answer:
				g.prGreen(res.details['Decimal approximation'])
			elif 'Result' in online_answer:
				g.prGreen(res.details['Result'])
			elif 'Scientific notation' in online_answer:
				g.prGreen(res.details['Scientific notation'])
			elif 'Exact result' in online_answer:
				g.prGreen(res.details['Exact result'])
			elif 'Input' in online_answer:
				g.prGreen(res.details['Input'])
		except:
			g.prRed("No result")


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
						# 	g.prGreen(res.details['Rational form'])
						# elif 'Rational approximation' in online_answer and g.fraction_form == True:
						# 	g.prGreen(res.details['Rational approximation'])
						# elif 'Result' in online_answer:
						# 	g.prGreen(res.details['Result'])
						# elif 'Exact result' in online_answer:
						# 	g.prGreen(res.details['Exact result'])
						# elif 'Input' in online_answer:
						# 	g.prGreen(res.details['Input'])
# 					except:
# 						online_answer = "no result"

# 					my_answer = parser.parse(t)

# 					if str(my_answer).replace(' ', '') != str(online_answer).replace(' ', ''):
# 						g.prRed(">>> " + t)
# 						print(my_answer)
# 						g.prGreen(online_answer)
# 					tests_count += 1
# print(tests_count)




