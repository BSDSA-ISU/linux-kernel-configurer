import requests

url = "https://raw.githubusercontent.com/AlieeLinux/linux-6.12.X/refs/heads/main/versions/linux612"
response = requests.get(url)

if response.status_code == 200:
    version = response.text.strip()
    print("Version:", version)
else:
    print("Failed to retrieve the file.")
