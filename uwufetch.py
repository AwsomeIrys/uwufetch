import os
import platform
import psutil
import datetime
import socket
import re

def uwuify(text):
    return (
        text.replace("r", "w")
            .replace("l", "w")
            .replace("R", "W")
            .replace("L", "W")
            .replace("no", "nu")
            .replace("has", "haz")
            .replace("have", "haz")
            .replace("you", "u")
            .replace("ove", "uv")
            + " ~ 🐾"
    )

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "N/A"

def get_distro_id():
    try:
        with open('/etc/os-release') as f:
            data = f.read()
            match = re.search(r'^ID="?(.+?)"?$', data, re.MULTILINE)
            return match.group(1).lower() if match else "unknown"
    except:
        return "unknown"

def get_info():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    distro_id = get_distro_id()
    return [
        f"{uwuify('OS')}: {platform.system()} {platform.machine()}",
        f"{uwuify('Kewnew')}: {platform.release()}",
        f"{uwuify('Uptime')}: {str(uptime).split('.')[0]}",
        f"{uwuify('Packwages')}: {get_package_count()}",
        f"{uwuify('Sheww')}: {os.environ.get('SHELL', 'unknown')}",
        f"{uwuify('DE')}: KDE Pwazma (or custom)",
        f"{uwuify('WM')}: KWin (Waywand)",
        f"{uwuify('CPU')}: {platform.processor()}",
        f"{uwuify('WAM')}: {memory.used / (1024 ** 3):.2f} / {memory.total / (1024 ** 3):.2f} GiB",
        f"{uwuify('Disk')}: {disk.used / (1024 ** 3):.2f} / {disk.total / (1024 ** 3):.2f} GiB",
        f"{uwuify('Wocaw IP')}: {get_ip()}",
    ]

def get_package_count():
    try:
        emerge = os.popen("qlist -I | wc -l").read().strip()
        return f"{emerge} (emewge)"
    except:
        return "?"

gentoo_logo = [
    "         -/oyddmdhs+:.",
    "     -odNMMMMMMMMNNmhy+-`              ",
    "   -yNMMMMMMMMMMMNNNmmdhy+-            ",
    " `omMMMMMMMMMMMMNmdmmmmddhhy/`         ",
    " omMMMMMMMMMMMNhhyyyohmdddhhhdo`       ",
    ".ydMMMMMMMMMMdhs++so/smdddhhhhdm+`     ",
    " oyhdmNMMMMMMMNdyooydmddddhhhhyhNd.    ",
    "  :oyhhdNNMMMMMMMNNNmmdddhhhhhyymMh    ",
    "    .:+sydNMMMMMNNNmmmdddhhhhhhmMmy    ",
    "       /mMMMMMMNNNmmmdddhhhhhmMNhs:    ",
    "    `oNMMMMMMMNNNmmmddddhhdmMNhs+`     ",
    "  `sNMMMMMMMMNNNmmmdddddmNMmhs/.       ",
    " /NMMMMMMMMNNNNmmmdddmNMNdso:`         ",
    "+MMMMMMMNNNNNmmmmdmNMNdso/-            ",
    "yMMNNNNNNNmmmmmNNMmhs+/-`              ",
    "/hMMNNNNNNNNMNdhs++/-`                 ",
    "`/ohdmmddhys+++/:.`                    ",
    "  `-//////:--.                         ",
]

def print_fastfetch():
    info = get_info()
    logo_lines = gentoo_logo
    max_logo_width = max(len(line) for line in logo_lines)
    pad = " " * 2

    for i in range(max(len(logo_lines), len(info))):
        logo_part = logo_lines[i] if i < len(logo_lines) else " " * max_logo_width
        info_part = info[i] if i < len(info) else ""
        print(f"{logo_part:<{max_logo_width}}{pad}{info_part}")

if __name__ == "__main__":
    print_fastfetch()
