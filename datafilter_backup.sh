#!/bin/bash

regex="db\s+[0-9A-F]+h?"
xregex="[0-9A-F]+"
cmd="grep -o -E \"$regex\" -"

while getopts "nx" opt
do
	case $opt in
		n) cmd+="| wc -l";;
		x) cmd+="| grep -o -E $xregex -";;
		?) echo "error"
			exit 1;;
	esac
done
echo $0
echo $cmd
`$cmd`
