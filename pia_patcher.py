#!/usr/bin/env python3

"Replace resolv.conf with Private Internet Access DNS's"

import shutil
import os


def check_current_dir():
    """Check current directory."""
    current_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
    return current_dir


def check_resolv_exist():
    """Check if resolv.conf exists."""
    return os.path.isfile('/etc/resolv.conf')


def backup_resolv():
    """Back up resolv.conf... just in case :P."""
    current_dir = check_current_dir()
    try:
        shutil.copy('/etc/resolv.conf', current_dir + 'resolv.bak')
    except PermissionError as denied:
        message = "\033[1m" + "ERR! ROOT is needed." + "\033[0;0m"
        print(message)
    else:
        return True


def append_to_resolv():
    """Append template to resolv.conf instead of replacing it."""
    current_dir = check_current_dir()
    with open(current_dir + 'pia_dns_template.txt', mode='r') as template_obj:
        pia_template = template_obj.read()
    with open('/etc/resolv.conf', mode='a') as resolv_obj:
        resolv_obj.write(pia_template)


def replace_resolv():
    """Replace resolv.conf with PIA template."""
    current_dir = check_current_dir()
    try:
        shutil.copy(current_dir + 'pia_dns_template.txt', '/etc/resolv.conf')
    except PermissionError as denied:
        denied_message = str(denied)
        print(denied_message)
        print("\033[1m" + "Whoops! Run it as root buddy." + "\033[0;0m")
    else:
        print("DNS successfully patched.")


if __name__ == '__main__':
    """Run if script called directly."""
    if 