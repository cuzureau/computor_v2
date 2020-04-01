from global_variables import prRed
import global_variables

class Rational(object):
	def __init__(self, numerator, denominator=1):
		try:
			numerator = int(numerator)
			self.num, self.den = numerator, denominator
		except:
			self.float = numerator
			numerator = float(numerator)
			self.num, self.den = numerator.as_integer_ratio()
			limited = self.limit_denominator()
			self.num, self.den = limited.num, limited.den
		print('R(', self.num, self.den, self.float, ')')

	def __str__(self):
		string = ''
		if global_variables.irreductible == False:
			string += str(self.num)
			if self.den != 1:
				string += '/' + str(self.den)
		else:
			string = str(self.float) 
		return string

	def __repr__(self):
		return 'Rational' + str(self)

	def __abs__(self):
		return Rational(abs(self.num), self.den)

	def __le__(self, other):
		if (self.num * other.den) <= (self.den * other.num):
			return True
		else:
			return False

	def limit_denominator(self, max_denominator=1000000):
		if self.den <= max_denominator:
			return self

		p0, q0, p1, q1 = 0, 1, 1, 0
		n, d = self.num, self.den
		while True:
			a = n//d
			q2 = q0+a*q1
			if q2 > max_denominator:
				break
			p0, q0, p1, q1 = p1, q1, p0+a*p1, q2
			n, d = d, n-a*d

		k = (max_denominator-q0)//q1
		bound1 = Rational(p0+k*p1, q0+k*q1)
		bound2 = Rational(p1, q1)

		if abs(bound2 - self) <= abs(bound1 - self):
			return bound2
		else:
			return bound1
	

######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		if isinstance(other, (int, float)):
			other = Rational(other)
		return Rational(self.num * other.den + other.num * self.den, self.den * other.den)

	def __radd__(self, other):
		return self + other 

	def __mul__(self, other):
		if isinstance(other, (int, float)):
			other = Rational(other)
		return Rational(self.num * other.num, self.den * other.den)

	def __rmul__(self, other):
		return self * other

####################### NON COMMUTATIVE OPERATIONS #######################
	
	def __sub__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return Rational(self.num * other.den - other.num * self.den, self.den * other.den)

	def __rsub__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other - self

	def __truediv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		other.num, other.den = other.den, other.num
		return (self * other)

	def __rtruediv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other / self

	def __floordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)

			return ret

	def __rfloordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other // self

	def __mod__(self, other):
		# Python does NOT accept modulo of complex numbers.
		# 	->	TypeError: can't mod complex numbers.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to 2 decimal places.
		if isinstance(other, (float,int)):
			other = Rational(other)
		floor = self // other
		if floor is not None:
			ret = self - floor * other
			if ret is not None:
				ret.real = round(ret.real, 1)
				ret.imag = round(ret.imag, 1)
				return ret

	def __rmod__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other % self

	def __pow__(self, power):
		answer = 1
		for i in range(1, abs(power) + 1): 
			answer = self * answer
		if power >= 0:
			return answer
		else:
			return 1 / answer

		