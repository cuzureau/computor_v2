import Number
import global_variables as g

class Matrix:
	def __init__(self, value):
		# print("BIGMATRIX= ", matrix)
		self.value = value

	def __str__(self):
		# string = ''
		# print('yoo')
		# for v in self.value:
		# 	string += str(v)
		# 	string += '\n'
		# return string
		return str(self.value)

	def __repr__(self):
		return str(self)

# 	def __abs__(self):
# 		return Complex(self.real ** 2 + self.imag ** 2) ** 0.5

# 	def __gt__(self, other):
# 		self._illegal('>')

# 	def __ge__(self, other):
# 		self._illegal('>=')

# 	def __lt__(self, other):
# 		self._illegal('<')

# 	def __le__(self, other):
# 		self._illegal('<=')

# 	def _illegal(self, operator):
# 		g.prRed('Illegal operation "{}" for complex numbers'.format(operator))

# ######################### COMMUTATIVE OPERATIONS #########################

# 	def __add__(self, other):
# 		if isinstance(other, (int,float,Decimal,Number.Number)):
# 			other = Complex(other)
# 		if isinstance(other, Complex):
# 			return Complex(self.real + other.real, self.imag + other.imag)
# 		else:
# 			return None

# 	def __radd__(self, other):
# 		return self + other 

# 	def __mul__(self, other):
# 		if isinstance(other, (int,float,Decimal,Number.Number)):
# 			other = Complex(other)
# 		if isinstance(other, Complex):
# 			return Complex(self.real * other.real - self.imag * other.imag,
# 						   self.imag * other.real + self.real * other.imag)
# 		else:
# 			return None

# 	def __rmul__(self, other):
# 		return self * other

# ####################### NON COMMUTATIVE OPERATIONS #######################

# 	def __sub__(self, other):
# 		if isinstance(other, (int,float,Decimal,Number.Number)):
# 			other = Complex(other)
# 		if isinstance(other, Complex):
# 			return Complex(self.real - other.real, self.imag - other.imag)
# 		else:
# 			return None

# 	def __rsub__(self, other):
# 		return Complex(other) - self

# 	def __truediv__(self, other):
# 		if isinstance(other, (int,float,Decimal,Number.Number)):
# 			other = Complex(other)
# 		if isinstance(other, Complex):
# 			s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
# 			r = o1 ** 2 + o2 ** 2
# 			try: 
# 				return Complex((s1 * o1 + s2 * o2) / r, ( s2 * o1 - s1 * o2) / r)
# 			except ZeroDivisionError as error:
# 				g.error = str(e).capitalize()
# 				return None
# 		else:
# 			return None

# 	def __rtruediv__(self, other):
# 		return Complex(other) / self

# 	def __floordiv__(self, other):
# 		# Python does NOT accept floor division of complex numbers.
# 		# 	->	TypeError: can't take floor of complex number.
# 		# So I have implemented the Wolframalpha convention : rounding
# 		# the result of a division (both real and imaginary parts)
# 		# to the closest integer.
# 		if isinstance(other, (int,float,Decimal,Number.Number)):
# 			other = Complex(other)
# 		if isinstance(other, Complex):
# 			div = self / other
# 			if isinstance(div, Complex):
# 				if isinstance(div.real, Number.Number):
# 					div.real = round(div.real.value)
# 				else:
# 					div.real = round(div.real)
# 				if isinstance(div.imag, Number.Number):
# 					div.imag = round(div.imag.value)
# 				else:
# 					div.imag = round(div.imag)
# 				return div
# 			else:
# 				return None	
# 		else:
# 			return None

# 	def __rfloordiv__(self, other):
# 		return Complex(other) // self





# 	def __mod__(self, other):
# 		# Python does NOT accept modulo of complex numbers.
# 		# 	->	TypeError: can't mod complex numbers.
# 		# So I have implemented the Wolframalpha convention : rounding
# 		# the result of a division (both real and imaginary parts)
# 		# to 2 decimal places.
# 		if isinstance(other, (int,float,Decimal,Number.Number)):
# 			other = Complex(other)
# 		if isinstance(other, Complex):
# 			floor = self // other
# 			if isinstance(floor, Complex):
# 				ret = self - floor * other
# 				if isinstance(ret, Complex):
# 					if isinstance(ret.real, Number.Number):
# 						ret.real = round(ret.real.value, 1)
# 					else:
# 						ret.real = round(ret.real, 1)
# 					if isinstance(ret.imag, Number.Number):
# 						ret.imag = round(ret.imag.value, 1)
# 					else:
# 						ret.imag = round(ret.imag, 1)
# 					return ret
# 				else:
# 					return None
# 			else:
# 				return None
# 		else:
# 			return None

# 	def __rmod__(self, other):
# 		return Complex(other) % self

# 	def __pow__(self, other):
# 		if isinstance(other, (int,float,Decimal)):
# 			other = Number.Number(other)
# 		if isinstance(other, Number.Number):
# 			answer = 1
# 			for i in range(1, int(abs(other)) + 1): 
# 				answer = self * answer
# 			if other >= 0:
# 				return answer
# 			else:
# 				return 1 / answer
# 		else:
# 			return None

# 	def __rpow__(self, other):
# 		return Number.Number(other) ** self