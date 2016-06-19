# Single source shortest path

import Binary_heap
import sys

def singleSourceShortestPath(graph, s):
	''' Compute and return (dist, pred) matrices of computation'''

	pq = Binary_heap.BHeap(len(graph))
	dist = {}
	pred = {}
	for v in graph:
		dist[v] = sys.maxint
		pred[v] = None

	dist[s] = 0
	for v in graph:
		pq.insert(v, dist[v])

	while not pq.isEmpty():
		u = pq.smallest()
		for v in graph[u]:
			wt = graph[u][v]
			newlen = dist[u] + wt
			if newlen < dist[v]:
				pq.decreaseKey(v, newlen)
				dist[v] = newlen
				pred[v] = u

	return (dist, pred)

def solution(s, v, dist, pred):
	'''Return path and total Information for shortest path from s to v'''

	path = [v]
	total = dist[v]
	while v != s:
		v = pred[v]
		path.insert(0, v)

	return 'length = ' + str(total) + ', path = ' + str(path)
	
if __name__ == '__main__':
	graph = { 0: {1: 6, 2: 8, 3: 18},
			  1: {4: 11},
			  2: {3: 9},
			  3: {},
			  4: {5: 3},
			  5: {3: 4, 2: 7}}

	dist, pred = singleSourceShortestPath(graph, 0)
	print dist, pred
	print solution(0, 5, dist, pred)		  							