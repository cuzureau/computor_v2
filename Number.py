import global_variables as g
from decimal import Decimal
import Complex
import Error

class Number:
	def __init__(self, number):
		if isinstance(number, Number):
			self.value = number.value
		else:
			self.value = Decimal(number)

	def __str__(self):
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
		else:
			return None

	def __rsub__(self, other):
		return Number(other) - self

	def __truediv__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			try:
				return Number(self.value / other.value)
			except:
				raise Error.Error("ZeroDivisionError: division by zero")
		elif isinstance(other, Complex.Complex):
			try:
				return Complex.Complex(self) / other
			except:
				raise Error.Error("ZeroDivisionError: division by zero")
		else:
			return None

	def __rtruediv__(self, other):
		return Number(other) / self

	def __floordiv__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			try:
				return Number(self.value // other.value)
			except:
				raise Error.Error("ZeroDivisionError: integer division or modulo by zero")
		elif isinstance(other, Complex.Complex):
			try:
				return Complex.Complex(self) // other
			except:
				raise Error.Error("ZeroDivisionError: integer division or modulo by zero")
		else:
			return None

	def __rfloordiv__(self, other):
		return Number(other) // self

	def __mod__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number(other)
		if isinstance(other, Number):
			try:
				return Number(self.value % other.value)
			except:
				raise Error.Error("ZeroDivisionError: integer division or modulo by zero")
		elif isinstance(other, Complex.Complex):
			try:
				return Complex.Complex(self) % other
			except:
				raise Error.Error("ZeroDivisionError: integer division or modulo by zero")
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
			return None

	def __rpow__(self, other):
		return Number(other) ** self

