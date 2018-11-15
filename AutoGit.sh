#!/bin/bash
#Morgan P.
#11/14/18
#Github Automation

cd /home/nyght/Desktop/GithubFolder/
git add .
read -p "Description for the changes?
> " description
git commit -m "$description"
echo $description
git push origin master
