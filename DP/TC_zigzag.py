class ZigZag :

	def __init__(self, array):
		self.array = array

	def longestZigZag (self):
		
		if len(array) == 1:
			return 1

		diff = [0]*len(array)

		for i in range(0, len(array)-1):
			diff[i] = array[i+1] - array[i]

		q = 0

		while q < len(array) and diff[q] ==0:
			q += 1

		fir = diff[q]
		length = 2

		for i in range(q+1, len(array)):
			if diff[i]*fir < 0:
				length += 1
				fir *= -1

		print length

a = raw_input()

array = map(int, a.split())

q = ZigZag(array)

q.longestZigZag()
