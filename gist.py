#!/bin/python3.7

# this gist
# https://gist.github.com/drandreaskrueger/94d3b92d57976da77ae2753b45314aeb
# is intended to run at PythonAnywhere
# https://www.pythonanywhere.com/gists/94d3b92d57976da77ae2753b45314aeb/plutoalert_StarTrek.py/python3/
#
# but see the 'sorry, EMPTY RESULT' info in
# README.md --> Geoblocking --> Python online execution environments: pythonanywhere

print("\nPreparing ... please be patient ...\n")

import subprocess
subprocess.check_call("git clone https://github.com/drandreaskrueger/plutoalert", shell=True)
subprocess.check_call("cd plutoalert; pip3.7 install -r requirements-minimum.txt", shell=True)

print()
print("Installation done. Run: ...")
print()

import sys
sys.path.append("./plutoalert/plutoalert")
import plutotv
plutotv.the_purpose_of_all_this_v2()
