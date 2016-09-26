'''link - http://www.spoj.com/problems/SEGSQRSS/'''

def shift_bit_length(x):
    return 1<<(x-1).bit_length()

class segmentTree:


	def __init__(self, n):
		self.length = 2*(shift_bit_length(n)) - 1
		self.tree = [0]*(self.length)
		#self.lazy = [0]*(self.length)

	def build(self, start, end, main, node = 0):

		if start == end:
			self.tree[node] = main[start]*main[start]

		else:
			mid = (start + end) / 2	
			self.build(start, mid, main, 2*node + 1)
			self.build(mid + 1, end, main, 2*node + 2)
			self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]
	
	def update1(self, start, end, l, r, main, val, node = 0):

		if (start > end) or (start > r) or (end < l):
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return

		if start == end:
			main[start] += val
			self.tree[node] = pow(main[start], 2)
			#print self.tree[node], start, end, l, r, node, 'qwre'
			return
		
		mid = (start + end ) / 2	
		self.update1(start, mid, l, r, main, val, 2*node + 1)
		self.update1(mid + 1, end, l, r, main, val, 2*node + 2)
		self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]
		#print self.tree[node], start, end, l, r, node, 'fuck'	

	def update2(self, start, end, l, r, main, val, node = 0):

		if (start > end) or (start > r) or (end < l):
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return

		if start == end:
			main[start] = val
			self.tree[node] = val*val
			#print self.tree[node], start, end, l, r, node, 'qkhkk', main
			return
		
		mid = (start + end ) / 2	
		self.update2(start, mid, l, r, main, val, 2*node + 1)
		self.update2(mid + 1, end, l, r, main, val, 2*node + 2)
		self.tree[node] = self.tree[2*node + 1] + self.tree[2*node + 2]

	def get(self, start, end, l, r, main, node = 0):
		
		if r < start or end < l:
			#print self.tree[node], start, end, l, r, node, 'qewr'
			return 0

		if l <= start and end <= r:
			#print self.tree[node], start, end, l, r, node, 'asdf'
			return self.tree[node]

		mid = (start + end) / 2
		p1 = self.get(start, mid, l, r, main, 2*node+1)
		p2 = self.get(mid + 1, end, l, r, main, 2*node+2)
		#print self.tree[node], start, end, l, r, node, 'bill'
		return p1 + p2

tt = long(raw_input())
temp = []
for i in xrange(tt):
	n, q = map(long, raw_input().split())
	a = map(long, raw_input().split())
	temp1 = []
	if n == 0 or q == 0:
		temp.append(temp1)
		continue

	g = segmentTree(n)
	g.build(0, n-1, a)
	for j in xrange(q):
		p = map(long, raw_input().split())
		if p[0] == 2:
			temp1.append(g.get(0, n-1, p[1]-1, p[2]-1, a))

		elif p[0] == 1:
			g.update1(0, n-1, p[1]-1, p[2]-1, a, p[3])

		else:
			g.update2(0, n-1, p[1]-1, p[2]-1, a, p[3])				

	temp.append(temp1)

for i in xrange(tt):
	
	if temp[i] == []:
		continue

	print 'Case %d:' % (i+1)
	for j in temp[i]:
		print j		

