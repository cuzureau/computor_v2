import global_variables as g
from decimal import *
import Complex
import Matrix
import Error

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
		if isinstance(other, (int,float,Decimal)):
			return self.value < other
		elif isinstance(other, Number):
			return self.value < other.value
		else:
			return None

	def __le__(self, other):
		if isinstance(other, (int,float,Decimal)):
			return self.value <= other
		elif isinstance(other, Number):
			return self.value <= other.value
		else:
			return None

	def __gt__(self, other):
		if isinstance(other, (int,float,Decimal)):
			return self.value > other
		elif isinstance(other, Number):
			return self.value > other.value
		else:
			return None

	def __ge__(self, other):
		if isinstance(other, (int,float,Decimal)):
			return self.value >= other
		elif isinstance(other, Number):
			return self.value >= other.value
		else:
			return None

	def __eq__(self, other):
		if isinstance(other, (int,float,Decimal)):
			return self.value == other
		elif isinstance(other, Number):
			return (self.value == other.value)
		else:
			return None

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			return Number(self.value + other.value)
		elif isinstance(other, Complex.Complex):
			return Complex.Complex(self) + other
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) + other
		else:
			return None

	def __radd__(self, other):
		return self + other

	def __mul__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			return Number(self.value * other.value)
		elif isinstance(other, Complex.Complex):
			return Complex.Complex(self) * other
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) * other
		else:
			return None

	def __rmul__(self, other):
		return self * other

####################### NON COMMUTATIVE OPERATIONS #######################
	
	def __sub__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			return Number(self.value - other.value)
		elif isinstance(other, Complex.Complex):
			return Complex.Complex(self) - other
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) - other
		else:
			return None

	def __rsub__(self, other):
		return Number(other) - self

	def __truediv__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			if other.value:
				return Number(self.value / other.value)
			else:
				raise Error.Error("Division by zero")
		elif isinstance(other, Complex.Complex):
			return Complex.Complex(self) / other
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) / other
		else:
			return None

	def __rtruediv__(self, other):
		return Number(other) / self

	def __floordiv__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			if other.value:
				return Number(self.value // other.value)
			else:
				raise Error.Error("Division by zero")
		elif isinstance(other, Complex.Complex):
			return Complex.Complex(self) // other
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) // other
		else:
			return None

	def __rfloordiv__(self, other):
		return Number(other) // self

	def __mod__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			if other.value:
				return Number(self.value % other.value)
			else:
				raise Error.Error("Division by zero")
		elif isinstance(other, Complex.Complex):
			return Complex.Complex(self) % other
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) % other
		else:
			return None

	def __rmod__(self, other):
		return Number(other) % self

	def __pow__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			return Number(self.value ** other.value)
		else:
			raise Error.Error('Illegal operation between Number and {}'.format(type(other).__name__))

	def __rpow__(self, other):
		return Number(other) ** self