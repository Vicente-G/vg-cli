function brew_install() {
    printf "Looking for installation of ${1}... "
    command -v "${1}" >& /dev/null
    if [[ $? != 0 ]]
    then printf "[FAILURE]\n Installing with brew!\n"
    brew install $1
    else printf "[SUCCESS]\n"
    fi
}

cd
# Adding our folder target to PATH
if [[ ::$PATH:: != *:/usr/local/bin:* ]]
then PATH="/usr/local/bin:$PATH"
fi

printf "Looking for installation of Homebrew... "
brew --version >& /dev/null
if [[ $? != 0 ]]
then printf "[FAILURE]\n Installing Homebrew!\n"
# Saving PATH for brew
if [[ $(uname) != Darwin ]]
then PATH="$HOME/.linuxbrew/bin:$PATH" ; hash -r
test -d ~/.linuxbrew && eval $( ~/.linuxbrew/bin/brew shellenv)
test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >> ~/.bash_profile
fi
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else printf "[SUCCESS]\n"
fi

# Installation of vg CLI
echo "Install the Vicente-G's CLI? (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing Vicente-G's CLI..."
# Checking for CLI dependencies
brew_install ca-certificates
brew_install python3
brew_install git
brew_install gh
brew_install docker
brew_install colima
printf "Getting pyautogui and numpy... "
pip3 install -qq --no-input pyautogui numpy
printf "[SUCCESS]\n"

echo "Clonning CLI from github.com!"
git clone https://github.com/Vicente-G/vg-cli.git /usr/local/lib/vg
rm /usr/local/lib/vg/setup.sh \
/usr/local/lib/vg/README.md \
/usr/local/lib/vg/.gitignore
rm -rf /usr/local/lib/vg/.git
mv /usr/local/lib/vg/vg.sh /usr/local/bin/vg.sh
cd /usr/local/bin
mv vg.sh vg ; cd
chmod +x /usr/local/bin/vg
echo "CLI succesfully installed!"
fi

# Checking for Zsh and OhMyZsh!
echo "Install OhMyZsh!? (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing OhMyZsh!..."
brew_install zsh
# Setting Zsh as default
echo "Required sudo password to set Zsh as default"
command -v zsh | sudo tee -a /etc/shells
chsh -s $(which zsh)
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

echo "Install my dependencies? It may take a while! (y/n) "
read -s -n 1 ans
if [[ $ans == "y" ]]
then echo "Installing my dependencies..."
brew install act \
node \
pnpm \
pdm \
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
