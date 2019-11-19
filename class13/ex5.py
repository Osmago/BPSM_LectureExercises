#!bin/usr/python3

def count_kmers(template, window_length, freq):
	windows = []
	hits = []
	for n in range(0, len(template)-window_length):
		window = template[n:n+window_length]
		windows.append(window)
	for kmer in set(windows):
		if template.count(kmer) > freq:
			hits.append(kmer)
	return hits

seq = str(input("what sequence to analyse? "))
query_len = int(input("what k-mer size to search for? "))
query_freq = int(input("search for k-mers appearing more than how many times? "))

print (count_kmers(seq, query_len, query_freq))
