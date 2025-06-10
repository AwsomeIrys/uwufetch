#!/usr/bin/env python3

import os
import platform
import psutil
import datetime
import socket
import re
import argparse

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

def get_package_count():
    distro = get_distro_id()
    try:
        if distro in ["debian", "ubuntu"]:
            count = os.popen("dpkg --get-selections | wc -l").read().strip()
            return f"{count} (depkgies~)"
        elif distro in ["arch", "manjaro"]:
            count = os.popen("pacman -Q | wc -l").read().strip()
            return f"{count} (pacwammies~)"
        elif distro in ["gentoo"]:
            count = os.popen("qlist -I | wc -l").read().strip()
            return f"{count} (emewgies~)"
        else:
            return "(unknown distwo >_<)"
    except:
        return "(oopsy owo)"


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
PRIDE_FLAGS = {
    "rainbow": [
        "\033[38;5;196m",  # Red
        "\033[38;5;202m",  # Orange
        "\033[38;5;226m",  # Yellow
        "\033[38;5;46m",   # Green
        "\033[38;5;21m",   # Blue
        "\033[38;5;93m",   # Purple
    ],
    "trans": [
        "\033[38;5;45m",   # Light Blue
        "\033[38;5;231m",  # White
        "\033[38;5;205m",  # Pink
        "\033[38;5;231m",  # White
        "\033[38;5;45m",   # Light Blue
    ],
    "bi": [
        "\033[38;5;206m",  # Pink
        "\033[38;5;93m",   # Purple
        "\033[38;5;21m",   # Blue
    ],
    "lesbian": [
        "\033[38;5;196m",  # Dark Orange/Red
        "\033[38;5;202m",  # Orange
        "\033[38;5;231m",  # White
        "\033[38;5;213m",  # Pink
        "\033[38;5;124m",  # Dark Red
    ],
    "pan": [
        "\033[38;5;201m",  # Pink
        "\033[38;5;226m",  # Yellow
        "\033[38;5;51m",   # Cyan
    ],
    "nonbinary": [
        "\033[38;5;226m",  # Yellow
        "\033[38;5;231m",  # White
        "\033[38;5;93m",   # Purple
        "\033[38;5;16m",   # Black
    ],
    "genderfluid": [
        "\033[38;5;231m",  # White
        "\033[38;5;206m",  # Pink
        "\033[38;5;16m",   # Black
        "\033[38;5;21m",   # Blue
        "\033[38;5;196m",  # Red
    ],
    "progress": [
        "\033[38;5;196m",  # Red
        "\033[38;5;202m",  # Orange
        "\033[38;5;226m",  # Yellow
        "\033[38;5;46m",   # Green
        "\033[38;5;21m",   # Blue
        "\033[38;5;16m",   # Black
        "\033[38;5;244m",  # Gray (white stripe)
        "\033[38;5;51m",   # Cyan (trans stripe)
    ],
    "ace": [
        "\033[38;5;16m",   # Black
        "\033[38;5;244m",  # Gray
        "\033[38;5;231m",  # White
        "\033[38;5;205m",  # Purple
    ],
}

# Alias mapping for user-friendly flag names
FLAG_ALIASES = {
    "transgender": "trans",
    "trans": "trans",
    "bi": "bi",
    "bisexual": "bi",
    "lesbian": "lesbian",
    "pan": "pan",
    "pansexual": "pan",
    "nonbinary": "nonbinary",
    "nb": "nonbinary",
    "genderfluid": "genderfluid",
    "progress": "progress",
    "ace": "ace",
    "rainbow": "rainbow",
}


def print_fastfetch_with_pride(flag="rainbow"):
    flag_key = FLAG_ALIASES.get(flag.lower(), "rainbow")
    pride_colors = PRIDE_FLAGS.get(flag_key, PRIDE_FLAGS["rainbow"])
    reset = "\033[0m"

    info = get_info()
    logo_lines = gentoo_logo
    max_logo_width = max(len(line) for line in logo_lines)
    pad = " " * 2

    for i in range(max(len(logo_lines), len(info))):
        logo_part = logo_lines[i] if i < len(logo_lines) else " " * max_logo_width
        color = pride_colors[i % len(pride_colors)]
        colored_logo = f"{color}{logo_part:<{max_logo_width}}{reset}"
        info_part = info[i] if i < len(info) else ""
        print(f"{colored_logo}{pad}{info_part}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UwUfetch with pride flag colors")
    parser.add_argument("--flag", type=str, default="rainbow", help="Select pride flag color theme (e.g. trans, bi, ace, lesbian, pan, nonbinary, etc.)")
    args = parser.parse_args()
    print_fastfetch_with_pride(flag=args.flag)
