#!/bin/bash

#first ask for what blast to analise

#echo "what blast file to analise?"
#read input_blast

input_blast=blastoutput2.out

#trim the data to remove the header and tail
grep -v '#' $input_blast > blast_trim.tsv

#list subject accesion numbers
echo -e "\nsaved subject accession numbers to subj_acc_nmbrs.details\n"
cut -f2 blast_trim.tsv > subj_acc_nmbrs.details

#list alignment length and %id
echo -e "saved alignment lengths and %IDs to lens_ids.details\n"
cut -f3,4 blast_trim.tsv > lens_ids.details

#show HSPs with more than 20 mismatches
echo -e "saved HSPs with more than 20 mismatches to 20plus_mismatches.details\n"
awk '($5 > 20)' blast_trim.tsv > 20plus_mismatches.details

#show HSPs with more than 20 mismatches and up to 100aa
echo -e "saved HSPs w/ 21+ mismatches and shorter than 100aa to 20+mm_100aa.details\n"
awk '($4 < 100)' 20plus_mismatches.details > 20+mm_100aa.details

#list first 20 HSPs with fewer than 20 mismatches
echo -e "saved first 20 HSPs with fewer than 20 mismatches to first20fewer20mm.details\n"
awk '($5 < 20)' blast_trim.tsv | head -20 > first20fewer20mm.details

#count HSPs shorter than 100aa
echo -e "this is the number of HSPs shorter than 100aa\n"
awk '{if($4 < 100){a += 1;}} END{print(a)}' blast_trim.tsv
echo -e " "

#10 best hits
echo -e "best 10 HSPs saved to best10.details\n"
head -10 blast_trim.tsv > best10.details


