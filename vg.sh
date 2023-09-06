#!/bin/bash

# Secret command of uninstalling
if [[ $1 == "uninstall" ]]
then printf "are you sure? (y/n) "
read -n 1 ans

# Confirmation of uninstalling
if [[ $ans == "y" ]]
then printf "\nuninstalling...\n"
rm -rf /usr/local/lib/vg
rm /usr/local/bin/vg
echo "uninstalled!"
else printf "\naborted!\n"
fi
exit 0
fi

python3 /usr/local/lib/vg/src/cli.py $@
