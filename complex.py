from decimal import Decimal
import Number
import Matrix
import Error
import global_variables as g

class Complex:
	def __init__(self, real, imag=0):
		self.real = Number.Number(real)
		self.imag = Number.Number(imag)

	def __str__(self):
		string = ''
		if self.real:
			# print(type(self.real), self.real)
			if self.real % 1 == 0 : self.real = int(self.real)
			string += str(self.real)
		if self.imag:
			if self.imag % 1 == 0 : self.imag = int(self.imag)
			if self.real:
				string += ' + ' if self.imag > 0 else ' - '
			else:
				string += '' if self.imag > 0 else '-'
			if abs(self.imag) != 1:
				string += str(abs(self.imag)) + 'i'
			else:
				string += 'i'
		return string or '0'

	def __repr__(self):
		return str(self)

	def __abs__(self):
		return Complex(self.real ** 2 + self.imag ** 2) ** 0.5

	def __gt__(self, other):
		raise Error.Error("TypeError: '>' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

	def __ge__(self, other):
		raise Error.Error("TypeError: '>=' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

	def __lt__(self, other):
		raise Error.Error("TypeError: '<' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

	def __le__(self, other):
		raise Error.Error("TypeError: '<=' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		if isinstance(other, (int,float,Decimal,Number.Number)):
			other = Complex(other)
		if isinstance(other, Complex):
			return Complex(self.real + other.real, self.imag + other.imag)
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) + other
		else:
			return None

	def __radd__(self, other):
		return self + other 

	def __mul__(self, other):
		if isinstance(other, (int,float,Decimal,Number.Number)):
			other = Complex(other)
		if isinstance(other, Complex):
			return Complex(self.real * other.real - self.imag * other.imag,
						   self.imag * other.real + self.real * other.imag)
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) * other
		else:
			return None

	def __rmul__(self, other):
		return self * other

####################### NON COMMUTATIVE OPERATIONS #######################

	def __sub__(self, other):
		if isinstance(other, (int,float,Decimal,Number.Number)):
			other = Complex(other)
		if isinstance(other, Complex):
			return Complex(self.real - other.real, self.imag - other.imag)
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) - other
		else:
			return None

	def __rsub__(self, other):
		return Complex(other) - self

	def __truediv__(self, other):
		if isinstance(other, (int,float,Decimal,Number.Number)):
			other = Complex(other)
		if isinstance(other, Complex):
			s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
			r = o1 ** 2 + o2 ** 2
			if r:
				return Complex((s1 * o1 + s2 * o2) / r, ( s2 * o1 - s1 * o2) / r)
			else:
				raise Error.Error("Division by zero")
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) / other
		else:
			return None

	def __rtruediv__(self, other):
		return Complex(other) / self

	def __floordiv__(self, other):
		# Python does NOT accept floor division of complex numbers.
		# 	->	TypeError: can't take floor of complex number.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to the closest integer.
		if isinstance(other, (int,float,Decimal,Number.Number)):
			other = Complex(other)
		if isinstance(other, Complex):
			div = self / other
			if isinstance(div.real, Number.Number):
				div.real = round(div.real.value)
			else:
				div.real = round(div.real)
			if isinstance(div.imag, Number.Number):
				div.imag = round(div.imag.value)
			else:
				div.imag = round(div.imag)
			return div
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) // other
		else:
			return None

	def __rfloordiv__(self, other):
		return Complex(other) // self

	def __mod__(self, other):
		# Python does NOT accept modulo of complex numbers.
		# 	->	TypeError: can't mod complex numbers.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to 2 decimal places.
		if isinstance(other, (int,float,Decimal,Number.Number)):
			other = Complex(other)
		if isinstance(other, Complex):
			floor = self // other
			ret = self - floor * other
			if isinstance(ret.real, Number.Number):
				ret.real = round(ret.real.value, 1)
			else:
				ret.real = round(ret.real, 1)
			if isinstance(ret.imag, Number.Number):
				ret.imag = round(ret.imag.value, 1)
			else:
				ret.imag = round(ret.imag, 1)
			return ret
		elif isinstance(other, Matrix.Matrix):
			return Matrix.Matrix(self, other.rows, other.columns) % other
		else:
			return None

	def __rmod__(self, other):
		return Complex(other) % self

	def __pow__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number.Number(other)
		if isinstance(other, Number.Number):
			answer = 1
			for i in range(1, int(abs(other)) + 1): 
				answer = self * answer
			if other >= 0:
				return answer
			else:
				return 1 / answer
		else:
			raise Error.Error('Illegal operation between Complex and {}'.format(type(other).__name__))

	def __rpow__(self, other):
		return Number.Number(other) ** self