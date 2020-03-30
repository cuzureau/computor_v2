from global_variables import prRed
import global_variables


class Rational(object):
	def __init__(self, numerator=0, denominator=1):
		self.num = numerator
		self.den = denominator

	def __str__(self):
		string = ''
		if global_variables.irreductible == False:
			if self.num % 1 == 0:
				self.num = int(self.num)
			string += str(self.num)
			if self.den != 1:
				if self.den % 1 == 0:
					self.den = int(self.den)
				string += '/' + str(self.den)
		else:
			fraction = round(self.num / self.den, 6)
			string = str(fraction) 
		return string

	def __repr__(self):
		return 'Rational' + str(self)

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
	def greatest_common_divisor(self, a, b):
	    while b:
	        a, b = b, a % b
	    return a

	def simplify(self):
	    gcd = self.greatest_common_divisor(self.num, self.den)
	    (reduced_num, reduced_den) = (self.num / gcd, self.den / gcd)
	    return Rational(reduced_num, reduced_den)
	
	def __sub__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return Rational(self.num * other.den - other.num * self.den, self.den * other.den).simplify()

	def __rsub__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other - self

	def __truediv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		other.num, other.den = other.den, other.num

		return (self * other).simplify()


	def __rtruediv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other / self

	def __floordiv__(self, other):
		# Python does NOT accept floor division of complex numbers.
		# 	->	TypeError: can't take floor of complex number.
		# So I have implemented the Wolframalpha convention : rounding
		# the result of a division (both real and imaginary parts)
		# to the closest integer.
		if isinstance(other, (float,int)):
			other = Rational(other)
		ret = self / other
		if ret is not None:
			ret.real = round(ret.real)
			ret.imag = round(ret.imag)
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


		