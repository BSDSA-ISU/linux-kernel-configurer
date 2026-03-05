import re
import requests
import os
import subprocess

def GetVersion(version):
    """
    Fumo segggsss!!!!!!!!!!!
    """
    URL = f"https://www.kernel.org/pub/linux/kernel/v6.x/"

    html = requests.get(URL, timeout=10).text

    # Use the version argument dynamically in the regex
    pattern = rf'linux-({re.escape(version)}\.\d+)\.tar\.xz'
    matches = re.findall(pattern, html)

    if not matches:
        print(f"No {version}.x versions found")
        return None
    else:
        # Sort numerically
        def version_key(v):
            return tuple(map(int, v.split(".")))

        latest = sorted(set(matches), key=version_key)[-1]
        return latest


def GetVersion5(version):
    """
    Fumo segggsss!!!!!!!!!!!
    """
    URL = f"https://www.kernel.org/pub/linux/kernel/v5.x/"

    html = requests.get(URL, timeout=10).text

    # Use the version argument dynamically in the regex
    pattern = rf'linux-({re.escape(version)}\.\d+)\.tar\.xz'
    matches = re.findall(pattern, html)

    if not matches:
        print(f"No {version}.x versions found")
        return None
    else:
        # Sort numerically
        def version_key(v):
            return tuple(map(int, v.split(".")))

        latest = sorted(set(matches), key=version_key)[-1]
        return latest

def linuxdownload(linuxversion):
    if os.path.exists(linuxversion) == False:
        getkey(linuxversion)
        os.system(f"wget -c 'https://cdn.kernel.org/pub/linux/kernel/v6.x/{linuxversion}.tar.xz'")
        i = verity(linuxversion)

        if int(i) != 0:
            print("verification Failed.")
            exit(8)
        else:
            os.system(f"tar -xvf {linuxversion}.tar")

    return linuxversion

def linuxdownload5(linuxversion):
    if os.path.exists(linuxversion) == False:
        getkey(linuxversion)
        os.system(f"wget -c 'https://cdn.kernel.org/pub/linux/kernel/v5.x/{linuxversion}.tar.xz'")
        i = verity(linuxversion)

        if int(i) != 0:
            print("verification Failed.")
            exit(8)
        else:
            os.system(f"tar -xvf {linuxversion}.tar")

    return linuxversion

def getkey(version):
    os.system(f"wget -c https://cdn.kernel.org/pub/linux/kernel/v6.x/{version}.tar.sign")

def verity(version):
    subprocess.run(["unxz", "-T", "0", f"{version}.tar.xz"])
    s = subprocess.run(["gpg2", "--verify", f"{version}.tar.sign"])
    return s.returncode



if __name__ == "__main__":
    a = GetVersion5("6.18")
    print(a)