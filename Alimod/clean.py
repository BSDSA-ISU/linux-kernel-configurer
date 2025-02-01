import os
from os.path import isdir

def clean():
    print("cleaning previous builds")
    for files in os.listdir():
        try:
            if isdir(files):
                os.system(f"rm -rvf {files}/linux-upstream*")
        except FileNotFoundError:
            continue

