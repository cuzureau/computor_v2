import Error as E
import Matrix as M
import Number as N

class Complex:
	def __init__(self, real, imag=0):
		self.real = N.Number(real)
		self.imag = N.Number(imag)

	def __repr__(self):
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
			if self.imag == N.Number(1) or self.imag == N.Number(-1):
				imag = 'i'
			else:
				imag += 'i'
		string = real + sign + imag
		return string or '0'

	def __raw__(self):
		return self.__repr__()

	def __bool__(self):
		if self.real:
			return True
		elif self.imag:
			return True
		else:
			return False

	def __neg__(self):
		self.real = -self.real
		self.imag = -self.imag
		return self

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

	def __floordiv__(self, other):
		# Python does NOT accept floor division of complex numbers.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to the closest integer.
		if isinstance(other, N.Number):
			other = Complex(other)
		if isinstance(other, Complex) and other:
			div = self / other
			div.real = N.Number(round(div.real.value))
			div.imag = N.Number(round(div.imag.value))
			return div
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) // other
		else:
			raise E.Error(self, '//', other)

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
			ret.real = N.Number(round(ret.real.value, 1))
			ret.imag = N.Number(round(ret.imag.value, 1))
			return ret
		elif isinstance(other, M.Matrix):
			return M.Matrix(self, other.size) % other
		else:
			raise E.Error(self, '%', other)

	def __pow__(self, other):
		if isinstance(other, N.Number) and other % N.Number(1) == N.Number(0):
			answer = N.Number(1)
			for i in range(int(abs(other))):
				answer = self * answer
			if other < N.Number(0):
				return N.Number(1) / answer
			else:
				return answer
		else:
			raise E.Error(self, '^', other)