# PIPupdate 0.9.1
# (c) 2016 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate (v0.9.1)")
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
    # And I realized that instead of a thrown error, maybe I'll install PIP for the user!
    print("Please install PIP to use PIPupdate!")
    sys.exit()
try:
    from subprocess import call
except ImportError:
    print("Please install subprocess/subprocess call to use PIPupdate!")
    sys.exit()
#Here we find out how many packages we need to install
for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1
#Run the int -> str conversion
updatenumberstr = str(updatenumber)
#Run the loop, gets the package name for each package.
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
