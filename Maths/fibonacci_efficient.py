
past_fib = {}

def fibonacci(n):
	'''Using recursion but storing value each time'''

	if n in past_fib:
		return past_fib[n]

	if n == 0 or n == 1:
		past_fib[n] = 1
		return 1

	total = fibonacci(n-1) + fibonacci(n - 2)
	past_fib[n] = total
	return total

print fibonacci(999)			
