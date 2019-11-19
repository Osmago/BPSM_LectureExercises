#!/usr/bin/python3

fasta = open("AJ223353.fasta").read()
gb = open("AJ223353.gb").read().replace("\n", "").replace(" ", "")

fasta = fasta.replace("\n", "")
cds_pos = gb.find("CDS")
start = int(gb[cds_pos+3:cds_pos+5])
end = int(gb[cds_pos+7:cds_pos+10])

cds = fasta[start-1:end]

print(cds)

cds_out = open("AJ223353_cds.fasta", "w")
cds_out.write(cds)
