#!/usr/bin/env python3
# Author: Franccesco Orozco
# Version: 0.1
#
# For installation make a symbolic link:
#     ~ sudo ln -s $PWD/pia_patcher.py /usr/bin/pia-patcher
# Execute:
#     ~ pia-patcher

"Replace resolv.conf with Private Internet Access DNS's"

import shutil
import os
from sys import exit


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
        exit()
    else:
        return True


def append_to_resolv():
    """Append template to resolv.conf instead of replacing it."""
    current_dir = check_current_dir()
    try:
        with open(current_dir + 'pia_dns_template.txt', mode='r') as temp_obj:
            pia_template = temp_obj.read()
        with open('/etc/resolv.conf', mode='a') as resolv_obj:
            # double return so it doesn't get cluttered
            resolv_obj.writelines("\n\n")
            resolv_obj.write(pia_template)
    except PermissionError as denied:
        denied_message = denied
        print(denied_message)
        print("\033[1m" + "Waddup, run me as ROOT okay?." + "\033[0;0m")
        print("Breaking...")
        exit()
    else:
        print("DNS successfully patched (Appended).")
        return True


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
        return True


if __name__ == '__main__':
    """Run if script called directly."""
    # Case scenario: if resolv exists, overwrite, append or break.
    #                but make a backup first!
    if check_resolv_exist():
        print("Warning: resolv.conf exist.")
        print("[O]verwrite / [A]ppend / [B]reak")
        override_safety = input("\033[1m" + "~> " + "\033[0;0m")

        if override_safety.lower() == 'o':
            print("\nMaking a backup first...")
            backup_resolv()

            print("Replacing file...")
            replace_resolv()

        elif override_safety.lower() == 'a':
            print("\nMaking a backup first.")
            backup_resolv()

            print("Appending to resolv.conf")
            append_to_resolv()

        elif override_safety.lower() == 'b':
            print('See ya.')
            exit()

        else:
            print("Wrong option I guess? Exiting...")
            exit()
    else:
        replace_resolv()
