# PIPupdate-installPIP 1.1.0
# External asset to PIPupdate.
# (c) 2016-2017 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate-installPIP (1.1.0)!")
print("Now installing PIP.")
try:
    import sys
except ImportError:
    raise ImportError("Please install PIP to use PIPupdate-installPIP!")

if sys.version_info[0] < 3:
    print("Please use Python 3.0 or greater to use PIPupdate-installPIP!")
    sys.exit()

try:
    import urllib.request
except ImportError:
    print("Please install urllib.request to use PIPupdate-installPIP!")
    sys.exit()
    
try:
    import shutil
except ImportError:
    print("Please install shutil to use PIPupdate-installPIP!")
    sys.exit()
    
try:
    import time
except ImportError:
    print("Please install time to use PIPupdate-installPIP!")
    sys.exit()
    
print("Now downloading the PIP installer...")
try:
    with urllib.request.urlopen('https://bootstrap.pypa.io/get-pip.py') as update_response, open('get-pip.py', 'wb') as update_out_file:
        shutil.copyfileobj(update_response, update_out_file)
except:
    print("The PIP installer could not be fetched, either due to a urllib failure, or you don't have an internet connection.",
          "Please attempt to download the installer from this url: 'https://bootstrap.pypa.io/get-pip.py'.",
          "Save the file in the pipupdate directory. When this process is complete, press enter to continue. Otherwise, press",
          "Control + C to exit.", sep="\n")
    input()
    
print("Now running the PIP installer...")
print("Please note: get-pip.py is not developed or maintained by myself.")
print("Please note: This script will quit out of PIPupdate. Please relaunch PIPupdate when the script is quitted.")
print("Starting in 2 seconds...")
time.sleep(2)

exec(open("get-pip.py").read())
print("PIP install complete. Returning to PIPupdate!")
