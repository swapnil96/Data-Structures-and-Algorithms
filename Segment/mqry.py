'''Link - https://www.codechef.com/problems/MQRY'''
import math

class segmentTree:


	def __init__(self, n):
		self.length = 2*(2**(int(math.log(n, 2)) + 1)) - 1
		self.tree1 = [0]*(self.length)
		self.tree2 = [0]*(self.length)

	def build(self, start, end, main, node = 0):

		if start == end:
			self.tree1[node] = main[start]
			self.tree2[node] = main[start]

		else:
			mid = (start + end) / 2	
			self.build(start, mid, main, 2*node + 1)
			self.build(mid + 1, end, main, 2*node + 2)
			self.tree1[node] = max(self.tree1[2*node + 1], self.tree1[2*node + 2])
			self.tree2[node] = min(self.tree2[2*node + 1], self.tree2[2*node + 2])

	def get1(self, start, end, l, r, main, node = 0):
		
		if r < start or end < l:
			return -1

		if l <= start and end <= r:
			return self.tree1[node]

		mid = (start + end) / 2
		p1 = self.get1(start, mid, l, r, main, 2*node+1)
		p2 = self.get1(mid + 1, end, l, r, main, 2*node+2)
		return max(p1, p2)

	def get2(self, start, end, l, r, main, node = 0):
		
		if r < start or end < l:
			return 10**9+1

		if l <= start and end <= r:
			return self.tree2[node]

		mid = (start + end) / 2
		p1 = self.get2(start, mid, l, r, main, 2*node+1)
		p2 = self.get2(mid + 1, end, l, r, main, 2*node+2)
		return min(p1, p2)	

n, q = map(int, raw_input().split())
a = map(int, raw_input().split())
g = segmentTree(n)
g.build(0, n-1, a)
ans = []
#print g.tree1
#print g.tree2
for i in xrange(q):
	c, d = map(int, raw_input().split())
	ans.append(g.get1(0, n-1, c, d, a) - g.get2(0, n-1, c, d, a))

for i in xrange(q):
	print ans[i]