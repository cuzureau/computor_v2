class Error(Exception):
	def __init__(self, left, operator, right):
		operation = "'" + str(left) + operator + str(right) + "'"
		self.message = "Illegal operation " + operation
