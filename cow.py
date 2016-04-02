def getmin(pos, cows):
	
	no = len(pos)
	dist = [0]*(no-1)

	for y in range(1,no):
		dist[y-1] = pos[y] - pos[y-1]
	
	hi = max(pos) - min(pos)
	lo = min(dist)
	
	if hi == lo:
		print lo
		continue
		
	while lo < hi:
		
		x = (hi + lo)/2
		done = 1
		cur_dir = 0
			
		for i in range (0,no-1):
			
			if cur_dir + dist[i] <  x:
				cur_dir += dist[i]
			
			else:
				done +=1
				cur_dir = 0

		if done < cows:
			hi = x

		else:
			lo = x + 1		
	
	print x		

t = int(raw_input())

for i in range(0,t):
	
	stalls,cows = map(int, raw_input().split())
	pos = [0]*stalls
	
	for z in range(0,stalls):
		pos[z] = int(raw_input())

	pos.sort()
	getmin(pos, cows)	
