# vg-cli: My workspace in a nutshell!

As now I'm really happy with my fairly automated setup, I wanted to save it in case I get to use another computer. With that in mind, the `setup.sh` file should work as a one liner to install all "my dependencies", and the `cli.sh` file would have prepared all "my commands" that I use everyday, which includes some interfaces for `git` and `github` operations. All of this is written in `Python` vanilla, which means it can be run in most "out of box" computers! But even if not, I'll have a nice [link](https://www.python.org/downloads/) to download the last version of it! To install this, just run the following:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Vicente-G/vg-cli/main/setup.sh)"
```

If everything is correct, running this command should output something that is not an error:

```sh
vg -h
```

If you liked anything that is made in here just steal it, there is a good reason because of why I made this repo public. I searched for other tools like this, but with not that much of a success, so, hopefully this project gives more people the fabulous idea of automating everything that they make, so we can spend those 2 minutes looking at our screen with no idea of what to do, instead of less important stuff as deploying or whatever.

Also, if you are in Windows, you need a Unix console, how would you get one? Easy, just install the Windows Subsystem for Linux (WSL) before doing anything! I can't provide you with a link as it's installed with the MS Store, but I lend you a nice [link](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10) with some instructions instead, just in case you forgot how to do it.
