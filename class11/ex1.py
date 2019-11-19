#!bin/usr/python3

in_file = open("input.txt")

adapter_len = 14

out_file = open("ex1_out.txt", "w")

for line in in_file:
	trim = line[adapter_len:].rstrip("\n")
	print(len(trim))
	out_file.write(trim + "\n")

out_file.close()
