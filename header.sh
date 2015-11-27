#!/bin/zsh
if [ $# -eq "1" ]; then 
	filename=$1
	echo "# AUTHOR\t: Arjun Krishna Babu" >> $filename
	echo -n "# DATE\t\t: " >> $filename
	date >> $filename
	echo "# OS\t\t: Fedora 23 Workstation" >> $filename
	exit 0
else
	echo "Error: Specify ONE filename"
	exit 1
fi
