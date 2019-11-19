#!bin/usr/python3

'''
function takes:
a dna sequence (str seq)
a codon translation table (dict table)
what frame to analyse(int = 1, 2, or 3)
if the reverse frame should be used (bool rev)
and returns the sequence for the translation of it
'''
def translate_cds(seq, table, frame = 1, rev = False):

	if type(seq) != str:
		print("dna sequence must be a string")
		return
	if type(table) != dict:
		print("codon table must be a dictionary")
		return	
	if type(frame) != int:
		print("frame# must be an integer")
		return
	
	#make the sequence processable
	seq = seq.upper()
	if rev:
		seq = ''.join(reversed(seq))
	seq = seq[frame-1:]

	protein	= []
	#get starting points 3 by 3
	for n in range(0, len(seq), 3):
		codon = seq[n:n+3]
		#check if codon is not in the end of the sequence and if it's in the dictionary
		if len(codon) == 3:
			if codon in table.keys():
				protein.append(table.get(codon))
			else:
				protein.append('*')
	return ''.join(protein)

'''
function takes:
a message for the input
the possibilities for the input to be (always strings)
'''
def user_input(m, possibilities = []):
	#won't stop unless given a proper input
	done = False
	while done == False:
		variable = input(m)
		#won't complain if a possibilities list ain't provided
		if possibilities != []:
			if variable in possibilities:
				return variable
				done = True
			else:
				print("please respond with {}".format(' or '.join(possibilities)))
		else:
			return variable
			done = True
	

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'
}

#get inputs from user
dna_in = user_input("please provide a coding sequence to be translated:\n\t")

rev_yn = user_input("should a reverse frame be translated? [y/n]:\t", ['y', 'n', 'Y', 'N'])
if rev_yn in 'yY':
	rev_in = True
	done = True
elif rev_yn in 'nN':		
	rev_in = False
	done = True

frame_nmbr = int(user_input("which frame? (1, 2, or 3):\t", ['1', '2', '3']))

print("your cds, translated is:\n\t", translate_cds(dna_in, gencode, frame_nmbr, rev_in))
