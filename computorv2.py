from global_variables import tokens
from lexer import lexer
from parser import parser






while True:
	try:
		s = raw_input('> ')
	except:
		s = input('> ')
	if s:

		# lexer.input(s)
		# while True:
		#     tok = lexer.token()
		#     if not tok: 
		#         break
		#     print(tok)



		parser.parse(s)

# [[1];[3];[5];[7];[9]]
# [[1,2];[3,4];[5,6];[7,8];[9,0]]
# [[1,2,1];[3,4,1];[5,6,1];[7,8,1];[9,0,1]]


# [[1];[2,2];[3,3,3];[4,4,4,4]]
# [[4,4,4,4];[3,3,3];[2,2];[1]]

# [[4,[1,2,3],4,4];[3,3,3];[2,2];[1]]
# [[4,4,4,4];[3,3,3];[2,2];[1,[1,2,[0,0,0],3]]]

#Error
#[1,[1,2,[0,0,0]]]


# 1
# [1]
# 1,2
# [1,2]
# 1,2,3,4,5
# [1,2,3,4,5]
# 1,2,[0,0,0],4,5
# [1,2,[0,0,0],4,5]
# [0,0,0],4,5,6
# [1,2,3,[0,0,0]]
# 1,2,3,[0,0,0]

