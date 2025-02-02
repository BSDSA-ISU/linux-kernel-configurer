import os


def linux613():
    linuxversion = "linux-6.13.1"
    if os.path.exists(linuxversion):
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")

    return linuxversion


def linux612():
    linuxversion = "linux-6.12.12"
    if os.path.exists(linuxversion) == False:
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux66():
    linuxversion = "linux-6.6.75"
    if os.path.exists(linuxversion):
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion

def linux61():
    linuxversion = "linux-6.1.128"
    if os.path.exists(linuxversion):
        os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        os.system(f"tar -xvf {linuxversion}.tar.xz")
    return linuxversion
