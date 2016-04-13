def computeLPSArray(pat, M, lps):
	len = 0 # length of the previous longest prefix suffix

	lps[0] # lps[0] is always 0
	i = 1

	# the loop calculates lps[i] for i = 1 to M-1
	while i < M:
		if pat[i]==pat[len]:
			len+=1
			lps[i] = len
			i+=1
		else:
			if len!=0:
				
				len = lps[len-1]

			else: 
				lps[i] = 0
				i+=1

def KMPSearch(txt):
	N = len(txt)

	# create lps[] that will hold the longest prefix suffix 
	# values for pattern
	got = ''
	lpss = [0]*N
	computeLPSArray(txt, N, lpss)
	for x in range (1,N+1):
		pat = txt[:x]
		M = len(pat)

		j = 0 # index for pat[]
		lps = lpss[:x]
		#print lps
		found = 0
		i = 0 # index for txt[]
		while i < N:
			if pat[j] == txt[i]:
				i+=1
				j+=1

			if j==M:
				#print "Found pattern at index " + str(i-j)
				found += 1
				j = lps[j-1]

			# mismatch after j matches
			elif i < N and pat[j] != txt[i]:
				# Do not match lps[0..lps[j-1]] characters,
				# they will match anyway
				if j != 0:
					j = lps[j-1]
				else:
					i+=1
		if ((found > 2) and (len(pat) > len(got))) :
			if pat == txt[:x] and pat == txt[N-x:]:
				got  = pat
	if got == '':
		print 'Just a legend'
	else:
		print got 

txt = raw_input()
KMPSearch(txt)
