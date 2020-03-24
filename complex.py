class Complex(object):
	def __init__(self, real, imag=0):
		self.real = real
		self.imag = imag

	def __add__(self, other):
		return Complex(self.real + other.real,
					   self.imag + other.imag)

	def __radd__(self, other):
		return self.__add__(other) 

	def __mul__(self, other):
		return Complex(self.real * other.real - self.imag * other.imag,
					   self.imag * other.real + self.real * other.imag)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __sub__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return Complex(self.real - other.real,
					   self.imag - other.imag)

	def __rsub__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__sub__(self)





	def __truediv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
		r = float(o1 ** 2 + o2 ** 2)
		try: 
			return Complex((s1 * o1 + s2 * o2) / r, ( s2 * o1 - s1 * o2) / r)
		except ZeroDivisionError as e:
			print (e)
			return None

	def __rtruediv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__truediv__(-self)





	def __floordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
		r = o1 ** 2 + o2 ** 2
		try: 
			return Complex((s1 * o1 + s2 * o2)//r, (s2 * o1 - s1 * o2) // r)
		except ZeroDivisionError as e:
			print (e)
			return None

	def __rfloordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__floordiv__(-self)

	def __mod__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return self - self.__floordiv__(other) * other

	def __rmod__(self, other):
		if isinstance(other, (float,int)):
			other = Complex(other)
		return other.__mod__(-self)

	def __pow__(self, power):
		# print(self, power)
		answer = 1
		if power >= 0:
			for i in range(1, power + 1): 
			    answer = self.__mul__(answer)
			return answer
		# else:
		# 	for i in range(power - 1):
		# 		self = self.__mul__(self)
		# return self





	# def __abs__(self):
	# 	return sqrt(self.real**2 + self.imag**2)



	def __neg__(self):   # defines -c (c is Complex)
		return Complex(-self.real, -self.imag)

	# def __eq__(self, other):
	# 	return self.real == other.real and self.imag == other.imag

	# def __ne__(self, other):
	# 	return not self.__eq__(other)

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

	# def __repr__(self):
	# 	return 'Complex' + str(self)


	def _illegal(self, op):
		print ('illegal operation "{}" for complex numbers'.format(op))


