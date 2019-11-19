#!bin/usr/python3

def aa_percent_v2(seq, aas=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
	count = 0
	seq = seq.upper()
	for letter in seq:
		for aa in aas:
			if letter == aa.upper():
				count += 1
	return int(100*count/len(seq))

assert round(aa_percent_v2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(aa_percent_v2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(aa_percent_v2("MSRSLLLRFLLFLLLLPPLP")) == 65
