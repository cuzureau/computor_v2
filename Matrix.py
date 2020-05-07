import Number as N
import Complex as C
import Error as E

class Matrix:
	def __init__(self, value, size=(1,1)):
		if isinstance(value, list):
			self.size = (len(value), len(value[0]))
			for v in value:
				if len(v) != self.size[1]:
					raise E.Error('Error: invalid matrix')
			self.value = value
		else:
			self.size = size
			self.value = [[value for i in range(size[1])] for j in range(size[0])]
		self.simple = str(value)

	def __repr__(self):
		string = ''
		for row in self.value:
			string += str(row).replace('[', '[ ').replace(']', ' ]') + '\n'
		return string

	def __raw__(self):
		string = self.simple.replace('],', '];')
		return string

	def __neg__(self):
		return Matrix([[-i for i in j] for j in self.value])

# ######################### COMMUTATIVE OPERATIONS #########################

	def __add__(self, other):
		if isinstance(other, (N.Number,C.Complex)):
			other = Matrix(other, self.size)
		if isinstance(other, Matrix) and self.size == other.size:
			return Matrix([[s + o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '+', other)

	def __mul__(self, other):
		if isinstance(other, (N.Number,C.Complex)):
			other = Matrix(other, self.size)
		if isinstance(other, Matrix) and self.size == other.size:
			return Matrix([[s * o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '*', other)

# ####################### NON COMMUTATIVE OPERATIONS #######################

	def dot_product(self, other):
		if isinstance(other, Matrix) and self.size == other.size[::-1]:
			new = []
			for sv in self.value:
				sub = []
				for i in range(other.size[1]):
					res = [v * ov[i] for v,ov in zip(sv, other.value)]
					total = N.Number(0)
					for r in res:
						total += r
					sub.append(total)
				new.append(sub)
			return Matrix(new)
		else:
			raise E.Error(self, '**', other)

	def __sub__(self, other):
		if isinstance(other, (N.Number,C.Complex)):
			other = Matrix(other, self.size)
		if isinstance(other, Matrix) and self.size == other.size:
			return Matrix([[s - o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '-', other)

	# def check_squareness(self):
	# 	if self.size[0] != self.size[1]:
	# 		raise E.Error(self, 'Error: Matrix must be square to inverse')

	# def determinant(self, value, total=0):
	# 	V = value
	# 	indices = list(range(len(V)))
	# 	if len(V) == 2 and len(V[0]) == 2:
	# 		val = V[0][0] * V[1][1] - V[1][0] * V[0][1]
	# 		return val
	# 	for fc in indices:
	# 		V2 = V
	# 		V2 = V2[1:]
	# 		height = len(V2)
	# 		builder = 0
	# 		for i in range(height):
	# 			V2[i] = V2[i][0:fc] + V2[i][fc+1:]
	# 		sign = (-1) ** (fc % 2)
	# 		sub_det = self.determinant(V2)
	# 		total += V[0][fc] * sign * sub_det
	# 	return total

	# def check_non_singular(self):
	# 	det = self.determinant(self.value)
	# 	if det == N.Number(0):
	# 		raise E.Error(self, 'Error: Singular Matrix')

	# def identity_matrix(self, n):
	# 	new = Matrix(N.Number(0), (n, n))
	# 	for i in range(n):
	# 		new.value[i][i] = N.Number(1)
	# 	return new.value

	# def invert(self):
	# 	self.check_squareness()
	# 	self.check_non_singular()
	# 	AM = self.value
	# 	n = len(AM)
	# 	IM = self.identity_matrix(n)
	# 	indices = list(range(n))
	# 	for fd in range(n):
	# 		fdScaler = N.Number(1) / AM[fd][fd]
	# 		for j in range(n):
	# 			AM[fd][j] *= fdScaler
	# 			IM[fd][j] *= fdScaler
	# 		for i in indices[0:fd] + indices[fd+1:]: 
	# 			crScaler = AM[i][fd]
	# 			for j in range(n): 
	# 				AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
	# 				IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
	# 	return Matrix(IM)

	def __truediv__(self, other):
		new = []
		if isinstance(other, (N.Number,C.Complex)):
			for row in self.value:
				new.append([elem / other for elem in row])
			return Matrix(new)
		elif isinstance(other, Matrix):
			# try:
			# 	new = other.invert()
			# except:
			# 	raise E.Error(self, '**', other)
			# if isinstance(other, Matrix) and self.size == other.size:
			# return self.dot_product(new)
			return Matrix([[s / o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '/', other)

	def __floordiv__(self, other):
		if isinstance(other, (N.Number,C.Complex)):
			other = Matrix(other, self.size)
		if isinstance(other, Matrix) and self.size == other.size:
			return Matrix([[s // o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '//', other)

	def __mod__(self, other):
		if isinstance(other, (N.Number,C.Complex)):
			other = Matrix(other, self.size)
		if isinstance(other, Matrix) and self.size == other.size:
			return Matrix([[s % o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '%', other)
			
	def __pow__(self, other):
		if isinstance(other, N.Number):
			other = Matrix(other, self.size)
		if isinstance(other, Matrix) and self.size == other.size:
			return Matrix([[s ** o for s,o in zip(sv, ov)] for sv,ov in zip(self.value, other.value)])
		else:
			raise E.Error(self, '^', other)