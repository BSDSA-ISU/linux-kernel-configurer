import os
import requests

class Version:
    @staticmethod
    def linuxdownload(linuxversion):
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
