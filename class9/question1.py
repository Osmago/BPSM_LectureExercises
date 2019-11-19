#!/usr/bin/python3

#count AT content of sequence 1 and get complement

#get sequence file
seq_file = open("sequence1.txt", "r")
seq = seq_file.read()

#close sequence file
seq_file.close()

#take out linebreaks
seq = seq.replace("\n", "")

#calculate at content
at_content = (seq.count("A") + seq.count("T"))/len(seq)
print("sequence: ", seq)
print("AT content: ", at_content)

#convert bases to complement lowercase
complement = seq.replace("A", "t")
complement = complement.replace("T", "a")
complement = complement.replace("C", "g")
complement = complement.replace("G", "c")

#remember to use uppercase and print
complement = complement.upper()
print ("Complement: ", complement)
