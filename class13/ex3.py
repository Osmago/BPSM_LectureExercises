#!bin/usr/python3

def undet_base_threshold(seq, thrsh):
	seq = seq.upper()
	count = 0
	for base in seq:
		if not (base in set(['A','C','T','G'])):
			count += 1
	percent = round(100*count/len(seq)) 
	return percent > thrsh

assert undet_base_threshold('ctagctag', 50) == False
assert undet_base_threshold('ctagctagnnnnnnnnnn', 50) == True
assert undet_base_threshold('nxakcatgcatg', 20) == True
