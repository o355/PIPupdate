# Welcome to PIPupdate (1.0.2)!
An easy-to-use PIP package manager. Update, force reinstall, do an easy requirements.txt install, and uninstall all packages in 1 command.

**Quick 2017 update: Sorry I haven't gotten around to 1.1. There's been little time to actually code PIPupdate, alongside 30 other projects (literally) I'm also maintaining.**

# Why PIPupdate?
There's a simple problem with PIP. There is no command that updates all packages in one sweep. So, to help alleviate the issue, I made PIPupdate.

PIPupdate was founded on the basis of a simple, but advanced PIP updater, from reading Stack Overflow. With answers flying all over the place, and bad cross-platform compatibility, I was inspired to make a cross-platform, simple, yet advanced PIP updater.

PIPupdate can do what it says. What it can also do (in later releases) is force reinstall all your packages, do a graphical requirements.txt install, and uninstall all packages (but pip) with command-line arguments. PIPupdate will (with your consent, of course) install needed libraries automatically, and do it's thing.

PIPupdate is completely open-source, and cross-platform. No need to install xargs, fool with grep. PIPupdate just works, and outputs progress along the way. 

# Requirements
* Python 3 (a Python 2 port will come after release)
* PIP (it's in the name, folks.)
* The subprocess, sys, and time libraries (unless you have a super custom Python install, you should already have these libraries.)
* An internet connection

# Setting up PIPupdate
It's easy. And it isn't a pain in the neck.

* Download the ZIP corresponding to the latest release (usually called pipupdate-versionnumber.zip), and extract it to a folder.
* Linux Users: You can also run the command ```https://github.com/o355/pipupdate.git --depth=1``` to download/extract PIPupdate. There are also instructions on getting the release ZIP, and extracting the ZIP in the releases tab.
* Open a terminal prompt in that location, and type in ```python pipupdate.py```
* You could always double-click the file on Mac OS X/Windows, if you don't feel like opening terminal prompts.
* For Linux users, use ```python3 pipupdate.py```, to force the script to run as Python 3.
* The updater will do it's thing. If you have lots of packages, grab a snack, it may take a while!
* The speed of the updater will usually depend on your internet connection, more than your computer speed.

# Have a suggestion? See a bug? Want to make additions?
Be sure to report suggestions and bugs with issues.
Send some pull requests as well, if you want to help contribute to the updater!
