import Matrix as M

class Error(Exception):
	def __init__(self, left, operator, right=None):
		if right is None:
			self.message = operator
		else:
			if isinstance(left, M.Matrix):
				left = '\n' + str(left)
			if isinstance(right, M.Matrix):
				right = '\n' + str(right)
			operation = str(left) + operator + str(right)
			self.message = "Illegal operation: " + operation

class Message(Exception):
	def __init__(self, message):
		self.message = message
