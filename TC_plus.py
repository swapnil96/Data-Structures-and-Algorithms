import re
class QuickSums:

	def __init__(self, array, sum1):

		self.array = array
		self.sum1 = sum1

	def minSums(self):

		arr = [0]*len(array)
		mini = 15

		while(arr[len(arr)-1] != 2):
			
			arr[0] += 1

			for i in range(0, len(arr) - 1):
				
				if arr[i] == 2:
					arr[i] =  0
					arr[i+1] += 1

			newstr = ''

			for i in range(0, len(array)):

				newstr += array[i]

				if arr[i] == 1:
					newstr += '+'

			nums = re.split(r'[+]', newstr)
			sum2 = 0

			for i in range(0, len(nums)):

				if nums[i] == '':
					nums[i] = 0

				sum2 += int(nums[i])
					
			if sum1 == sum2 and len(nums) - 1 < mini:
				
				mini = len(nums) - 1	

		if mini == 15:
			print -1

		else:
			print mini			  		


array = raw_input()
s = raw_input()
sum1 = int(s)
q = QuickSums(array, sum1)
q.minSums()	