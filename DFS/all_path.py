graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(graph, start, end, path=[]):
    
    path = path + [start]
    print path

    if start == end:
        return [path]
    
    if not graph.has_key(start):
        return []
    
    paths = []

    for node in graph[start]:
            
        print node
        if node not in path:
    
            newpaths = find_path(graph, node, end, path)
    
    	    for newpath in newpaths:
    	       	paths.append(newpath)

    return paths        

print find_path(graph, 'A', 'D')    