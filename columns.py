#!/usr/bin/python3

import re
import os
import sys
from distances import levenshtein,phoneit

adr = "/home/arthur/programmes/python/projet/"
spatab = adr+ "mcr/wn-data-spa.tab"
itatab = adr+ "ita/wn-data-ita.tab"
portab = adr+ "por/wn-data-por.tab"
engtab = adr+ "eng/wn-data-eng.tab"

files=[("spa",spatab),("ita",itatab),("por",portab)]

trips=dict()

phones=set()
phstring=""
tabz=re.compile(r"\t")
spaces=re.compile(r" ")
paren=re.compile(r"\([^)]*\)")

capinterdit="ABCDEFGHIJKLMNOPQRSTUVWXYZΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψω"

print("Extraction des lemmes...")

for lang,elem in files:
	
	with open(elem) as f:
		for line in f:
			if line[0] == "#":
				continue
			else:
				[sem,_,forme]=tabz.split(line)
				forme=forme.rstrip()
				z=paren.sub("",forme)
				if len(z) > 0:
					forme=z
				else:
					forme=re.sub(r"[)(]*","",forme)
				
				
				if not " " in forme and forme[0] not in capinterdit:
					trips[lang]=trips.get(lang,{})
					trips[lang][sem]=trips[lang].get(sem,[])+ [forme]
					#phstring += phoneit(forme,lang)
					#print(forme)
					
#print(str(set(phstring)))

#sys.exit(0)

print("Création de triplets de sens")
intersection = set(trips["spa"].keys()) & set(trips["ita"].keys()) & set(trips["por"].keys()) 

print("Phonétisation")

fonetik=dict()
orthogr=dict()

glose=dict()

for synset in intersection:
	fonetik[synset]={}
	orthogr[synset]={}
	for l in trips:
		fonetik[synset][l]=[phoneit(x,l) for x in trips[l][synset] ]
		orthogr[synset][l]=[x for x in trips[l][synset] ]

print("Extraction de la glose")

with open(engtab) as en:
	for line in en:
		if line[0] == "#":
			continue
		else:
			[sem,_,forme]=tabz.split(line)
			if sem in intersection and sem not in glose:
				glose[sem]=forme.strip()

print("Écriture de la sortie")

with open(adr+"phono","w") as cols:
	y=""
	for synset in intersection:
		y+=glose[synset]
		for l in ["por","spa","ita"]:
			y += "\t" 
			for m in fonetik[synset][l]:
				y += m + "; "
		y += "\n"
	
	cols.write(y)

with open(adr+"orthogr","w") as cols:
	y=""
	for synset in intersection:
		y+=glose[synset]
		for l in ["por","spa","ita"]:
			y += "\t" 
			for m in orthogr[synset][l]:
				y += m + "; "
		y += "\n"
	
	cols.write(y)

print("Fin")



