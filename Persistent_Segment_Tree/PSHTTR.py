
# def dfs(node, parent, distance, pa, tree, depth, explored):

#     explored[node] = True
#     depth[node] = distance
#     pa[node][0] = parent
#     for i in tree[node]:
#         if explored[i] == False:
#             dfs(i, node, distance+1, pa, tree, depth, explored)
        
# def lca(u, v, depth, pa):

#     if depth[u] < depth[v]:
#         u, v = v, u

#     for i in xrange(16, -1, -1):
#         if depth[u] - (1 << i) >= depth[v]:
#             u = pa[u][i]

#     if u == v:
#         return u

#     for i in xrange(16, -1, -1):
#         if pa[u][i] != -1 and pa[u][i] != pa[v][i]:
#             u = pa[u][i]
#             v = pa[v][i]

#     return pa[u][0]

# def find(u, v, k, depth, pa):

#     # anc = lca(u, v, depth, pa)
#     tot1 = 0
#     par = pa[u][0]
#     while par != -1:
#         temp = tree[u][par]
#         if temp <= k:
#             tot1 ^= temp
        
#         u = par
#         par = pa[par][0]

#     tot2 = 0
#     par = pa[v][0]
#     while par != -1:
#         temp = tree[v][par]
#         if temp <= k:
#             tot2 ^= temp
        
#         v = par
#         par = pa[par][0]
    
#     return tot1 ^ tot2 

# tt = int(raw_input())
# for i in xrange(tt):
#     n = int(raw_input())
#     tree = {}
#     for j in xrange(n-1):
#         u, v, c = map(int, raw_input().split())
#         try:
#             t = tree[u]
#             tree[u][v] = c
#             try:
#                 t = tree[v]
#                 tree[v][u] = c
            
#             except:
#                 tree[v] = {u: c}

#         except:
#             tree[u] = {v: c}
#             try:
#                 t = tree[v]
#                 tree[v][u] = c

#             except:
#                 tree[v] = {u: c}

#     depth = [-1]*(n+1)
#     explored = [False]*(n+1)
#     pa = [[-1]*17 for _ in xrange(n+1)]
#     dfs(1, -1, 0, pa, tree, depth, explored)
#     for j in xrange(1, n+1):
#         for k in xrange(1, 17):
#             if pa[j][k-1] != -1:
#                 pa[j][k] = pa[pa[j][k-1]][k-1]
    
#     m = int(raw_input())
#     for j in xrange(m):
#         u, v, k = map(int, raw_input().split())
#         print find(u, v, k, depth, pa)



# def dfs(node, parent, pa, tree, explored):

#     explored[node] = True
#     pa[node] = parent
#     for i in tree[node]:
#         if explored[i] == False:
#             dfs(i, node, pa, tree, explored)

# def dfs(node, pa, tree, depth, explored):

#     stack = []
#     stack.append(node)
#     stack1 = []
#     stack1.append(0)
#     pa[node][0] = -1
#     while stack:
#         u = stack.pop()
#         if explored[u] == False:
#             explored[u] = True
#             depth[u] = stack1.pop()
#             for i in tree[u]:
#                 if explored[i] == False:
#                     pa[i][0] = u
#                     stack.append(i)    
#                     stack1.append(depth[u]+1)
        

import bisect

class node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, l, r, val, idx, null):
        if l <= idx and idx <= r:
            # print '1st', self.value, l, r, val, idx
            if l == r:
                return node(self.value^val, null, null)

            m = (l + r)>>1
            return node(self.value^val, self.left.insert(l, m, val, idx, null), self.right.insert(m+1, r, val, idx, null))

        # print '2nd', self.value, l, r, val, idx
        return self

    def get(self, start, end, l, r):
        if r < start or end < l:
            return 0
        
        if l <= start and end <= r:
            return self.value

        m = (start + end)>>1
        p1 = self.left.get(start, m, l, r)
        p2 = self.right.get(m+1, end, l, r)
        return p1 ^ p2

# def dfs(root, pa, tree, depth, explored, null, hash, maxi):
def dfs(root, pa, tree, explored, null, hash, maxi):

    stack = []
    stack.append(1)
    stack_depth = []
    stack_depth.append(0)
    # pa[1][0] = -1
    pa[1] = 0
    while stack:
        u = stack.pop()
        if explored[u] == False:
            if u == 1:
                root[u] = null

            else:
                # print 'asdf', u, 0, maxi, pa[u][0], tree[u][pa[u][0]], hash[tree[u][pa[u][0]]]
                root[u] = root[pa[u]].insert(0, maxi, tree[u][pa[u]], hash[tree[u][pa[u]]], null)
            
            explored[u] = True
            # depth[u] = stack_depth.pop()
            for i in tree[u]:
                if explored[i] == False:
                    # pa[i][0] = u
                    pa[i] = u
                    stack.append(i)    
                    # stack_depth.append(depth[u]+1)
    
tt = int(raw_input())
for i in xrange(tt):
    n = int(raw_input())
    tree = {}
    weight = []
    for j in xrange(n-1):
        u, v, c = map(int, raw_input().split())
        weight.append(c)
        try:
            t = tree[u]
            tree[u][v] = c
            try:
                t = tree[v]
                tree[v][u] = c
            
            except:
                tree[v] = {u: c}

        except:
            tree[u] = {v: c}
            try:
                t = tree[v]
                tree[v][u] = c

            except:
                tree[v] = {u: c}
    
    weight = list(set(weight))
    weight.sort()
    hash = {}
    maxi = len(weight)
    for j in xrange(maxi):
        hash[weight[j]] = j

    # depth = [-1]*(n+1)
    explored = [False]*(n+1)
    # pa = [[-1]*17 for _ in xrange(n+1)]
    pa = [-1]*(n+1)
    root = [node]*(n+1)
    null = node(0, None, None)
    null.left = null
    null.right = null

    # print weight, hash

    # dfs(root, pa, tree, depth, explored, null, hash, maxi-1)
    dfs(root, pa, tree, explored, null, hash, maxi-1)
    # for j in xrange(1, n+1):
    #     for k in xrange(1, 17):
    #         if pa[j][k-1] != -1:
    #             pa[j][k] = pa[pa[j][k-1]][k-1]

    m = int(raw_input())
    for j in xrange(m):
        u, v, k = map(int, raw_input().split())
        idx = bisect.bisect(weight, k) - 1
        # anc = lca(u, v, depth, pa)
        c1 = root[u].get(0, maxi-1, 0, idx)
        # c2 = root[anc].get(0, maxi-1, 0, idx)
        c3 = root[v].get(0, maxi-1, 0, idx)
        # print c1, c3, idx
        print c1 ^ c3
