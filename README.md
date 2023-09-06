# vg-cli: My workspace in a nutshell!

As now I'm really happy with my fairly automated setup, I wanted to save it in case I get to use another computer. With that in mind, the `setup.sh` file should work as a one liner to install all "my dependencies", and the `vg.sh` file would have prepared all "my commands" that I use everyday, which includes some interfaces for `git` and `github` operations.

## Install

To install my workspace on your machine, just run the following command:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Vicente-G/vg-cli/main/setup.sh)"
```

If everything is correct, running the following command should output the help message of the cli, if not, then some error of the `vg` command not existing could be shown. In that case, please add an Issue explaning everything you did so I can work in solving it.

```sh
vg -h
```

If you liked anything that is made in here just steal it, there is a good reason because of why I made this repo public. I searched for other tools like this, but with not that much of a success, so, hopefully this project gives more people the fabulous idea of automating everything that they make, so we can spend those 2 minutes looking at our screen with no idea of what to do, instead of less important stuff as making that first commit or whatever. 

Also, if you are in Windows, you NEED a Unix console to use this. How would you get one? Easy, just install the Windows Subsystem for Linux (WSL) before doing anything! I can't provide you with a link as it's installed with the MS Store, but I lend you a nice [link](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10) with some instructions instead, just in case you forgot how to do it.

## Uninstall

Last but not least, you didn't like my cli and want to get rid of it? Well, that's sad, but I respect that, is not for everyone. I mean, it was made by me and for me. With that in mind, I'll lend you one last secret command, which will let you make a clean uninstall of my cli whenever you want to:

```sh
vg uninstall
```

With this command, and doing a confirmation, the cli will be removed from your system. However, the dependencies installed with the `setup.sh` file will remain intact, if you are interested on a way of removing those as well, add an Issue! Is not on my plans by now, (which I comment later) but I can certainly help. Feel free to add a PR as well with whatever you think is nice to this workspace, if you convince me, I'll add it right away!

## Future roadmap!

I plan to make some other stuff with this cli when I get more time, so here a TODO list:

* More templates! I'm actually working on this one, so take a look in my other repos!
* OMZ auto config with the setup (This should be easy, but I need some testing)
* One password only command (I want to stop typing so much passwords on everything!)
* SSH easy config for GH (I always forget how it is done, so it could be of big help)
* More GH commands! (Check the status of PRs and Issues, accept a PR to merge, etc)
* Config file guided changing (This should be easy too, to update the json file easily)
* Docker commands! (I would like to begin using just the terminal for productivity)
* Automatic updates (Is something I always wanted to do, so I can learn about it!)
