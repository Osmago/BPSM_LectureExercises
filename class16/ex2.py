#!/bin/usr/python3

import matplotlib.pyplot as plt

#read and make it processable (a list of characters
align = open("alignment.txt", "r").readlines()

total_cons = []
for pos in range(len(align[0])-1):
	aa_align = []
	#get each column in turn
	for seq in align:
		aa_align.append(seq[pos])
	
	#measure the conservation and append to a list
	total_cons.append(len(set(aa_align)))

#plot
plt.figure(figsize=(20, 10))
plt.plot(total_cons)
plt.title("AA possibilies for each position")
plt.xlabel("position")
plt.ylabel("unique AAs")
plt.savefig("ex2.png", transparent = True)
plt.show()
