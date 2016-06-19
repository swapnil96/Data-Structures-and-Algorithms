'''Shortest path when there is weight in edges of graph'''

import sys

def allPairsShortestPath(g):
	'''Return distance structure as computed'''

	dist = {}
	pred = {}
	for u in g:
		dist[u] = {}
		pred[u] = {}
		for v in g:
			dist[u][v] = sys.maxint
			pred[u][v] = None

		dist[u][u] = 0
		for v in g[u]:
			dist[u][v] = g[u][v]
			pred[u][v] = u

	for mid in g:
		for u in g:
			for v in g:
				newlen = dist[u][mid] + dist[mid][v]
				if newlen < dist[u][v]:
					dist[u][v] = newlen
					pred[u][v] = pred[mid][v]

	return (dist, pred)

def constructShortestPath(s, t, pred):
	'''Reconstruct shortest path from s to t using information in pred'''

	path = [t]
	while t != s:
		t = pred[s][t]
		if t is None:
			return None

		path.insert(0, t)

	return path		

if __name__ == '__main__':
	graph = {0: {1: 2, 4: 4}, 
			 1: {2: 3},
			 2: {3: 5, 4: 1},
			 3: {0:8},
			 4: {3: 3}}

	dist, pred = allPairsShortestPath(graph)		 					
	print dist
	print pred
	print dist[1][3]
	print constructShortestPath(1, 3, pred)
