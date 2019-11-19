#!/usr/bin/python3

#Extract exons

#get sequence file
seq_file = open("sequence3.txt", "r")
seq = seq_file.read()

#close sequence file
seq_file.close()

#take out linebreaks
seq = seq.replace("\n", "")

#splice the string to get exon and intron parts
exon1 = seq[:63]
intron = seq[63:91]
exon2 = seq[91:]

#report what was got
print("seq:\t", seq)
print("\tlength:\t", len(seq))
print("\nexon1:\t", exon1)
print("\tlength:\t", len(exon1))
print("\nintron:\t", intron)
print("\tlength:\t", len(intron))
print("\nexon2:\t", exon2)
print("\tlength:\t", len(exon2))

#concatenate exons to create cds and calculate % coding
cds = exon1 + exon2
print("\ncds:\t", cds)
print("\tlength:\t", len(cds))
print("%cds:\t", (100*len(cds)/len(seq)))

#return the better-annotated form with lowercase intron
intron = intron.lower()
print ("\nbetter-annotated form:\n", (exon1+intron+exon2))

