# PIPupdate 1.0.2
# (c) 2016 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate (v1.0.2)")
print("Loading...")
    
updatecountint = 0
updatenumber = 0

try:
    import sys
except ImportError:
    raise ImportError("Please install sys to use PIPupdate!")

if sys.version_info[0] < 3:
    print("Please use Python 3.0 or greater to use PIPupdate!")
    sys.exit()

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
        
try:
    from subprocess import call
except ImportError:
    print("Please install subprocess/subprocess call to use PIPupdate!")
    sys.exit()
    
try:
    from colorama import init, Fore, Style
except ImportError:
    print("Shucks. PIPupdate is dependent on Colorama to run. Would you like me to install Colorama for you?")
    coloramainstall = input("Yes or No: ").lower()
    if coloramainstall == "yes":
        print("Alright. Installing Colorama now!")
        pip.main(['install', 'colorama'])
        try:
            from colorama import init, Fore, Style
            print("Installed Colorama!")
        except ImportError:
            print("Colorama wasn't installed...")
            print("Please try running 'pip install colorama' in a Python terminal.")
            sys.exit()
    elif coloramainstall == "no":
        print("Alright. Would you like me to run the colorless version of PIPupdate?")
        colorlessrun = input("Yes or No: ").lower()
        if colorlessrun == "yes":
            print("Running the colorless version of PIPupdate!")
            exec(open("pipupdate-nc.py").read())
        elif colorlessrun == "no":
            print("Not running the colorless version of PIPupdate.")
            print("Exiting now...")
            sys.exit()
        else:
            print("I couldn't understand what you inputted.")
            print("I'll assume you didn't want to run the colorless version. Exiting now!")
            sys.exit()
    else:
        print("I couldn't understand what you inputted.")
        print("I'll assume you didn't want to install Colorama. Exiting now!")
        sys.exit()
        
init()
for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1
    
updatenumberstr = str(updatenumber)

for pkgname in pip.get_installed_distributions():
    print(Fore.GREEN + Style.BRIGHT + "PIPupdate: Now attempting to update package " + pkgname.project_name + "..." + Style.RESET_ALL)
    updatecountint = updatecountint + 1
    updatecountstr = str(updatecountint)
    call("pip install --upgrade " + pkgname.project_name, shell=True)
    print(Fore.GREEN + Style.BRIGHT + "PIPupdate: Updated package " + pkgname.project_name + ". Progress: " + updatecountstr + "/" + updatenumberstr + " updates")

print(Style.RESET_ALL)
print("PIPupdate is done, updated " + updatecountstr + " packages!")
print("Thank you for using PIPupdate!")
