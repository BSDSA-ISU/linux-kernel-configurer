import os

def MenuconfigPacman(version):
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cp -rvf PKGBUILD {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {os.cpu_count()} pacman-pkg")
    os.system(f"cd {version} && sudo pacman -U linux*")


#don't mind this
def MenuconfigDebian(version):
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cd {version} && make -j {os.cpu_count()} deb-pkg")


def DefconfigPacman(version):
    os.system(f"zcat /proc/config.gz > {version}/.config")
    os.system(f"cd {version} && make oldconfig -j4")
    print("\n\nfinalize it\n\n")
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cp -rvf PKGBUILD {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {os.cpu_count()} pacman-pkg")
    print("it may ask you that linux-upstream-api-headres and linux-api-headers are in conflict just click y no need 2 worry")
    os.system(f"cd {version} && sudo pacman -U *headers* *linux-upstream-6*")


def LocalModConfigpacman(version):
    os.system(f"cd {version} && make localmodconfig")
    os.system(f"cp -rvf PKGBUILD {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {os.cpu_count()} pacman-pkg")
