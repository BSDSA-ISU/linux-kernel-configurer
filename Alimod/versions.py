import os
import requests

class myclass:
    @staticmethod
    def myself():
        print()

myclass.myself()


class Version:
    @staticmethod
    def linuxrc():
        linuxversion = "linux-6.15.1"
        rclink = f"https://cdn.kernel.org/pub/linux/kernel/x6.x/{linuxversion}.tar.xz"
        if os.path.exists("linux-6.15.1.tar.gz") == False:
            os.system(f"wget https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def linuxdownload(linuxversion):
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")

        return linuxversion

    @staticmethod
    def linux612():
        linuxversion = "linux-6.12.32"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def getver(numbr):
        url = f"https://raw.githubusercontent.com/AlieeLinux/linux-6.12.X/refs/heads/main/versions/{numbr}"
        response = requests.get(url)

        if response.status_code == 200:
            version = response.text.strip()
            return version
        else:
            print("no version available. exiting...")
            exit(9)
    
    def fetchver(self, kerneltype):
        if kerneltype == "12lts":
            ver = "linux612lts"
        elif kerneltype == "stable":
            ver = "linuxstable"

        version = Version.getver(ver)
        Version.linuxdownload(version)


    
'''
    @staticmethod
    def linux66():
        linuxversion = "6.6.80"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def linux61():
        linuxversion = "linux-6.1.129"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

    @staticmethod
    def linux515():
        linuxversion = "linux-5.15.178"
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")
        return linuxversion

'''
