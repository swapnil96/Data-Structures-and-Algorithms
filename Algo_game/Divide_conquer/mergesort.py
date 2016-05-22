'''Best algo for Mergesort as it takes minimum space, only duplicates once the original array.'''

def mergesort(A):
	'''Merge Sort A in place'''

	copy = list(A)
	mergesort_array(copy, A, 0, len(A))

def mergesort_array(A, result, start, end):
	'''Mergesort array in memory with given range'''

	if end - start < 2:
		return 

	if end - start == 2:
		if result[start] > result[start + 1]:
			result[start],result[start + 1] = result[start + 1],result[start]

		return

	mid = (start + end)/2
	mergesort_array(result, A, start, mid)
	mergesort_array(result, A, mid, end)

	'''Merge is now ready. Merge from A back into result'''
	
	i = start
	j = mid
	idx = start
	while idx < end:
		if j >= end or (i < mid and A[i] < A[j]):
			result[idx] = A[i]
			i += 1

		else:
			result[idx] = A[j]
			j += 1

		idx += 1


x = [1, 4, 5, 2 ,6, 8, 9]
mergesort(x)
print x					
