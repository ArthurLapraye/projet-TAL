#!/usr/bin/python3

import re
import os
from distances import levenshtein

adr = "/home/arthur/programmes/python/projet/"
spatab = adr+ "mcr/wn-data-spa.tab"
itatab = adr+ "ita/wn-data-ita.tab"
portab = adr+ "por/wn-data-por.tab"
engtab = adr+ "eng/wn-data-eng.tab"

files=[("spa",spatab),("ita",itatab),("por",portab)]

trips=dict()

for lang,elem in files:
	tabz=re.compile(r"\t")
	spaces=re.compile(r" ")
	with open(elem) as f:
		for line in f:
			if line[0] == "#":
				continue
			else:
				[sem,_,forme]=tabz.split(line)
				if not " " in forme and forme[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					trips[lang]=trips.get(lang,{})
					trips[lang][sem]=trips[lang].get(sem,[])+ [forme[:-1]]

print("a")
intersection = set(trips["spa"].keys()) & set(trips["ita"].keys()) & set(trips["por"].keys()) 

print("b")

z=dict()
glose=dict()

for synset in intersection:
	z[synset]={}
	for l in trips:
		z[synset][l]=trips[l][synset]

print("c")

with open(engtab) as en:
	for line in en:
		if line[0] == "#":
			continue
		else:
			[sem,_,forme]=tabz.split(line)
			if sem in intersection:
				glose[sem]=forme[:-1]

print("d")

with open("/tmp/columns","w") as cols:
	y=""
	for synset in intersection:
		y+=glose[synset]
		for l in z[synset]:
			y += "\t" 
			for m in z[synset][l]:
				y += m + "; "
		y += "\n"
	
	cols.write(y)

print("e")



