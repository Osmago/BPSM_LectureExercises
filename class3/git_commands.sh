# rm -f *.zip *.txt *.sh
rm -fr .git

git init
git config --local user.name "KeenPythonCoder2019"
git config --local user.email "SuperStudent@someserver.universe.com"
git config merge.tool vimdiff
git config merge.conflictstyle diff3
git config mergetool.prompt false
git config --global core.editor "nano -w"
git config --global core.editor "gedit --wait --new-window"
git config --global core.autocrlf input
git config --global alias.st status
git config --list | grep "core"
git status
git st
echo -e "# This line has motif1 and motif1 in it \n# This line has motif2 only" > motif_file.txt
cat motif_file.txt
git add motif_file.txt
git commit -m "First file added"

zip Assignment.zip motif_file.txt


ls
git add Assignment.zip
git commit -m "Assignment all done and zipped"

git st
git log 
git log --oneline


echo "# This line has motif3 on it" >> motif_file.txt
cat motif_file.txt
cat motif_file.txt <(echo "# This line has motif4 on it")  > motif_file2.txt
cat motif_file2.txt
zip -u Assignment.zip motif_file*
git add motif_file*
git add Assignment.zip
git commit -m "Additional motif files, and updated zip file"

git log
git config --global alias.lo "log --oneline"
git lo


touch someotherfile.sh
zip -u Assignment.zip someotherfile.sh
ls -al


git add someotherfile.sh
git commit -m "Added the someotherfile.sh shell script"
git reset HEAD someotherfile.sh
cat someotherfile.sh 
echo "Some random text" >> someotherfile.sh
cat someotherfile.sh 

git add someotherfile.sh
git commit -m "Second version of the someotherfile.sh shell script"
git add Assignment.zip
git commit Assignment.zip -m "Updated version of zip"
git st

cat someotherfile.sh 
echo "More random text" >> someotherfile.sh
cat someotherfile.sh 
git add someotherfile.sh
git commit -m "Third version of the someotherfile.sh shell script"
git st
git lo


echo -e "# This is my better script\n# Done using different approaches" > my_cool_script.sh
cat my_cool_script.sh
git add my_cool_script.sh
git commit -m "Added my_cool_script"
git lo
echo "# This is definitely my better script" >> my_cool_script.sh
cat my_cool_script.sh

git checkout my_cool_script.sh
cat my_cool_script.sh

echo "# This script is not going to work" >> my_cool_script.sh
cat my_cool_script.sh
echo "# This script is not good" >> my_cool_script.sh
cat my_cool_script.sh
git add my_cool_script.sh
git commit -m "I am not sure cool script is actually any good"
cat my_cool_script.sh

zip Assignment.zip my_cool_script.sh
zip -u Assignment.zip
git add Assignment.zip
git commit Assignment.zip -m "Updated contents of zip to include coolscript"

git lo

git tag -a v1.0 f114520 -m "A very preliminary version 1"
git tag -a v2.0 -m "Version 2"
git tag
git show v1.0
git tag -a v1.2 f114520 -m "A very preliminary version 1.2"
git tag
git tag -d v1.0
git show v1.2 | grep commit


git lo

cat my_cool_script.sh

git checkout HEAD 
cat my_cool_script.sh

git checkout HEAD~1
git st
cat my_cool_script.sh
git checkout master
git st

git lo
git checkout HEAD~3
git branch -v
git st

cat my_cool_script.sh
git checkout master
cat my_cool_script.sh
git st

git lo

git tag

ls
git checkout -b Version1.2 v1.2
ls

git lo
cat someotherfile.sh
echo "This script has achieved total perfection now, so I am going to finish things off and call it done." >> someotherfile.sh
cat someotherfile.sh
git add someotherfile.sh
git commit -m "Final version of the someotherfile.sh shell script prior to merge"
git lo

cat someotherfile.sh
git checkout master
cat someotherfile.sh


git merge Version1.2
git mergetool 

git merge Version1.2

git commit -m "There were conflicts with someotherfile.sh, merged all the changes manually"
git clean 
git clean -f
git merge Version1.2
git lo

cat someotherfile.sh
ls -al

git log > all_the_things_I_did
head all_the_things_I_did

sed -i 's/KeenPythonCoder2019/Bxxxxxx-2019/g' all_the_things_I_did
head -n3 all_the_things_I_did

sed -i 's/<SuperStudent@someserver.universe.com>/<email_not_provided>/g' all_the_things_I_did
head -n3 all_the_things_I_did


git log |  awk '{
if($1=="Author:")
 {
$2="Bxxxxxx-2019";
$3="<email_not_provided>";
 }
print $0;
               }' | head -3


git log |  awk '{
if($1=="Author:") {$2="Bxxxxxx-2019"; $3="<email_not_provided>"; }
print $0; }' >  all_the_things_I_did

zip  Assignment.zip all_the_things_I_did
zip -emf Assignment.zip

ls -al

mkdir ~/LectureExercises/Assignment1
cp Assignment.zip ~/LectureExercises/Assignment1/Bxxxxxx-2019.Assignment1.zip
cd ~/LectureExercises/Assignment1
ls
git lo

git init
git config --local user.name "Bxxxxxx-2019"
git config --local user.email "<email_not_provided>"
git add Bxxxxxx-2019.Assignment1.zip
git commit -m "Assignment1 submission"


curl -u Bxxxxxx-2019 https://api.github.com/user/repos -d '{"name":"Assignment1"}'
git remote add origin https://github.com/Bxxxxxx-2019/Assignment1.git
git push -u origin master


cd ~/LectureExercises/Lecture03
git clone https://github.com/B000000-2019/Assignment1 Als_Assignment1
cd Als_Assignment1
ls -al

git log
unzip -l Bxxxxxx-2019.Assignment1.zip
unzip Bxxxxxx-2019.Assignment1.zip

cd ~/LectureExercises/Lecture03
git clone https://github.com/B000000-2019/hello-world Als_HelloWorld
cd Als_HelloWorld
ls
firefox index.html &









