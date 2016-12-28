# PIPupdate 1.0
# (c) 2016 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate (v1.0)")
print("Loading...")
#Declaring number vars
updatecountint = 0
updatenumber = 0
#Try/Except for proper handling of possible import errors
try:
    import sys
except ImportError:
    raise ImportError("Please install sys to use PIPupdate!")
try:
    import pip
except ImportError:
    # We ask for an input, and determine if the user wants PIP installed.
    # To keep things organized, we launch an external script that installs PIP for them.
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
try:
    from subprocess import call
except ImportError:
    print("Please install subprocess/subprocess call to use PIPupdate!")
    sys.exit()
#Here we find out how many packages we need to install
for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1
#Run the int -> str conversion for printing progress
updatenumberstr = str(updatenumber)
#Run the loop, and the updater does it's thing.
for pkgname in pip.get_installed_distributions():
    print("PIPupdate: Now attempting to update package " + pkgname.project_name)
    print("")
    updatecountint = updatecountint + 1
    updatecountstr = str(updatecountint)
    call("pip install --upgrade " + pkgname.project_name, shell=True)
    print("")
    print("PIPupdate: Updated package " + pkgname.project_name + " successfully (finished " + updatecountstr + "/" + updatenumberstr + " updates so far.)")

print("")
print("PIPupdate is done, upgraded " + updatecountstr + " packages!")
print("Thank you for using PIPupdate!")
