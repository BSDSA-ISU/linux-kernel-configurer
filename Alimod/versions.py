import os


def linux613():
    linuxversion = "linux-6.13"
    if os.path.exists(linuxversion):
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")

    return linuxversion


def linux612():
    linuxversion = "linux-6.12.11"
    if os.path.exists(linuxversion) == False:
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux66():
    linuxversion = "linux-6.6.74"
    if os.path.exists(linuxversion):
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux61():
    linuxversion = "linux-6.1.127"
    return "linux-6.1.127"
