import os

def MenuconfigPacman():
    os.system("cd linux-6.12.10 && make menuconfig -j4")
    os.system(f"cd linux-6.12.10 && make -j {os.cpu_count()} pacman-pkg")

#don't mind this
def MenuconfigDebian():
    os.system("cd linux-6.12.10 && make menuconfig -j4")
    os.system(f"cd linux-6.12.10 && make -j {os.cpu_count()} deb-pkg")

def DefconfigPacman():
    os.system("cd linux-6.12.10 && make defconfig -j4")
    os.system(f"cd linux-6.12.10 && make -j {os.cpu_count()} pacman-pkg")

def LocalModConfigpacman():
    os.system("cd linux-6.12.10 && make localmodconfig")
    os.system(f"cd linux-6.12.10 && make -j {os.cpu_count()} pacman-pkg")
