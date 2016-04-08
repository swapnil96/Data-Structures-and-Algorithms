import re

class BadNeighbors:

	def __init__(self, array):

		self.array  = array

	def which(self, x):
		
		tot = [0]*(len(array) - 1)
		tot[0] = array[x]
		
		if array[x + 1] > array[x]:
			tot[1] = array[x + 1]

		else:
			tot[1] = array[x]

		for i in range(2, len(array) - 1):

			if array[x+2] + tot[i-2] >= tot[i-1]:
				tot[i] = array[x+2] + tot[i-2]
				x += 1

			else:
				tot[i] = tot[i-1]
				x += 1

		return tot[len(array) - 2]	

	def maxDonations(self):
		
		length = len(array)
		
		if length > 2:
			print max(self.which(0), self.which(1))

		elif length == 1:
			print array[0]

		else:
			print max(array[0], array[1]) 

a = raw_input()

array1 = re.findall( r'\b\d+\b', a)

array = map(int, array1)

q = BadNeighbors(array)

q.maxDonations() 
