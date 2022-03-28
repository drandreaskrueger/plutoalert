#!/bin/bash

# this will ONLY print anything IF the specific episodes are found
# plus the SILENT=false choice can make it much more talkative again

#######################################

FIND_THESE="s02e08\|s03e12"
# FIND_THESE="s02e99"
# FIND_THESE="s02e01\|s02e02"

# SILENT=false
SILENT=true

#######################################

print_perhaps () {
	if [ "$SILENT" = false ] ; then
		printf "$1"
		echo
	fi
}

print_perhaps ""
print_perhaps "select for $FIND_THESE" # "s02e08 or s03e12?"
print_perhaps ""

answer=$(./pluto_discovery.sh)
myEpisodes=$(printf "$answer" | grep "$FIND_THESE")

if [ -z "$myEpisodes" ]
then
	print_perhaps "NOPE. Your episodes are NOT in the results."
	print_perhaps ""
	print_perhaps "$answer"
else
	print_perhaps "YES"
	print_perhaps "YES"
	print_perhaps "YES"
	printf "$myEpisodes"
	echo
fi

print_perhaps ""
print_perhaps ""
print_perhaps "echo oh, and this is STEnterprise, by the way"
print_perhaps ""
if [ "$SILENT" = false ] ; then
	./pluto_enterprise.sh
fi
