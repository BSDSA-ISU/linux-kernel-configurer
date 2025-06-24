import os
import requests

class Version:
    @staticmethod
    def linuxdownload(linuxversion):
        if os.path.exists(linuxversion) == False or "rc" in linuxversion:
            os.system(f"wget 'https://git.kernel.org/torvalds/t/{linuxversion}.tar.gz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")

        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")

        return linuxversion

    @staticmethod
    def linuxdownload5(linuxversion):
        if os.path.exists(linuxversion) == False or "rc" in linuxversion:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v5.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")

        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://cdn.kernel.org/pub/linux/kernel/v5.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.xz")

        return linuxversion

    @staticmethod
    def linuxdownloadrc(linuxversion):
        if os.path.exists(linuxversion) == False:
            os.system(f"wget 'https://git.kernel.org/torvalds/t/{linuxversion}.tar.gz'")
            os.system(f"tar -xvf {linuxversion}.tar.gz")

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

    def fetchver(self, kerneltype:str):
        version = Version.getver(kerneltype)
        Version.linuxdownload(version)
        return version

    def fetchver5(self, kerneltype:str):
        version = Version.getver(kerneltype)
        Version.linuxdownload5(version)
        return version

    def fetchverrc(self, kerneltype:str):
        version = Version.getver(kerneltype)
        Version.linuxdownloadrc(version)
        return version
