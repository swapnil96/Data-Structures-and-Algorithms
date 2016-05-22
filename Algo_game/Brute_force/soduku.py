import time
def Print(que):

	print '\t'
	for row in xrange(9):

		print ' '.join(map(str, que[row]))


def UsedInRow(que, row, num):

	for col in xrange(9):

		if que[row][col] == num:
			return True

	return False

def UsedInCol(que, col, num):

	for row in xrange(9):

		if que[row][col] == num:
			return True

	return False

def UsedInBox(que, BoxStartRow, BoxStartCol, num):

	for row in xrange(3):

		for col in xrange(3):

			if que[row + BoxStartRow][col + BoxStartCol] == num:
				return True

	return False

def FindUnassignedLocation(que):

	for row in xrange(9):

		for col in xrange(9):

			if que[row][col] == 0:
				return True

	return False

def FindCoor(que):

	for row in xrange(9):

		for col in xrange(9):

			if que[row][col] == 0:
				return row, col

def isSafe(que, row, col, num):

	if UsedInRow(que, row, num) is False:

		#print '1', num

		if UsedInCol(que, col, num) is False:

			#print '2'

			if UsedInBox(que, row - row%3, col - col%3, num) is False:
				
				#print '3'
				return True

def solve(que):

	if FindUnassignedLocation(que) is False:
		return True

	row, col = FindCoor(que)	
	#print row, col
	for num in xrange(1, 10):

		if isSafe(que, row, col, num):

			#print 'asdf'
			que[row][col] = num
			if solve(que):

				return True

			que[row][col] = 0		

	return False

que = [0]*9
for i in xrange(9):
	a = raw_input()
	b = map(int, a.split())
	que[i] = b
now = time.time()
if solve(que) == True:
	Print(que)
else:
	print "Wrong Input"
after = time.time()
print 'Time elapsed -', after - now