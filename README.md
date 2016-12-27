# Welcome to PIPupdate!
An easy-to-use PIP package manager. Update, force reinstall, and uninstall all packages in 1 command.

# Why PIPupdate?
Updating all PIP packages can be confusing to a newcomer. I wanted PIPupdate to sort of emulate APT, but in a different way.

Right now, there is no solution that kills all the problems we've had in one stone. Browsing through possible solutions on StackOverflow confused me, which script actually works, what works in Windows, which ones have me installing other things to do one thing.

PIPupdate was my solution to the troubles the newcomers and myself have had. It's a small >4 KB script that can update, force reinstall, and uninstall packages easily, while outputting useful information, like progress, update duration, and the number of packages to update.

PIPupdate is open-source, cross-platform, and doesn't require installing anything. Run 1 command, and the script does it all.

# Requirements
* Python 3 (a Python 2 port will come after release)
* PIP (it's in the name, folks.)
* The subprocess, sys, and time libraries (unless you have a super custom Python install, you should already have these libraries.)

# Setting up PIPupdate
It's easy. And it isn't a pain in the neck.

* Download the ZIP corresponding to the latest release (usually called pipupdate-versionnumber.zip), and extract it to a folder.
* Linux Users: You can also run the command ```https://github.com/o355/pipupdate.git --depth=1``` to download/extract PIPupdate.
* Open a terminal prompt in that location, and type in ```python pipupdate.py```
* For Linux users, use ```python3 pipupdate.py```
* The updater will do it's thing. If you have lots of packages, grab a snack, it may take a while!
* The speed of the updater will usually depend on your internet connection, more than your computer speed.

# Known Issues/Features to Come
PIPupdate is in it's early stages, and there's still a lot left to fix and add. Generally, here are some issues that need to get addressed, and features that should come.

* PIPupdater doesn't check pip list --outdated first, before updating packages.
* PIPupdater obviously needs the force reinstall/uninstall everything arguments.
* PIPupdater should warn users who are about to do an op with 100+ packages.
* PIPupdater should have the equivalent of pip install -r requirements.txt, but users input packages/version numbers, then the updater compiles it into a file, and does the op on it's own.
* Python 2 compatibility. Right now this is Python 3 or greater only.

# Have a suggestion? See a bug? Want to make additions?
Be sure to report suggestions and bugs with issues.
Send some pull requests as well, if you want to help contribute to the updater!
