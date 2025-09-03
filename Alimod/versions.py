import os
import requests
import subprocess

class Version:
    @staticmethod
    def linuxdownload(linuxversion):
        if os.path.exists(linuxversion) == False:
            Version.getkey(linuxversion)
            os.system(f"wget -c 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
            i = Version.verity(linuxversion)

            if int(i) != 0:
                print("verification Failed.")
                exit(8)
            else:
                os.system(f"tar -xvf {linuxversion}.tar")

        return linuxversion

    @staticmethod
    def linuxdownload5(linuxversion):
        if os.path.exists(linuxversion) == False or "rc" in linuxversion:
            os.system(f"wget -c 'https://cdn.kernel.org/pub/linux/kernel/v5.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.gz")

        if os.path.exists(linuxversion) == False:
            os.system(f"wget -c 'https://cdn.kernel.org/pub/linux/kernel/v5.x/{linuxversion}.tar.xz'")
            os.system(f"tar -xvf {linuxversion}.tar.gz")

        return linuxversion

    @staticmethod
    def linuxdownloadrc(linuxversion):
        if os.path.exists(linuxversion) == False:
            os.system(f"wget -c 'https://git.kernel.org/torvalds/t/{linuxversion}.tar.gz'")
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

    @staticmethod
    def verity(version):
        subprocess.run(["unxz", "-T", "0", f"{version}.tar.xz"])
        s = subprocess.run(["gpg2", "--verify", f"{version}.tar.sign"])
        return s.returncode

    @staticmethod
    def getkey(version):
        os.system(f"wget -c https://cdn.kernel.org/pub/linux/kernel/v6.x/{version}.tar.sign")

    @staticmethod
    def getkey5(version):
        os.system(f"wget -c https://cdn.kernel.org/pub/linux/kernel/v5.x/{version}.tar.sign")


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


