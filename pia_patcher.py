#!/usr/bin/env python3

"Replace resolv.conf with Private Internet Access DNS's"

import shutil
import os


def check_current_dir():
    current_dir = os.path.abspath('')
    return current_dir


def replace_resolv():
    current_dir = check_current_dir()
    try:
        shutil.copy(current_dir + 'pia_dns_template.txt', '/etc/resolv.conf')
    except PermissionError as denied:
        denied_message = str(denied)
        print(denied_message)
        print("\033[1m" + "Whoops! Try as root buddie." + "\033[0;0m")
    else:
        print("DNS successfully patched.")
