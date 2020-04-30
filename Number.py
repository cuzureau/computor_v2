import Complex as C
from decimal import *
import Error as E
import Matrix as M

class Number:
	def __init__(self, number):
		getcontext().traps[Overflow]=None
		getcontext().traps[InvalidOperation]=None
		if isinstance(number, Number):
			self.value = number.value
		else:
			self.value = Decimal(number)

	def __repr__(self):
		# return str(self.value.normalize())
		return str(self.value)

	def __abs__(self):
		return Number(abs(self.value))

	def __int__(self):
		return int(self.value)

	def __bool__(self):
		if self.value == 0:
			return False
		else:
			return True

	def __neg__(self):
		self.value = -self.value
		return self

	def __lt__(self, other):
		if isinstance(other, Number):
			return self.value < other.value
		else:
			raise E.Error(self, '<', other)

	def __gt__(self, other):
		if isinstance(other, Number):
			return self.value > other.value
		else:
			raise E.Error(self, '>', other)

	def __eq__(self, other):
		if isinstance(other, Number):
			return (self.value == other.value)
		else:
			raise E.Error(self, '==', other)

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		# if isinstance(other, str):
		# 	return (str(self) + '+' + other)
		if isinstance(other, Number):
			return Number(self.value + other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) + other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) + other
		else:
			raise E.Error(self, '+', other)

	# def __radd__(self, other):
	# 	if isinstance(other, str):
	# 		return (other + '+' + str(self))

	def __mul__(self, other):
		if isinstance(other, Number):
			return Number(self.value * other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) * other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) * other
		else:
			raise E.Error(self, '*', other)

####################### NON COMMUTATIVE OPERATIONS #######################
	
	def __sub__(self, other):
		if isinstance(other, Number):
			return Number(self.value - other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) - other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) - other
		else:
			raise E.Error(self, '-', other)

	def __truediv__(self, other):
		if isinstance(other, Number) and other:
			return Number(self.value / other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) / other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) / other
		else:
			raise E.Error(self, '/', other)

	def __floordiv__(self, other):
		if isinstance(other, Number) and other:
			return Number(self.value // other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) // other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) // other
		else:
			raise E.Error(self, '//', other)

	def __mod__(self, other):
		if isinstance(other, Number) and other:
			return Number(self.value % other.value)
		elif isinstance(other, C.Complex):
			return C.Complex(self) % other
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) % other
		else:
			raise E.Error(self, '%', other)
		
	def __pow__(self, other):
		if isinstance(other, Number):
			return Number(self.value ** other.value)
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) ** other
		else:
			raise E.Error(self, '^', other)