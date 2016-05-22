'''Magic square construction, Using brute force as backtracking, not work with n = 4 as very large calculation'''

board = []
used = []
magicsum = [0]

def initialize(n):
	'''Prepare board'''

	del board[0:len(board)]
	del used[0:len(used)]
	for r in xrange(n):
		board.append([0 for c in xrange(n)])

	for d in xrange(n*n+1):
		used.append(False)

	magicsum[0] = n*(n*n+1)/2

def output():
	'''Output board''' 

	for row in board:
		for val in row:
			print ("{:2d}".format(val)),
			
		print

def isvalid(n):
	'''Determine if a board is valid'''

	sumD1 = sumD2 = 0
	for i in xrange(n):
		sumR = sumC = 0
		sumD1 += board[i][i]
		sumD2 += board[i][n-i-1]

		for j in xrange(n):
			sumR += board[i][j]
			sumC += board[j][i]

		if sumR != magicsum[0] or sumC != magicsum[0]:
			return False

	return sumD1 == magicsum[0] and sumD2 == magicsum[0]

def solve(n, step = 0):
	'''Complete given step in magic square board'''

	if step == n**2:
		return isvalid(n)

	for val in xrange(1, n**2 + 1):
		if not used[val]:
			used[val] = True
			board[step/n][step % n] = val
			if solve (n, step + 1):
				return True

			board[step/n][step % n] = 0
			used[val] = False

	return False				

'''Slight change so n = 4 can be calculated, check initially that a row is good before checking whole matrix'''

def validupto(n, step):
	'''Determine if valid so far'''

	for r in xrange(n):
		if step == (r + 1)*n - 1:
			return sum(board[r]) == magicsum[0]

	for c in xrange(n):
		if step == n*(n - 1) + c:
			total = 0
			for r in xrange(n):
				total += board[r][c]

			return total == magicsum[0]

	return True

def solveit(n, step = 0):
	'''Complete given step in magic square board'''

	if step == n**2:
		return isvalid(n)

	for val in xrange(1, n**2 + 1):
		if not used[val]:
			used[val] = True
			board[step/n][step%n] = val
			if validupto(n, step) and solveit(n, step + 1):
				return True

			board[step/n][step%n] = 0
			used[val] = False

	return False
	

initialize(3)
print used
print magicsum
output()
solve(3)
output()
print used	

initialize(4)
print used
print magicsum
output()
solveit(4)
output()
print used	