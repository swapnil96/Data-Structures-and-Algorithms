import os
import sys
import string
import random
def KMPSearch(txt, pat, lps):
	M = len(pat)
	N = len(txt)

	j = 0 # index for pat[]

	i = 0 # index for txt[]
	found  = 0
	while i < N:
		if pat[j] == txt[i]:
			i+=1
			j+=1

		if j==M:
			#print "Found pattern at index " + str(i-j)
			#j = lps[j-1]
			return True
		# mismatch after j matches
		elif i < N and pat[j] != txt[i]:
			# Do not match lps[0..lps[j-1]] characters,
			# they will match anyway
			if j != 0:
				j = lps[j-1]
			else:
				i+=1
	
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

def isRepeat(string):
    # Find length of string and create an array to
    # store lps values used in KMP
    n = len(string)
    lps = [0] * n
 
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(string, n, lps)
 	
    length = lps[n-1]
    #print lps
    got = 0 
    while length != 0:
    	if KMPSearch(string[1:n-1], string[:length], lps):
    		print string[:length]
    		got = 1
    		break
    	length = lps[length-1]
    if length == 0 and got == 0:
    	print 'Just a legend'	
    

txt = raw_input()
#txt = ''.join(random.choice(string.ascii_lowercase) for _ in range(10^6))
isRepeat(txt)

