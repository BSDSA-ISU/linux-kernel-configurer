import os

class myclass:
    def myself():
        print()

myclass.myself()

def linuxrc():
    rclink = "https://git.kernel.org/torvalds/t/linux-6.14-rc1.tar.gz"
    if os.path.exists("linux-6.14-rc2.tar.gz") == False:
        os.system(f"wget {rclink}")

def linux613():
    linuxversion = "linux-6.13.2"
    if os.path.exists(linuxversion) == False:
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")

    return linuxversion


def linux612():
    linuxversion = "linux-6.12.13"
    if os.path.exists(linuxversion) == False:
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux66():
    linuxversion = "linux-6.6.76"
    if os.path.exists(linuxversion) == False:
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux61():
    linuxversion = "linux-6.1.128"
    if os.path.exists(linuxversion) == False:
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion
