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

# Secret command of upgrading the version
if [[ $1 == "upgrade" ]]
then echo "uninstalling current version..."
SAVE_CONFIG=$(cat /usr/local/lib/vg/config.json)
rm -rf /usr/local/lib/vg
rm /usr/local/bin/vg
echo "clonning new version..."
git clone https://github.com/Vicente-G/vg-cli.git /usr/local/lib/vg
rm /usr/local/lib/vg/setup.sh \
/usr/local/lib/vg/README.md \
/usr/local/lib/vg/.gitignore
rm -rf /usr/local/lib/vg/.git
mv /usr/local/lib/vg/vg.sh /usr/local/bin/vg.sh
cd /usr/local/bin
mv vg.sh vg ; cd
chmod +x /usr/local/bin/vg
echo "recovering older config..."
set -o | grep on | grep noclobber >& /dev/null
if [[ $? != 0 ]]
then echo $SAVE_CONFIG > /usr/local/lib/vg/config.json
else echo $SAVE_CONFIG |> /usr/local/lib/vg/config.json
fi
echo "newer version of CLI succesfully installed!"

python3 /usr/local/lib/vg/src/cli.py $@
