#!/bin/bash
#This script will check the date and tell you who is having a birthday in the next days of the current month and in the next month

#First check the date to compare it to the file
 
curr_day=$(date +"%d")
curr_month=$(date +"%m")
next_month=$(($curr_month+1))
echo -e "Current date is\n$curr_day $curr_month\nAnd next month is \n$next_month\n"

#make adjustments to data
head -101 example_people_data.tsv | tail -100 | sort -t$'\t' -k5,5n -k4,4n > trimmed_data.tsv

echo "The next people having anniversaries in the next month are:"

#remove any previous output file
rm -f next_annivs.tsv

#while loop will read the data and do the necessary adjustments
unset IFS
IFS=$'\t'
while read name email city bday bmonth byear country
do
if test "$bmonth" -eq $curr_month -o "$bmonth" -eq $next_month
then
 echo -e "$name\t$bday\t$bmonth" >> next_annivs.tsv
fi
done < trimmed_data.tsv

cat next_annivs.tsv
