'''http://www.codeforces.com/problemset/problem/369/C'''

def find(path, road1):

	road2 = [0]*len(road1)
	for i in xrange(len(road)):
		road2[i] = road1[i]

	for i in xrange(len(path) - 1):
		ini = path[i]
		fin = path[i + 1]

		for j in xrange(len(road1)):
			if ((key[j] == ini and value[j] == fin) or (key[j] == fin and value[j] == ini)):
				road2[j] = 1

	return road2				
'''
def recur(path, idx, count, road1 = road):

	if idx == 1:
		return 
	count += 1
	road2 = find(path[idx][0], road1)	
	print road2
	if 2 in road2:
		recur(path, idx - 1, count, road2)

	else:
		return count 
#for i in xrange(len())
print path
count = 0
print find(path[7][0], road)
print recur(path, 2, count)
print count

'''
class Graph:

	def __init__(self):
		'''Creater an empty graph'''

		self.edges = {}

	def addVertex(self, ver):
		'''Add vertex to the graph if not already present'''

		if ver not in self.edges:
			self.edges[ver] = []

	def addEdge(self, from_ver, to_ver):
		'''Creates a road between given vertices'''

		if from_ver not in self.edges:
			self.edges[from_ver] = []

		if to_ver not in self.edges:
			self.edges[to_ver] = []

		if from_ver not in self.edges[to_ver]:
			self.edges[to_ver].append(from_ver)

		if to_ver not in self.edges[from_ver]:
			self.edges[from_ver].append(to_ver)

	def find_path(self, start, end, path = []):
		
		path = path + [start]
		if start == end:
			return path

		if not self.edges.has_key(start):
			return []

		paths = []
		for node in self.edges[start]:
			if node not in path:
				newpaths = self.find_path(node, end, path)
				for newpath in newpaths:
					paths.append(newpath)

		return paths

def u():

	got = []
	dic = {}
	ans = []
	for i in xrange(len(key)):

		temp = []
		temp1 = []
		ini = key[i]
		fin = value[i]
		if road[i] == 2:
			'''
			temp1.append(path[value[i]])
			dic[i] = temp1
			'''
			for a in path.itervalues():
				if fin in a and ini in a:
					temp.append(a)
					dic[i] = temp
		#print temp		
		for j in temp:
			idx = value.index(j[0])
			if road[idx] != 2:
				temp.remove(j)

		if len(temp) == 1:

			got += temp
			ans.append(value[i])
		
		#print temp			


	#print dic, got
	if len(got) != 0:
		for i in dic.keys():
			for k in dic[i]:
				if k in got:
					dic.pop(i)
					break

		if len(dic) == 0:
			print len(ans)
			print ' '.join(map(str, ans))			

	else:
		li = []
		for k in dic.keys():
			li.append(value[k])
		
		print len(dic)
		print ' '.join(map(str, li))  		

a = int(raw_input())
key = []
value = []
road = []
for i in xrange(a-1):
	r = raw_input()
	rr = map(int, r.split())
	key.append(rr[0])
	value.append(rr[1])
	road.append(rr[2])

g = Graph()
i = 0
path = {}

for v in key:
	g.addVertex(v)
	g.addEdge(v, value[i])
	i += 1

for i in g.edges.keys():
	if i == 1:
		continue

	else:
		path[i] = g.find_path(i, 1)
		#print find(path[i], road)

u()