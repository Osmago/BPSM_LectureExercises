#!/bin/usr/python3

import matplotlib.pyplot as plt

genome = open("ecoli.txt", "r").read().replace("\n", "")

window = 10000

at_count = []

for start in range(len(genome) - window):
    win = genome[start:start+window]
    at_count.append(win.count('AT') / window)

plt.figure(figsize=(20, 10))
plt.plot(at_count)
plt.title("AT COUNT\nPER 10Kb WINDOW")
plt.xlabel("Position in genome")
plt.ylabel("AT per 10000 bases")
plt.savefig("ex1.png", transparent = True)
plt.show()
