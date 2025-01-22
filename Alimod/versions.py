import os


def linux613():
    linuxversion = "linux-6.13"
    if os.path.exists(linuxversion):
        os.system("wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.13.tar.xz'")
        os.system("tar -xvf linux-6.13.tar.xz")

    return linuxversion


def linux612():
    linuxversion = "linux-6.12.10"
    if os.path.exists(linuxversion) == False:
        os.system("wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.12.10.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux66():
    return "linux-6.6.73"
