from global_variables import prRed

class Complex(object):
	def __init__(self, real, imag=0):
		self.real = real
		self.imag = imag

	def __str__(self):
		string = ''
		if self.real != 0:
			if self.real % 1 == 0 : self.real = int(self.real)
			string += str(self.real)
		if self.imag != 0:
			if self.imag % 1 == 0 : self.imag = int(self.imag)
			if self.real != 0:
				string += ' + ' if self.imag > 0 else ' - '
			else:
				string += '' if self.imag > 0 else '-'
			if abs(self.imag) != 1:
				string += str(abs(self.imag)) + 'i'
			else:
				string += 'i'
		return string or '0'

	def __repr__(self):
		return 'Complex' + str(self)

	def _illegal(self, op):
		prRed('Illegal operation "{}" for complex numbers'.format(op))

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		return Complex(self.real + other.real,
					   self.imag + other.imag)

	def __radd__(self, other):
		return self + (other) 

	def __mul__(self, other):
		return Complex(self.real * other.real - self.imag * other.imag,
					   self.imag * other.real + self.real * other.imag)

	def __rmul__(self, other):
		return self * (other)

####################### NON COMMUTATIVE OPERATIONS #######################

	def __sub__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return Complex(self.real - other.real,
					   self.imag - other.imag)

	def __rsub__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other - (self)

	def __truediv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
		r = o1 ** 2 + o2 ** 2
		try: 
			return Complex((s1 * o1 + s2 * o2) / r, ( s2 * o1 - s1 * o2) / r)
		except ZeroDivisionError as e:
			prRed(str(e).capitalize())

	def __rtruediv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other / (self)

	def __floordiv__(self, other):
		# Python does NOT accept floor division of complex numbers.
		# 	->	TypeError: can't take floor of complex number.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to the closest integer.
		if isinstance(other, (float,int)):
			other = Complex(other)
		ret = self / (other)
		if ret is not None:
			ret.real = round(ret.real)
			ret.imag = round(ret.imag)
			return ret

	def __rfloordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other // (self)

	def __mod__(self, other):
		# Python does NOT accept modulo of complex numbers.
		# 	->	TypeError: can't mod complex numbers.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to 2 decimal places.
		if isinstance(other, (float,int)):
			other = Complex(other)
		floor = self // (other)
		if floor is not None:
			ret = self - floor * other
			if ret is not None:
				ret.real = round(ret.real, 1)
				ret.imag = round(ret.imag, 1)
				return ret

	def __rmod__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other % (self)

	def __pow__(self, power):
		answer = 1
		for i in range(1, abs(power) + 1): 
			answer = self * (answer)
		if power >= 0:
			return answer
		else:
			return 1 / answer