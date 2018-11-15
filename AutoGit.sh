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
read -p "Please enter the absolute file path to your github folder. If your folder has a space in it's name, please use a wildcard symbol after the starting 2-4 letters of it's name, so it won't accidentally pick up other folders. 
> " path
read -p "$path, is this correct? [Y/N]
> " y
case $y in
	y)
		mkdir /home/$user/Desktop/lib
		echo "path=$path" > /home/$user/Desktop/lib/AutoGitFilePath.txt
		echo "user=$user" > /home/$user/Desktop/lib/AutoGitUser.txt
		;;
	n)
		echo "Exiting Program..."
		exit
		;;
esac
;;

	y)
		cd
                source */lib/AutoGitUser.txt
		source */lib/AutoGitFilePath.txt
	     
	     ;;

esac
cd $path
git add .
read -p "Description for the changes?
> " description
git commit -m "$description"
git push origin master
