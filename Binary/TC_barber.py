
class HairCuts:

	def __init__(self, enter, exit):
		
		self.enter = enter
		self.exit = exit

	def time(self, string):
	
		h = int(string[:2])
		m = int(string[3:])
	
		if h < 9:
			h += 12

		return h*60 + m

	def loop (self, no, entr):

		free = 0
		length = len(self.enter) 

		for y in range(0,length):

			if entr[y] > free:
				free = entr[y]
	
			free += no
		
		return free 

	def maxCut ( self ):

		length = len(self.enter) 
		entr = [0]*length

		for i in range (0,length):
			entr[i] = self.time(self.enter[i])

		entr.sort()
		hi = 24*60
		lo = 5
		
		while lo < hi:

			mid = (lo + hi)/2.0

			if abs(hi - lo) <= 1e-13:
				break

			free = self.loop(mid,entr)

			if free >= self.time(self.exit):
				hi = mid
			
			else:
				lo = mid

		ret = (hi + lo)/2.0
		free1 = self.loop(mid,entr)

		if free1 > self.time(self.exit) + 1e-13 :
			print -1

		else:
			print ret			

s = raw_input()		
enter = map(str, s.split())
exit = raw_input()

y = HairCuts(enter, exit)
y.maxCut()
	