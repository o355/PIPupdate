#PIPupdate
#(c) 2016 o355 under the GNU GPL 3.0

import sys
print("Welcome to PIPupdate (v0.9).")
print("Loading...")
try:
    import pip
except ImportError:
    print("Please install PIP to use PIPupdate!")
    sys.exit()

for pkgname in pip.get_installed_distributions():
    print("Now attempting to update package " + pname.project_name)
    call("pip install --upgrade " + pname.project_name, shell=True)
    updates + 1
    print("Updated package " + pname.project_name + " successfully (finished", updates, "updates so far.)")

print("PIPupdate is done!")
