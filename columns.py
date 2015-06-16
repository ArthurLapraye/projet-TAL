#!/usr/bin/python3

import re
import os
from distances import levenshtein

adr = "/home/arthur/programmes/python/projet/"s
spatab = adr+ "mcr/wn-data-spa.tab"
itatab = adr+ "ita/wn-data-ita.tab"
portab = adr+ "por/wn-data-por.tab"

files=[("spa",spatab),("ita",itatab),("por",portab)]

trips=dict()

for tag,elem in files:
	tabz=re.compile(r"\t")
	spaces=re.compile(r" ")
	with open(elem) as f:
		for line in f:
			if line[0] == "#":
				continue
			else:
				[sem,_,forme]=tabz.split(line)
				trips[sem]=trips.get(sem,{})
				trips[sem][tag]=trips[sem].get(tag,[])+[spaces.sub("_",forme[:-1])]


