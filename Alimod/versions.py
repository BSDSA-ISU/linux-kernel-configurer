import os


def linux613():
    os.system("wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.13.tar.xz'")
    os.system("tar -xvf linux-6.13.tar.xz")

    return "linux-6.13"


def linux612():
    os.system("wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.12.10.tar.xz'")
    return "linux-6.12.10"

def linux66():
    return "linux-6.6.73"

def linux61():
    return "linux-6.1.126"

def linux515():
    return "linux-5.15.176"