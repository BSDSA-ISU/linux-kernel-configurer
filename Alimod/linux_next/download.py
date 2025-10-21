import os
import requests
import subprocess

class Version:
    @staticmethod
    def linuxdownload(linuxversion):
        if os.path.exists(linuxversion) == False:
            os.system(f"wget -c 'https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/snapshot/{linuxversion}.tar.gz'")
            i = Version.verity()

            if int(i) != 0:
                print("verification Failed.")
                exit(8)
            else:
                os.system(f"tar -xvf {linuxversion}.tar.gz")

        return linuxversion

# https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/snapshot/linux-next-next-20250904.tar.gz

    @staticmethod
    def getver(numbr):
        url = f"https://raw.githubusercontent.com/BSDSA-ISU/linux-kernel-configurer/refs/heads/main/versions/{numbr}"
        response = requests.get(url)

        if response.status_code == 200:
            version = response.text.strip()
            return version
        else:
            print("no version available. exiting...")
            exit(9)

    @staticmethod
    def verity():
        # no need for gpg verify
        return 0

    @staticmethod
    def fetchver(kerneltype:str):
        version = Version.getver(kerneltype)
        Version.linuxdownload(version)
        return version

