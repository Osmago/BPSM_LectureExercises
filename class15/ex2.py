#!bin/usr/python3

import re

dna = open("long_dna.txt", "r").read().rstrip("\n")

frags = [dna]
sites = [[r'A[ATCG]TAAT', 3],[r'GC[AG][AT]TG', 4]]

i = 0
while i < len(frags):
	for site in sites:
		if re.search(site[0], frags[i]):
			span = re.search(site[0], frags[i]).span()
			cut = span[0]+site[1]
			frag1 = frags[i][:cut]
			frag2 = frags[i][cut:]
			frags.remove(frags[i])
			frags.insert(i, frag2)
			frags.insert(i, frag1)
	i += 1

report = open("ex2.fasta", 'w')

total_length = 0
for frag in frags:
	report.write(">long_dna({}...{})\n{}\n".format(total_length, total_length+len(frag),frag))
	total_length += len(frag)

report.close()
