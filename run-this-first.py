#!/usr/bin/env python3

import os
import time
import random
import sys
import re
import subprocess as sbp

def install_nvidia_drivers():
    # TODO write this function
    ...

# TODO check that dnf exists (are we running on fedora?)
# TODO check that we are running an up-to-date version of fedora

current_fedora_desktop_version = open("fedora_supported_version.txt", "r").read()

# get the version this script is running on from /etc/os-release

os_release_file = open("/etc/os-release", "r").read()
found_version = ""
for i in os_release_file.splitlines():
    if str(i).startswith("VERSION_ID="):
        if i.split("=") ==  current_fedora_desktop_version:
            found_version = i
            pass
        else:
            print("update to the most modern version of fedora before running these scripts")
            exit()
    else:
        pass
if found_version:
    pass
else:
    print("could not find fedora version in /etc/os-release, quitting!")
    exit()

# now, make sure the system is completetly up-to-date
os.system("sudo dnf update -y")

# check if an nvidia card is installed
install_lspci = ""
try:
    open("/usr/bin/lspci", "r")
except:
    while True:
        print("could not run (lspci), install 'pciutils' package?")
        ans = input("yes or no: ")
        if ans.lower().repace(" ", "") == "yes":
            print("installing pciutils with dnf in: ")
            counter = 5
            for i in range(5):

                sys.stdout.write(str(counter))
                sys.stdout.write("..")
                sys.stdout.flush()
                time.sleep(1)
                counter = counter - 1
            os.system("sudo dnf install pciutils -y")

            install_lspci = True
            break


        if ans.lower().replace(" ", "")  == "no":
            print("WARNING: continuing without detecting graphics card info!")
            install_lspci = False
            break
        else:
            print("answer (yes) or (no) without the parenthesis")
            continue

if install_lspci:
    print("attempting to detect installed graphics card")

    output = os.system("lspci").read()

    while True:
        if "NVIDIA" in output:
            print("nvidia card detected, would you like to install the proprietary drivers from rpmfusion?")
            

            answer = input("yes or no: ")
            if answer == "yes":
                try:
                    install_nvidia_drivers()
                except:
                    print("couldn't install proprietary nvidia drivers. Continue?")








