import global_variables as g

class Rational(object):
	def __init__(self, numerator, denominator=1):
		try:
			numerator = int(numerator)
		except:
			numerator = float(numerator)
			numerator, denominator = numerator.as_integer_ratio()
		self.num, self.den = numerator, denominator
		# print('R(', self.num, self.den, ')')

	def __str__(self):
		if g.fraction_form == True:
			string = str(self.num)
			if self.den != 1:
				limit = self.limit_denominator()
				string += '/' + str(self.den)
				string += ' ≃ ' + str(limit.num) + '/' + str(limit.den)
		else:           
			fraction = self.num / self.den
			if fraction % 1 == 0:
				fraction = int(fraction)
			string = str(fraction)
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

# ######################### COMMUTATIVE OPERATIONS #########################

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

# ####################### NON COMMUTATIVE OPERATIONS #######################
	
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
		inverse = Rational(other.den, other.num)
		return self * inverse

	def __rtruediv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other / self

	def __floordiv__(self, other):
		if isinstance(other, (float,int)):
		  other = Rational(other)
		div = self / other
		return div.num // div.den

	def __rfloordiv__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		return other // self

	def __mod__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		div = self // other
		return self - (div * other)

	def __rmod__(self, other):
	  if isinstance(other, (float,int)):
		  other = Rational(other)
	  return other % self

	def __pow__(self, other):
		if isinstance(other, (float,int)):
			other = Rational(other)
		if other.den == 1:
			power = other.num
			if power >= 0:
				return Rational(self.num ** power, self.den ** power)
			else:
				return Rational(self.den ** -power, self.num ** -power)
		else:
			return (self.num / self.den) ** (other.num / other.den)
