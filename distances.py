#!/usr/bin/python3

import os
import re
import phonemes as p


rem=re.compile(r"['ˈˈˌː ̃]*")
subs=re.compile(r"tʃ")

def memoize(f):
	memo = {}
	def helper(x,y):
		if x not in memo:
			memo[x,y] = f(x,y)
		return memo[x,y]
	return helper


def phoneit(mot,lang):
	subst = {"spa":"es", "por":"pt", "ita":"it"}
	commande = "espeak \"" + mot + "\" -q --ipa -v " + subst[lang]
	p = os.popen(commande).read()
	p=rem.sub("",p)
	p=re.sub("tʃ","ʧ",p)
	p=re.sub("dʒ","ʤ",p)
	#p=subs.sub(r"\1\1",p)
	#print(p.rstrip())
	
	return p.strip()

MAXCOST=100

def dist(a,b):
	if a == b:
		return 0
	elif a in p.phonemes and b in p.phonemes:
		return p.dist(a,b)
	else:
		print("phoneme inconnu : " + a + " " + b +"\n")
		raise ValueError
		
		#return MAXCOST

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
				cost = 0 if s[i]==t[j] else 1
				v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
			for j in range(len(v0)):
				v0[j] = v1[j]
 
		return v1[len(t)]

def phlevenshtein(s, t):
		''' From Wikipedia article; Iterative with two matrix rows. '''
		if s == t: return 0
		elif len(s) == 0: return len(t)*MAXCOST
		elif len(t) == 0: return len(s)*MAXCOST
		v0 = [None] * (len(t) + 1)
		v1 = [None] * (len(t) + 1)
		for i in range(len(v0)):
			v0[i] = i*MAXCOST
		for i in range(len(s)):
			v1[0] = i*MAXCOST + MAXCOST
			for j in range(len(t)):
				cost = dist(s[i],t[j])
				v1[j + 1] = min(v1[j] + MAXCOST, v0[j + 1] + MAXCOST, v0[j] + cost)
			for j in range(len(v0)):
				v0[j] = v1[j]
 
		return v1[len(t)]

"""def levenshtein(s,t):
	if len(s) == 0:
		return len(t)
	elif len(t) == 0:
		return len(s)
	elif s == t:
		return 0
	else:
		n=0
		while n < min(len(s),len(t)) and s.startswith(t[:n]):
			n += 1
			#print(n)
			
		return min([levenshtein(s[1:],t)+1,levenshtein(s,t[1:])+1,1+levenshtein(s[n:],t[n:])])
"""

def avglev(s,t):
	try:
		d = min(len(s),len(t)) + 0.0
		return phlevenshtein(s,t)/d
	except ZeroDivisionError:
		return None

