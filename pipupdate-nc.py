# PIPupdate 1.0.1-nocolor
# Specific PIPupdate version to run 
# (c) 2016 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate (v1.0)")
print("Loading...")

updatecountint = 0
updatenumber = 0

try:
    import sys
except ImportError:
    raise ImportError("Please install sys to use PIPupdate-nocolor!")

if sys.version_info[0] < 3:
    print("Please use Python 3.0 or greater to use PIPupdate-nocolor!")
    sys.exit()

# In the color script, the PIP install options come up before the Colorama install.
# There's a little except and exit here for proper handling.
# In the event someone just runs the NC script off the bat.
try:
    import pip
except ImportError:
    print("Please install PIP to use PIPupdate-nocolor!")
    print("You can also use the pipinstall.py script to install PIP.")
    sys.exit()

try:
    from subprocess import call
except ImportError:
    print("Please install subprocess/subprocess call to use PIPupdate-nocolor!")
    sys.exit()

for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1

updatenumberstr = str(updatenumber)

for pkgname in pip.get_installed_distributions():
    print("PIPupdate: Now attempting to update package " + pkgname.project_name + "...")
    updatecountint = updatecountint + 1
    updatecountstr = str(updatecountint)
    call("pip install --upgrade " + pkgname.project_name, shell=True)
    print("PIPupdate: Updated package " + pkgname.project_name + ". Progress: " + updatecountstr + "/" + updatenumberstr + " updates")

print("")
print("PIPupdate is done, updated " + updatecountstr + " packages!")
print("Thank you for using PIPupdate!")

