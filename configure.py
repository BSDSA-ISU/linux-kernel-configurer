from Alimod.linux import LocalModConfigpacman, DefconfigPacman, MenuconfigPacman, DirectCompile
from Alimod.versions import Version
from Alimod import clean
from Alimod.linuxrc import LocalModConfigpacmanrc, DefconfigPacmanrc, MenuconfigPacmanrc, DirectCompilerc
from Alimod.linux5 import LocalModConfigpacman5, DefconfigPacman5, MenuconfigPacman5, DirectCompile5

version = Version()

def main():
    clean.clean()
    print("What version of linux Do you want to install? \n")
    print("(0) Rc Linux")
    print("(1) Stable Linux 6.14")
    print("(2) LTS Linux 6.12")
    print("(3) Linux LTS 6.6")
    print("(4) Linux LTS 6.1")
    print("(5) Linux LTS 5.15")
    print("(6) Linux LTS 5.10")
    print("(7) Linux LTS 5.4")
    try:
        dversion = int(input(">>"))
    except ValueError:
        print("error pick a valid shit")
        return 2

    if dversion >= 8:
        print("error. pick a valid shit")
        return 9

    if dversion == 0:
        vername = "linuxrc"
    elif dversion == 1:
        vername = "stable"
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

    if 1 <=  dversion >= 5:
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

    if dversion == 0:
        if how == 0:
            DefconfigPacmanrc(kver)
        elif how == 1:
            MenuconfigPacmanrc(kver)
        elif how == 2:
            LocalModConfigpacman5(kver)
        elif how == 3:
            DirectCompile5(kver)

    elif 1 <= dversion <=6:
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

