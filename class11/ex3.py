#!bin/usr/python3

def gc_cont(seq):
	i = 0
	for base in seq:
		if base == 'C' or base == 'G':
			i += 1
	return round(100*i/len(seq), 2)


seq = open("../week10/AJ223353_cds.fasta").read()
window_length = 30
offset = 3

out_file = open("ex3_out.txt", "w")

for n in range(0, len(seq)-window_length+1, offset):
	window = seq[n:n+window_length]
	out_file.write((">AJ223353 position {}, gc content: {}%".format(n+1, gc_cont(window)) + "\n"))
	out_file.write(window + "\n")

out_file.close()
