from Alimod import linux
from Alimod.linux import LocalModConfigpacman, DefconfigPacman, MenuconfigPacman, DirectCompile
from Alimod.versions import Version
from Alimod import clean
from Alimod.linuxrc import LocalModConfigpacmanrc, DefconfigPacmanrc, MenuconfigPacmanrc, DirectCompilerc
from Alimod.linux5 import LocalModConfigpacman5, DefconfigPacman5, MenuconfigPacman5, DirectCompile5
from Alimod.linux_next import download as fetch_next
from Alimod.linux_next import linux as linux_next

version = Version()

def main():
    clean.clean()
    print("What version of linux Do you want to install? \n")
    print("(0) Rc Linux")
    print("(1) stable Linux 6.16")
    print("(2) LTS Linux 6.12")
    print("(3) Linux LTS 6.6")
    print("(4) Linux LTS 6.1")
    print("(5) Linux LTS 5.15")
    print("(6) Linux LTS 5.10")
    print("(7) Linux LTS 5.4")
    print("(8) Linux next")
    try:
        dversion = int(input(">>"))
    except ValueError:
        print("error pick a valid shit")
        return 2

    if dversion >= 9:
        print("error. pick a valid shit")
        return 9

    if dversion == 0:
        vername = "linuxrc"
    elif dversion == 1:
        vername = "linuxstable"
    elif dversion == 2:
        vername = "linux612lts"
    elif dversion == 3:
        vername = "linux66lts"
    elif dversion== 4:
        vername = "linux61lts"
    elif dversion == 5:
        vername = "linux515lts"
    elif dversion == 6:
        vername = "linux510lts"
    elif dversion == 7:
        vername = "linux54lts"
    elif dversion == 8:
        vername = "linux_next"

    if dversion == 8:
        kver = fetch_next.Version.fetchver(vername)
    elif  dversion >= 5:
        kver = version.fetchver5(vername)
    elif dversion == 0:
        kver = version.fetchverrc(vername)
    else:
        kver = version.fetchver(vername)


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

