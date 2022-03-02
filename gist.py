#!/bin/python3

# this gist is intended to run on PythonAnywhere

print("\nPreparing ... please be patient ...\n")

import subprocess
subprocess.check_call("git clone https://github.com/drandreaskrueger/plutoalert", shell=True)
subprocess.check_call("cd plutoalert; pip install -r requirements.txt", shell=True)

import sys
sys.path.append("./plutoalert/plutoalert")
import plutotv

print()
print("Done. Run: ...")
print()
plutotv.the_purpose_of_all_this_v2()
