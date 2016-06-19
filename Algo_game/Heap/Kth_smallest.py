'''Find Kth smallest number in an array using Nlog(k) time'''

import heap

def kthSmallest(collection, k):
	'''Return Kth smallest element in collection for valid k >= 1'''

	A = collection[:k]
	heap.buildHeap(A)
	for i in xrange(k, len(collection)):
		if collection[i] < A[0]:
			A[0] = collection[i]
			heap.heapify(A, 0, k)

	return A[0]

if __name__ == '__main__':
	x = range(10000000)
	print kthSmallest(x, 10)		
