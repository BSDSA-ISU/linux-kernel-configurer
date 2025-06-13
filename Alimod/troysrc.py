import os

def MenuconfigPacman(version):
    x = input("how many cpu cores(1, 2, 3, 4, 5 etc)? \n>>")
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cp -rvf install/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {x} tar-pkg")
    os.system(f"cd {version} && makepkg --cleanbuild -si")
    #os.system(f"cd {version} && sudo pacman -U *tar")


#don't mind this
def MenuconfigDebian(version):
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cd {version} && make -j {os.cpu_count()} deb-pkg")


def DefconfigPacman(version):
    x = input("how many cpu cores(1, 2, 3, 4, 5 etc)? \n>>")
    os.system(f"zcat /proc/config.gz > {version}/.config")
    os.system(f"cd {version} && make oldconfig -j4")
    print("\n\nfinalize it\n\n")
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cp -rvf install/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {x} tar-pkg")
    print("it may ask you that linux-upstream-api-headres and linux-api-headers are in conflict just click y no need 2 worry")
    os.system(f"cd {version} && makepkg --cleanbuild -si")


def LocalModConfigpacman(version):
    os.system(f"cd {version} && make localmodconfig")
    os.system(f"cp -rvf install/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {os.cpu_count()} tar-pkg")
    os.system(f"cd {version} && makepkg --cleanbuild -si")
