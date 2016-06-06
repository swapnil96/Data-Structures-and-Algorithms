'''Based on Activity selection problem - Codechef'''

tt = int(raw_input())

def printMaxActivities(s, f, n):
    
    f, s = zip(*sorted(zip(f, s)))
    #print f, s, f[0], s[1]
    i = 0
    ans = 1
    for j in xrange(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously 
        # selected activity, then select it
        if s[j] > f[i]:
                #sol1.append(j)
            #print 'adsf'
            ans += 1
            i = j

    #print sol1            
    return ans

sol = []
for i in xrange(tt):
    b = int(raw_input())
    start = []
    finish = []
    for j in xrange(b):
    	a = map(int, raw_input().split())
    	start.append(a[0])
    	finish.append(a[1])

    #print start, finish
    sol.append(printMaxActivities(start, finish, b))

for i in xrange(tt):
    print sol[i]
