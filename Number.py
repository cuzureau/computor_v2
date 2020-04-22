from decimal import *
import Complex as C
import Matrix as M
import Error as E

class Number:
	def __init__(self, number):
		getcontext().traps[Overflow]=None
		getcontext().traps[InvalidOperation]=None
		if isinstance(number, Number):
			self.value = number.value
		else:
			self.value = Decimal(number)

	def __str__(self):
		# return str(self.value.normalize())
		return str(self.value)

	def __repr__(self):
		return str(self)

	def __abs__(self):
		return Number(abs(self.value))

	def __int__(self):
		return int(self.value)

	def __bool__(self):
		if self.value == 0:
			return False
		else:
			return True

	def __lt__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	return self.value < other
		if isinstance(other, Number):
			return self.value < other.value
		else:
			raise E.Error(self, '<', other)

	# def __le__(self, other):
	# 	# if isinstance(other, (int,float,Decimal)):
	# 	# 	return self.value <= other
	# 	if isinstance(other, Number):
	# 		return self.value <= other.value
	# 	else:
			return None

	def __gt__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	return self.value > other
		if isinstance(other, Number):
			return self.value > other.value
		else:
			raise E.Error(self, '>', other)

	# def __ge__(self, other):
	# 	# if isinstance(other, (int,float,Decimal)):
	# 	# 	return self.value >= other
	# 	if isinstance(other, Number):
	# 		return self.value >= other.value
	# 	else:
	# 		return None

	# def __eq__(self, other):
	# 	# if isinstance(other, (int,float,Decimal)):
	# 	# 	return self.value == other
	# 	if isinstance(other, Number):
	# 		return (self.value == other.value)
	# 	else:
	# 		return None

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number):
			return Number(self.value + other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) + other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.rows, other.columns) + other
		else:
			raise E.Error(self, '+', other)

	# def __radd__(self, other):
	# 	return self + other

	def __mul__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number):
			return Number(self.value * other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) * other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.rows, other.columns) * other
		else:
			raise E.Error(self, '*', other)

	# def __rmul__(self, other):
	# 	return self * other

####################### NON COMMUTATIVE OPERATIONS #######################
	
	def __sub__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number):
			return Number(self.value - other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) - other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.rows, other.columns) - other
		else:
			raise E.Error(self, '-', other)

	# def __rsub__(self, other):
	# 	return Number(other) - self

	def __truediv__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number) and other.value:
			return Number(self.value / other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) / other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.rows, other.columns) / other
		else:
			raise E.Error(self, '/', other)

	# def __rtruediv__(self, other):
	# 	return Number(other) / self

	def __floordiv__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number) and other.value:
			return Number(self.value // other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) // other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.rows, other.columns) // other
		else:
			raise E.Error(self, '//', other)

	# def __rfloordiv__(self, other):
	# 	return Number(other) // self

	def __mod__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number) and other.value:
			return Number(self.value % other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) % other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.rows, other.columns) % other
		else:
			raise E.Error(self, '%', other)
		

	# def __rmod__(self, other):
	# 	return Number(other) % self

	def __pow__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = Number(other)
		if isinstance(other, Number):
			return Number(self.value ** other.value)
		else:
			raise E.Error(self, '^', other)

	# def __rpow__(self, other):
	# 	return Number(other) ** self