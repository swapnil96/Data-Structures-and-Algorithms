
def is_perfect_cube(n):

	c = int(n**(1.0/3))
	return (c**3 == n) or ((c + 1)**3 == n)

def find(n):

	for i in xrange(n-1, 1, -1):
		got = 0

		for j in xrange(1, int(n**(1.0/3))):
			if j**3 >= i:
				break

			temp = i - j**3
			if is_perfect_cube(temp):
				got += 1

			if got == 3:	
				return i	

	return -1			

tt = int(raw_input())
sol = []
for i in xrange(tt):

	a = int(raw_input())
	sol.append(find(a))

for i in xrange(tt):
	
	print sol[i]	