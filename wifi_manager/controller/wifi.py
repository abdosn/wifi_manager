import subprocess

def scan_networks():
    result = subprocess.run(["nmcli", "-t", "-f", "SSID,SIGNAL", "device", "wifi", "list"],
                            stdout=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split("\n")
    return [line.split(":") for line in lines if line]

def connect_to_wifi(ssid, password):
    cmd = ["nmcli", "dev", "wifi", "connect", ssid, "password", password]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0, result.stdout or result.stderr
