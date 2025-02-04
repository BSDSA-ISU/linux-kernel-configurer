from Alimod.troysrc import LocalModConfigpacman, DefconfigPacman, MenuconfigPacman
from Alimod import versions
from Alimod import clean


def main():
    clean.clean()
    print("What version of linux Do you want to install? \n")
    print("(0) Release Candidated 1 Linux 6.14")
    print("(1) mainline Linux 6.13")
    print("(2) LTS Soon Linux 6.12")
    print("(3) LTS Linux 6.6")
    print("(4) LTS Linux 6.1")

    try:
        version = int(input(">>"))
    except ValueError:
        print("error pick a valid shit")
        return 2

    if version >= 5:
        print("error. pick a valid shit")
        return 9

    if version == 0:
        vername = versions.linuxrc()

    elif version == 1:
        vername = versions.linux613()
        print(vername)
    elif version == 2:
        vername = versions.linux612()
    elif version == 3:
        vername = versions.linux66()
    elif verson == 4:
        vername = versions.linux61()

    print("how do you want to start configure your kernel? \n")
    print("(0) default from /proc/config.gz")
    print("(1) manual")
    print("(2) based on modules/feature that are used by this machine(make sure to turn on every mod you need)")

    how = int(input(">>"))
    if how == 0:
        DefconfigPacman(vername)
    elif how == 1:
        MenuconfigPacman(vername)
    elif how == 2:
        LocalModConfigpacman(vername)


main()
#
# pacman()
