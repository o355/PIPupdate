# Welcome to PIPupdate (1.0)!
An easy-to-use PIP package manager. Update, force reinstall, do an easy requirements.txt install, and uninstall all packages in 1 command.

# Why PIPupdate?
Updating all PIP packages can be confusing to a newcomer. I wanted PIPupdate to sort of emulate APT, but in a different way.

Right now, there is no solution that kills all the problems we've had in one stone. Browsing through possible solutions on StackOverflow confused me, which script actually works, what works in Windows, which ones have me installing other things to do one thing.

PIPupdate was my solution to the troubles the newcomers and myself have had. It's a small >4 KB script that can update, force reinstall, easily do a requirements.txt install, and uninstall all packages. PIPupdate was made with simplicity, but also being advanced for power users, and also outputs useful information to boot.

PIPupdate is open-source, cross-platform, and doesn't require installing anything manually. Run 1 command, and the script does it all. PIPupdate can install PIP for you, and automatically installs any required libraries for running the script (via PIP). At the same time, I've baked in some advanced functionality for advanced users.

# Requirements
* Python 3 (a Python 2 port will come after release)
* PIP (it's in the name, folks.)
* The subprocess, sys, and time libraries (unless you have a super custom Python install, you should already have these libraries.)
* An internet connection

# Setting up PIPupdate
It's easy. And it isn't a pain in the neck.

* Download the ZIP corresponding to the latest release (usually called pipupdate-versionnumber.zip), and extract it to a folder.
* Linux Users: You can also run the command ```https://github.com/o355/pipupdate.git --depth=1``` to download/extract PIPupdate.
* Open a terminal prompt in that location, and type in ```python pipupdate.py```
* You could always double-click the file on Mac OS X/Windows, if you don't feel like opening terminal prompts.
* For Linux users, use ```python3 pipupdate.py```
* The updater will do it's thing. If you have lots of packages, grab a snack, it may take a while!
* The speed of the updater will usually depend on your internet connection, more than your computer speed.

# The future of PIPupdate
PIPupdate is in it's early stages, and there's still a lot left to add. Here's generally a list of things I'd like to add in the future.

* The force reinstall, uninstall everything, and required.txt easy install arguments. (probably 1.1)
* Warnings for operations on 150+ packages (as well as saving the option to not reannoy the user with the warning) (probably 1.3)
* A colorless version of PIPupdate (1.0.1)
* Displaying elapsed time for 1 update, the entire operation (probably 1.2), and possibly doing a rough ETA for finishing the entire op (1.4?)

# Have a suggestion? See a bug? Want to make additions?
Be sure to report suggestions and bugs with issues.
Send some pull requests as well, if you want to help contribute to the updater!
