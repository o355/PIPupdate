#PIPupdate
#(c) 2016 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate (v0.9)")
print("Loading...")
updatecountint = 0
updatenumber = 0
try:
    import pip
except ImportError:
    print("Please install PIP to use PIPupdate!")
    sys.exit()
import sys
from subprocess import call
for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1
updatenumberstr = str(updatenumber)
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
