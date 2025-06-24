import os

def MenuconfigPacmanrc(version):
    print(version)
    x = input("how many cpu cores(1, 2, 3, 4, 5 etc)? \n>>")
    os.system(f"cd {version} && make menuconfig -j {x}")
    os.system(f"cp -rvf install/releasecandidate/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {x} tar-pkg")
    os.system(f"cd {version} && makepkg --cleanbuild -si")

def DefconfigPacmanrc(version):
    x = input("how many cpu cores(1, 2, 3, 4, 5 etc)? \n>>")
    os.system(f"zcat /proc/config.gz > {version}/.config")
    os.system(f"cd {version} && make oldconfig -j {x} ")
    print("\n\nfinalize it\n\n")
    os.system(f"cd {version} && make menuconfig -j {x}")
    os.system(f"cp -rvf install/releasecandidate/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {x} tar-pkg")
    print("it may ask you that linux-upstream-api-headres and linux-api-headers are in conflict just click y no need 2 worry")
    os.system(f"cd {version} && makepkg --cleanbuild -si")


def LocalModConfigpacmanrc(version):
    x = input("how many cpu cores(1, 2, 3, 4, 5 etc)? \n>>")
    os.system(f"cd {version} && make localmodconfig")
    os.system(f"cp -rvf install/releasecandidate/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {x} tar-pkg")
    os.system(f"cd {version} && makepkg --cleanbuild -si")

def DirectCompilerc(version):
    x = input("how many cpu cores(1, 2, 3, 4, 5 etc)? \n>>")
    os.system(f"cp -rvf install/releasecandidate/* {version}")
    os.system(f"vim {version}/PKGBUILD")
    os.system(f"cd {version} && make -j {x} tar-pkg")
    os.system(f"cd {version} && makepkg --cleanbuild -si")

def CopyCheck(version):
    if os.path.isfile(f"{version}/linux.install") or os.path.isfile(f"{version}/package.preset") or os.path.isfile(f"{version}/PKGBUILD"):
        pass
    else:
        os.system(f"cp -rvf install/releasecandidate/* {version}")