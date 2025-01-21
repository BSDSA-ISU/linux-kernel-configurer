from Alimod.troysrc import LocalModConfigpacman, DefconfigPacman
import os
from Alimod import versions



def main():
    print("What version of linux Do you want to install? \n")
    print("(0) Release Candidated Linux (not available for now)")
    print("(1) mainline Linux 6.13")
    print("(2) LTS Linux 6.12")
    print("(3) LTS Linux 6.6")
    print("(4) LTS Linux 6.1")
    print("(5) LTS Linux 5.15")

    try:
        version = int(input(">>"))
    except ValueError:
        print("error pick a valid shit")
        return 2

    if version > 8:
        print("error. pick a valid shit")

        exit

    if version == 0:
        print("still no rc release out there yet.")

    elif version == 1:
        vername = versions.linux613()
        print(vername)

    print("how do you want to start configure your kernel? \n")
    print("(0) default from /proc/config.gz")
    print("(1) manual")
    print("(2) based on modules/feature that are used by this machine(make sure to turn on every mod you need)")

    how = int(input(">>"))
    if how == 0:
        DefconfigPacman(vername)
main()
#
# pacman()