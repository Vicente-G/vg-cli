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
# Checking for Homebrew
brew --version >& /dev/null
if [[ $? != 0 ]]
then echo "Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
# Checking for CLI dependencies
brew_install python3
brew_install git
brew_install gh
# Installation of vg CLI
git clone https://github.com/Vicente-G/vg-cli.git /usr/local/lib/vg
mv /usr/local/lib/vg/vg.sh /usr/local/bin/vg.sh
chmod +x /usr/local/bin/vg.sh
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
