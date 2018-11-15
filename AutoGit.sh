#!/bin/bash
#Morgan P.
#11/14/18
#Github Automation

read -p "Have you completed the setup before? [Y/N]
> " n
case $n in

	n)
read -p "Please enter your PC's username so the script can make a library folder
> " user
read -p "Please enter the absolute file path to your github folder 
> " path
read -p "$path, is this correct? [Y/N]
> " y
case $y in
	y)
		mkdir /home/$user/Desktop/lib
		echo "path="$path"" > /home/$user/Desktop/lib/AutoGitFilePath.txt
		;;
	n)
		echo "Exiting Program..."
		;;
esac
;;

	y)
source AutoGitFilePath.txt
cd $path
git add .
read -p "Description for the changes?
> " description
git commit -m "$description"
git push origin master
