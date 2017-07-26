# PIPupdate 1.1.0-nocolor
# Specific PIPupdate version to run 
# (c) 2016-2017 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate-nocolor (v1.1.0)!")
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
    print("Shucks. PIP isn't installed. Would you like me to install PIP for you?")
    pipinstall = input("Yes or No: ").lower()
    if pipinstall == "yes":
        print("Alright. Installing PIP now!")
        exec(open("pipinstall.py").read())
    elif pipinstall == "no":
        print("Alright. Not installing PIP, exiting PIPupdate.")
        sys.exit()
    else:
        print("I couldn't understand what you inputted.")
        print("I'll assume you didn't want to install PIP, exiting now.")
        sys.exit()

for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1

updatenumberstr = str(updatenumber)

for pkgname in pip.get_installed_distributions():
    print("PIPupdate: Now attempting to update package " + pkgname.project_name + "...")
    updatecountint = updatecountint + 1
    updatecountstr = str(updatecountint)
    try:
        pip.main(['install', '--upgrade', pkgname.project_name])
        print("PIPupdate: Updated package " + pkgname.project_name + ". Progress: " + updatecountstr + "/" + updatenumberstr + " updates")
    except:
        print("PIPupdate: Failed to update package " + pkgname.project_name + ". Progress: " + updatecountstr + "/" + updatenumberstr + " updates")

print("")
print("PIPupdate is done, updated " + updatecountstr + " packages!")
print("Thank you for using PIPupdate!")

