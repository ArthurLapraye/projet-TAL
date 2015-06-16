#!/usr/bin/python3


def phoneit(mot,lang):
	subst = {"spa":"es", "por":"pt", "ita":"it"}
	commande = "espeak " + mot + " -q --ipa -v " + subst[lang]
	p = os.popen(commande).read()
	
	return p[:-1]

def levenshtein(s,t):
	if len(s) == 0:
		return len(t)
	elif len(t) == 0:
		return len(s)
	else:
		if s[-1] == t[-1]:
			cost = 0
		else:
			cost = 1
			
		return min([levenshtein(s[:-1],t)+1,levenshtein(s,t[:-1])+1,levenshtein(s[:-1],t[:-1]) + cost])

def avglev(s,t):
	d = min(len(s),len(t))
	return levenshtein(d
