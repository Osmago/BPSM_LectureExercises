#!bin/usr/python3

def count_kmers(template, window_length, freq):
	windows = []
	for n in range(0, len(template)-window_length):
		window = template[n:n+window_length]
		windows.append(window)
	for kmer in set(windows):
		if template.count(kmer) > freq:
			print(kmer)

count_kmers("ATGCATCATG", 2, 2)
