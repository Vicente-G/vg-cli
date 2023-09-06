function brew_install() {
    printf "Looking for installation of ${1}... "
    command -v "${1}" >& /dev/null
    if [[ $? != 0 ]]
    then printf "[FAILURE]\n Installing with brew!\n"
    brew install $1
    else printf "[SUCCESS]\n"
    fi
}
# Getting on home folder
cd
# Adding our folder target to PATH
if [[ ::$PATH:: != *:/usr/local/bin:* ]]
then PATH="/usr/local/bin:$PATH"
fi
printf "Looking for installation of Homebrew... "
brew --version >& /dev/null
if [[ $? != 0 ]]
then printf "[FAILURE]\n Installing Homebrew!\n"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else printf "[SUCCESS]\n"
fi
fi
# Checking for CLI dependencies
brew_install python3
brew_install git
brew_install gh
# Adding python useful modules
printf "Getting pyautogui and numpy... "
pip3 install -qq --no-input pyautogui numpy
printf "[SUCCESS]\n"
# Installation of vg CLI
echo "Install the Vicente-G's CLI? (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing Vicente-G's CLI..."
git clone https://github.com/Vicente-G/vg-cli.git /usr/local/lib/vg
rm /usr/local/lib/vg/setup.sh \
/usr/local/lib/vg/README.md \
/usr/local/lib/vg/.gitignore
rm -rf /usr/local/lib/vg/.git
mv /usr/local/lib/vg/vg.sh /usr/local/bin/vg.sh
cd /usr/local/bin
mv vg.sh vg ; cd
chmod +x /usr/local/bin/vg
fi
# Checking for Zsh and OhMyZsh!
brew_install zsh
echo "Install OhMyZsh!? (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing OhMyZsh!..."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

# From here it may interrupt, but there is no problem at all!
echo "Install my dependencies? It may take a while! (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing my dependencies..."
brew install ca-certificates \
act \
node \
pnpm \
pdm \
docker \
colima \
terraform
fi
echo "Install ALL Python versions? It may take a while! (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing Python versions..."
brew install python@3.7 \
python@3.8 \
python@3.9 \
python@3.10 \
python@3.11
fi
