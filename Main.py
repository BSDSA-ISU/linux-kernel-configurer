from Alimod.linux import LocalModConfigpacman, DefconfigPacman, MenuconfigPacman, DirectCompile
from Alimod.versions import Version
from Alimod import clean
from Alimod.linuxrc import LocalModConfigpacmanrc, DefconfigPacmanrc, MenuconfigPacmanrc, DirectCompilerc
from Alimod.linux5 import LocalModConfigpacman5, DefconfigPacman5, MenuconfigPacman5, DirectCompile5
from Alimod.linux_next import download as fetch_next
from Alimod.linux_next import linux as linux_next
import sys
from Alimod.GetVer import GetVersion as getver, linuxdownload, linuxdownload5, GetVersion5 as getver5, releasecandidate, linuxdownloadrc

version = Version()

def main():
    print("What version of linux Do you want to install? \n")
    print("(0) Rc Linux")
    print("(1) Stable Linux 6.19")
    print("(2) Linux LTS 6.18")
    print("(3) Linux LTS 6.12")
    print("(4) Linux LTS 6.6")
    print("(5) Linux LTS 6.1")
    print("(6) Linux LTS 5.15")
    print("(7) Linux LTS 5.10")
    print("(8) Linux LTS 5.4")
    print("(9) Clean build and source Files")

    try:
        dversion = int(input(">>"))
    except ValueError:
        print("error pick a valid shit")
        return 2

    if dversion == 9:
        clean.clean()
        main()

    if dversion >= 10:
        print("error. pick a valid shit")
        return 9

    if dversion == 0:
        vername = "linuxrc"
    if dversion == 1:
        vername = "6.19"
    elif dversion == 2:
        vername = "6.18"
    elif dversion == 3:
        vername = "6.12"
    elif dversion == 4:
        vername = "6.6"
    elif dversion== 5:
        vername = "6.1"
    elif dversion == 6:
        vername = "5.15"
    elif dversion == 7:
        vername = "5.10"
    elif dversion == 8:
        vername = "5.4"
    elif dversion == 9:
        vername = "linux_next"

    if dversion < 6 and dversion != 0:
        kver = f"linux-{getver(vername)}"
        linuxdownload(kver)

    elif dversion == 0:
        kver = releasecandidate(vername)

        linuxdownloadrc(kver)
    else:
        kver = f"linux-{getver5(vername)}"
        linuxdownload5(kver)

    print("how do you want to start configure your kernel? \n")
    print("(0) default from /proc/config.gz")
    print("(1) manual")
    print("(2) based on modules/feature that are used by this machine(make sure to turn on every mod you need)")
    print("(3) Direct compile(do nothing)")

    how = int(input(">>"))

    if dversion == 8:
        if how == 0:
            linux_next.DefconfigPacman(kver)
        elif how == 1:
            linux_next.MenuconfigPacman(kver)
        elif how == 2:
            linux_next.LocalModConfigpacman(kver)
        elif how == 3:
            linux_next.DirectCompile(kver)


    elif dversion == 0:
        if how == 0:
            DefconfigPacmanrc(kver)
        elif how == 1:
            MenuconfigPacmanrc(kver)
        elif how == 2:
            LocalModConfigpacmanrc(kver)
        elif how == 3:
            DirectCompilerc(kver)

    elif dversion >=5:
        if how == 0:
            DefconfigPacman5(kver)
        elif how == 1:
            MenuconfigPacman5(kver)
        elif how == 2:
            LocalModConfigpacman5(kver)
        elif how == 3:
            DirectCompile5(kver)

    else:
        if how == 0:
            DefconfigPacman(kver)
        elif how == 1:
            MenuconfigPacman(kver)
        elif how == 2:
            LocalModConfigpacman(kver)
        elif how == 3:
            DirectCompile(kver)

try:
    main()
except KeyboardInterrupt:
    print("canceled")
except Exception:
    raise Exception


