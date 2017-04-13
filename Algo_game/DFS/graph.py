
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

	def isedge(self, from_ver, to_ver):
		'''Determines whether edge exists'''

		if to_ver not in self.edges:
			return False

		if from_ver not in self.edges:
			return False

		return to_ver in self.edges[from_ver]

def loadgraph(edges):
	'''Create a graph instance'''

	g = Graph()
	for v in edges:
		g.addVertex(v)
		for neighbour in edges[v]:
			g.addEdge(v, neighbour)

	return g	

White = 0
Gray = 1
Black = 2

class DepthFirstTraversal:

	def __init__(self, graph, s):
		'''Initiate a DFS traversal of a graph'''

		self.graph = graph
		self.start = s
		self.colour = {}
		self.pred = {}

		for v in self.graph.edges:
			self.colour[v] = White
			self.pred[v] = None

		self.dfs_visits(s)

	def dfs_visits(self, u):
		'''Recursive traversal of graph using DFS'''

		self.colour[u] = Gray
		for v in self.graph.edges[u]:
			if self.colour[v] is White:
				self.pred[v] = u
				self.dfs_visits(v)

		self.colour[u] = Black

	def Solution(self, v):
		'''Recover path from start to this vertex v'''

		if v not in self.graph.edges:
			return None

		if self.pred[v] is None:
			return None

		path = [v]					
		while v != self.start:
			v = self.pred[v]
			path.insert(0, v)

		return path				

if __name__ == '__main__':
	simple = {1 : [2, 8, 6, 5], 
		      2 : [1, 3],
		      3 : [2, 4], 
		      4 : [3, 5], 
		      5 : [1, 4],
		      6 : [1, 7],
		      7 : [8, 6],
		      8 : [1, 7]}

	g = loadgraph(simple)
	# print g.edges
	# print g.isedge(1, 2)
	dfs = DepthFirstTraversal(g, 1)
	print dfs.pred
	print dfs.Solution(1)