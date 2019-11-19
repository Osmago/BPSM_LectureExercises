#!bin/usr/python3

def aa_percent(seq, aa):
	seq = seq.upper()
	aa = aa.upper()
	count = seq.count(aa)
	return int(100*count/len(seq))

assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(aa_percent("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
