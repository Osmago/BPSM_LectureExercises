myfavoritesequence='ACATAAAACATCAAAGTGAACAGATTGTAGTGTAAGAAGTTAGATTAA' 
while read line
do read line2
 if [[ $line2 == *$myfavoritesequence* ]];
 then
  echo "The sequence was found in" $line $line2
 fi  
done < $1
