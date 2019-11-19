#!/usr/bin/python3

#calculate fragment length after digestion

#get sequence file
seq_file = open("sequence2.txt", "r")
seq = seq_file.read()

#close sequence file
seq_file.close()

#take out linebreaks
seq = seq.replace("\n", "")

#find EcoRI site
site_loc = seq.find("GAATTC")
print ("EcoRI site found at position ", str(site_loc+1))

#get generated fragments
frag1 = seq[:site_loc+1]
print("First fragment: ", frag1)
print("length: ", len(frag1))

frag2 = seq[site_loc+1:]
print("Second fragment: ", frag2)
print("length: ", len(frag2))
