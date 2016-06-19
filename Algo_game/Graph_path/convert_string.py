'''Change one string to another in minimum steps'''

def minEditDistance(s1, s2):
	'''Compute minimum edit distance converting s1 --> s2'''

	m = {}
	len1 = len(s1)
	len2 = len(s2)
	maxlen = max(len1, len2)
	m = [None] * (len2 + 1)
	for i in xrange(len2 + 1):
		m[i] = [0] * (len1 + 1)

	#set up initial cost in horizontal
	for i in xrange(1, len1 + 1):
		m[0][i] = i

	#set up cost for vertical
	for i in xrange(1, len2 + 1):
		m[i][0] = i

	#compute best
	for i in xrange(1, len2 + 1):
		for j in xrange(1, len1 + 1):
			cost = 1
			if s1[j - 1] == s2[i - 1]:
				cost = 0

			#cost of changing [i][j] character
			#cost of removing character from si
			#cost of adding character to sj
			replaceCost = m[i - 1][j - 1] + cost
			removeCost = m[i - 1][j] + 1
			addCost = m[i][j - 1] + 1
			m[i][j] = min(replaceCost, removeCost, addCost)

	print m
	return m[len2][len1]

def levenshtein(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    if s == t: return 0
    elif len(s) == 0: return len(t)
    elif len(t) == 0: return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        
        for j in range(len(v0)):
            v0[j] = v1[j]
                
    return v1[len(t)]

if __name__ == '__main__':
	print minEditDistance('grates', 'create')
	print levenshtein('grates', 'create')

							
