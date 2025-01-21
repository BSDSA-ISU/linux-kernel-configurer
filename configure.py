from Alimod.troysrc import MenuconfigPacman as pacman
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
    print("(6) LTS Linux 5.10")
    print("(7) LTS Linux 5.4")
    try:
        version = int(input(">>"))
    except ValueError:
        print("error pick a valid shit")
        return 2

    if version > 8:
        print("error. pick a valid shit")
        exit
    print("how do you want to start configure your kernel? \n")
    print("(0) default from /proc/config.gz")
    print("(1) manual")
    print("(2) ")
    
    versions.linux612()


main()
#
# pacman()