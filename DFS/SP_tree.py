class tree:

    def __init__(self, no):

        self.no = no

    def LPT(self, s):
        
        p1 = 0
        p2 = 0
 
        for v in self.GRAPH[s]:
            
            if v in self.visited:
                continue
 
            self.visited.add(v)
 
            value = self.LPT(v) + 1
 
            if value > p1:
                p1 = value
                continue
            
            elif value == p1 or value > p2:
                p2 = value
                continue
        
        self.MAX_PATH = max(self.MAX_PATH, p1 + p2)
       
        return p1
 
    def make_graph(self):       
        
        self.GRAPH = {}
        self.MAX_PATH = float('-inf')
        self.visited = set()
 
        if self.no == 1:
            print 0
            raise KeyError
 
 
        for _ in xrange(1, self.no):
            
            u, v = map(int, raw_input().split())
            self.GRAPH.setdefault(u, []).append(v)
            self.GRAPH.setdefault(v, []).append(u)
           
        start = max(self.GRAPH.keys())
        self.visited.add(start)
        self.LPT(start)
        print self.MAX_PATH

a = int(raw_input())
q = tree(a)
q.make_graph()