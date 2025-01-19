import asyncio
import os
import subprocess

async def bash(command):
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if stdout:
        print(f"{stdout.decode()}")
        return 0
    if stderr:
        print(f"{stderr.decode()}")
        return 1

def menuconfig():
    syn = os.system("cd linux-6.12.10 && make menuconfig -j4")
    nproc = asyncio.run(bash("nproc"))
    os.system(f"cd linux-6.12.10 && make -j {os.cpu_count()}")