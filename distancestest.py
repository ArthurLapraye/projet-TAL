#!/usr/bin/python3

import re
from distances import *

tabz=re.compile(r"\t")
spaces=re.compile(r" ")
with open("/home/arthur/programmes/python/projet/cognates+lat.txt") as f:
	for line in f:
		if line[0] == "#":
			continue
		else:
			[es,it,_,pt] = tabz.split(line)
			pt=pt[:-1]
			try:
				print(pt+"\t"+es+"\t"+it+" "+str(avglev(es,pt))+"/"+str(avglev(es,it))+"/"+str(avglev(it,pt)))
			except ValueError:
				input()
				pass


