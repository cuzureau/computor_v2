from decimal import Decimal
import Number
import Complex
import Error
import global_variables as g

class Matrix:
	def __init__(self, value, rows=1, columns=1):
		if isinstance(value, list):
			self.columns = len(value[0])
			for v in value:
				if len(v) != self.columns:
					raise Error.Error('Error: invalid matrix dimensions')
			self.rows = len(value)
			self.value = value
		else:
			self.columns = columns
			self.rows = rows
			self.value = []
			for i in range(0, rows):
				self.value.append([value for j in range(0, columns)])
		self.dimensions = (self.rows, self.columns)

	def __str__(self):
		string = ''
		for row in self.value:
			string += str(row).replace('[', '[ ').replace(']', ' ]') + '\n'
		return string

# ######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		new = []
		if isinstance(other, (int,float,Decimal,Number.Number,Complex.Complex)):
			for row in self.value:
				new.append([elem + other for elem in row])
			return Matrix(new)
		elif isinstance(other, Matrix):
			if self.dimensions != other.dimensions:
				raise Error.Error('Error: Incompatible matrixes dimensions')
			for sv,ov in zip(self.value, other.value):
				new.append([s + o for s,o in zip(sv, ov)])
			return Matrix(new)
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))

	def __radd__(self, other):
		return self + other 

	def __mul__(self, other):
		new = []
		if isinstance(other, (int,float,Decimal,Number.Number,Complex.Complex)):
			for row in self.value:
				new.append([elem * other for elem in row])
			return Matrix(new)
		elif isinstance(other, Matrix):
			if self.dimensions != other.dimensions:
				raise Error.Error('Error: Incompatible matrixes dimensions')
			for sv,ov in zip(self.value, other.value):
				new.append([s * o for s,o in zip(sv, ov)])
			return Matrix(new)
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))
		
	def __rmul__(self, other):
		return self * other

# ####################### NON COMMUTATIVE OPERATIONS #######################

	def dot_product(self, other):
		if isinstance(other, Matrix):
			if self.dimensions == other.dimensions:
				new = []
				for sv in self.value:
					sub = []
					for i in range(other.columns):
						sub.append(sum([v * ov[i] for v,ov in zip(sv, other.value)]))
					new.append(sub)
				return Matrix(new)
			else:
				raise Error.Error('Error: Incompatible matrixes dimensions')
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))

	def __sub__(self, other):
		new = []
		if isinstance(other, (int,float,Decimal,Number.Number,Complex.Complex)):
			for row in self.value:
				new.append([elem - other for elem in row])
			return Matrix(new)
		elif isinstance(other, Matrix):
			if self.dimensions != other.dimensions:
				raise Error.Error('Error: Incompatible matrixes dimensions')
			for sv,ov in zip(self.value, other.value):
				new.append([s - o for s,o in zip(sv, ov)])
			return Matrix(new)
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))

	def __rsub__(self, other):
		return Matrix(other, self.rows, self.columns) - self

	def check_squareness(self):
		if self.rows != self.columns:
			raise Error.Error('Error: Matrix must be square to inverse')

	def determinant(self, value, total=0):
		V = value
		indices = list(range(len(V)))
		if len(V) == 2 and len(V[0]) == 2:
			val = V[0][0] * V[1][1] - V[1][0] * V[0][1]
			return val
		for fc in indices:
			V2 = V
			V2 = V2[1:]
			height = len(V2)
			builder = 0
			for i in range(height):
				V2[i] = V2[i][0:fc] + V2[i][fc+1:]
			sign = (-1) ** (fc % 2)
			sub_det = self.determinant(V2)
			total += V[0][fc] * sign * sub_det
		return total

	def check_non_singular(self):
		det = self.determinant(self.value)
		if det != 0:
			return det
		else:
			raise Error.Error('Error: Singular Matrix')

	def identity_matrix(self, n):
		new = Matrix(0, n, n)
		for i in range(n):
			new.value[i][i] = 1
		return new.value

	def invert(self):
		self.check_squareness()
		self.check_non_singular()
		AM = self.value
		n = len(AM)
		IM = self.identity_matrix(n)
		indices = list(range(n))
		for fd in range(n):
			fdScaler = 1 / AM[fd][fd]
			for j in range(n):
				AM[fd][j] *= fdScaler
				IM[fd][j] *= fdScaler
			for i in indices[0:fd] + indices[fd+1:]: 
				crScaler = AM[i][fd]
				for j in range(n): 
					AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
					IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
		return Matrix(IM)

	def __truediv__(self, other):
		new = []
		if isinstance(other, (int,float,Decimal,Number.Number,Complex.Complex)):
			for row in self.value:
				new.append([elem / other for elem in row])
			return Matrix(new)
		elif isinstance(other, Matrix):
			new = other.invert()
			return self.dot_product(new)
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))

	def __rtruediv__(self, other):
		return Matrix(other, self.rows, self.columns) / self

	def __floordiv__(self, other):
		new = []
		if isinstance(other, (int,float,Decimal,Number.Number,Complex.Complex)):
			for row in self.value:
				new.append([elem // other for elem in row])
			return Matrix(new)
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))

	def __rfloordiv__(self, other):
		return Matrix(other, self.rows, self.columns) // self


	def __mod__(self, other):
		new = []
		if isinstance(other, (int,float,Decimal,Number.Number,Complex.Complex)):
			for row in self.value:
				new.append([elem % other for elem in row])
			return Matrix(new)
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))

	def __rmod__(self, other):
		return Matrix(other, self.rows, self.columns) // self

	def __pow__(self, other):
		if isinstance(other, (int,float,Decimal)):
			other = Number.Number(other)
		if isinstance(other, Number.Number):
			if other > 0:
				answer = self
				for i in range(1, int(abs(other))):
					answer = self.dot_product(answer)
				return answer
			else:
				raise Error.Error('Error: Exponent is not a positive integer Number')
		else:
			raise Error.Error('Error: Illegal operation between Matrix and {}'.format(type(other).__name__))
			
	def __rpow__(self, other):
		return Matrix(other, self.rows, self.columns) ** self