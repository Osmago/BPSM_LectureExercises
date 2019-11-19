#!bin/usr/python3

g_dna = open("genomic_dna2.txt").read().rstrip("\n")
exons_file = open("exons.txt")

exons = []

for line in exons_file:
	exon = line.rstrip("\n").split(",")
	exons.append(g_dna[int(exon[0])-1:int(exon[1])])

out_file = open("ex2_out.txt", "w")
out_file.write(''.join(exons))
out_file.close()
