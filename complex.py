import Error as E
import Matrix as M
import Number as N

class Complex:
	def __init__(self, real, imag=0):
		self.real = N.Number(real)
		self.imag = N.Number(imag)

	def __str__(self):
		real = str(self.real or '')
		imag = str(abs(self.imag) or '')
		if self.imag < N.Number(0):
			if self.real:
				sign = ' - '
			else:
				sign = '-'
		elif self.imag > N.Number(0) and self.real:
			sign = ' + '
		else:
			sign = ''
		if self.imag:
			if self.imag == N.Number(1):
				imag = 'i'
			else:
				imag += 'i'
		string = real + sign + imag
		return string or '0'

	def __repr__(self):
		return str(self)

	def __bool__(self):
		if self.real:
			return True
		elif self.imag:
			return True
		else:
			return False

	# def __abs__(self):
	# 	return Complex(self.real ** N.Number(2) + self.imag ** N.Number(2)) ** N.Number(0.5)

	# def __gt__(self, other):
	# 	raise E.Error("TypeError: '>' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

	# def __ge__(self, other):
	# 	raise E.Error("TypeError: '>=' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

	# def __lt__(self, other):
	# 	raise E.Error("TypeError: '<' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

	# def __le__(self, other):
	# 	raise E.Error("TypeError: '<=' not supported between instances of 'Complex' and '{}'".format(type(other).__name__))

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex):
			return Complex(self.real + other.real, self.imag + other.imag)
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) + other
		else:
			raise E.Error(self, '+', other)

	# def __radd__(self, other):
	# 	return self + other 

	def __mul__(self, other):
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex):
			return Complex(self.real * other.real - self.imag * other.imag,
						   self.imag * other.real + self.real * other.imag)
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) * other
		else:
			raise E.Error(self, '*', other)

	# def __rmul__(self, other):
	# 	return self * other

####################### NON COMMUTATIVE OPERATIONS #######################

	def __sub__(self, other):
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex):
			return Complex(self.real - other.real, self.imag - other.imag)
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) - other
		else:
			raise E.Error(self, '-', other)

	# def __rsub__(self, other):
	# 	return Complex(other) - self

	def __truediv__(self, other):
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex) and other:
			s1, s2, o1, o2 = self.real, self.imag, other.real, other.imag
			r = o1 ** N.Number(2) + o2 ** N.Number(2)
			return Complex((s1 * o1 + s2 * o2) / r, ( s2 * o1 - s1 * o2) / r)
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) / other
		else:
			raise E.Error(self, '/', other)

	# def __rtruediv__(self, other):
	# 	return Complex(other) / self

	def __floordiv__(self, other):
		# Python does NOT accept floor division of complex numbers.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to the closest integer.
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex) and other:
			div = self / other
			# if isinstance(div.real, N.Number):
			div.real = N.Number(round(div.real.value))
			# else:
				# div.real = N.Number(round(div.real))
			# if isinstance(div.imag, N.Number):
			div.imag = N.Number(round(div.imag.value))
			# else:
				# div.imag = N.Number(round(div.imag))
			return div
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) // other
		else:
			raise E.Error(self, '//', other)

	# def __rfloordiv__(self, other):
	# 	return Complex(other) // self

	def __mod__(self, other):
		# Python does NOT accept modulo of complex numbers.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to 2 decimal places.
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex) and other:
			floor = self // other
			ret = self - floor * other
			# if isinstance(ret.real, N.Number):
			ret.real = N.Number(round(ret.real.value, 1))
			# else:
				# ret.real = N.Number(round(ret.real, 1))
			# if isinstance(ret.imag, N.Number):
			ret.imag = N.Number(round(ret.imag.value, 1))
			# else:
				# ret.imag = N.Number(round(ret.imag, 1))
			return ret
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) % other
		else:
			raise E.Error(self, '%', other)

	# def __rmod__(self, other):
	# 	return Complex(other) % self

	def __pow__(self, other):
		# if isinstance(other, (int,float,Decimal)):
		# 	other = N.Number(other)
		if isinstance(other, N.Number):
			answer = 1
			for i in range(1, int(abs(other)) + 1): 
				answer = self * answer
			if other >= 0:
				return answer
			else:
				return 1 / answer
		else:
			raise E.Error(self, '^', other)

	# def __rpow__(self, other):
	# 	return N.Number(other) ** self