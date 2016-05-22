'''Recursive calculation of exponent, 3 times faster than naive for loop, 2 times slower than in inbuilt ** operation'''

def exponent(x, n):
	'''Returns the value of x raised to the nth power'''

	if n == 0:
		return 1

	if n == 1:
		return x

	if n % 2:
		return x * exponent(x * x, (n-1)/2)

	return exponent(x * x, n/2)


def exponent_mod(x, n, m):
	'''Returns the value of x raised to the nth power with modulo of m, less than 2 times slower than inbuilt pow operation'''

	if n == 0:
		return 1

	if n == 1:
		return x % m

	if n % 2:
		return x * exponent_mod(x * x % m, (n-1)/2, m) % m

	return exponent_mod(x * x, n/2, m) % m


def exponent_nonr(x, n):
	'''Non-Rucursive solution of exponent, similar time as in the recursive one, even faster when last if is used'''

	if n == 0:
		return 1

	if n == 1:
		return x

	val = 1
	while n > 0:
		if n %2:
			val *= x
			n -= 1

		n /= 2
		if n > 0:
			x *= x

	return val	

'''Exponent of Matrices'''

import numpy
import random

'''900 times faster than naive multiplication'''

def random_matrix(n):
	'''Return a random nxn matrix'''

	r = []
	for i in xrange(n):
		r.append([random.random() for i in xrange(n)])

	base = numpy.array(r).reshape(n,n)
	return base

def exponent_mat(x, n):
	'''Returns the matrix n to the power n'''

	if n == 0:
		return numpy.identity(len(x))

	if n == 1:
		return x

	if n % 2:
		return x.dot(exponent_mat(x.dot(x), (n-1)/2))

	return exponent_mat(x.dot(x), n/2)

a = random_matrix(3)
print a
print exponent_mat(a, 6)










