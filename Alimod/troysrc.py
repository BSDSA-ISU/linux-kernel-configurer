import os

def MenuconfigPacman(version):
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cd {version} && make -j {os.cpu_count()} pacman-pkg")

#don't mind this
def MenuconfigDebian(version):
    os.system(f"cd {version} && make menuconfig -j4")
    os.system(f"cd {version} && make -j {os.cpu_count()} deb-pkg")

def DefconfigPacman(version):
    os.system(f"cd {version} && make defconfig -j4")
    os.system(f"cd {version} && make -j {os.cpu_count()} pacman-pkg")

def LocalModConfigpacman(version):
    os.system(f"cd {version} && make localmodconfig")
    os.system(f"cd {version} && make -j {os.cpu_count()} pacman-pkg")
