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
import argparse


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
        print("Successfully backup resolv.conf")
        return True


def append_to_resolv():
    """Append template to resolv.conf instead of replacing it."""
    current_dir = check_current_dir()
    try:
        with open(current_dir + 'pia_dns_template.txt', mode='r') as temp_obj:
            pia_template = temp_obj.read()
        with open('/etc/resolv.conf', mode='a') as resolv_obj:
            # double return so it doesn't get cluttered
            resolv_obj.writelines("\n")
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

    options = argparse.ArgumentParser()
    options.add_argument("-o", "--overwrite",
                         help="Overwrites the entire resolv.conf file.",
                         action="store_true")
    options.add_argument("-f", "--force",
                         help="Forces overwrite. Use with -o",
                         action="store_true")
    options.add_argument("-a", "--append",
                         help="Append resolv.conf instead of overwriting.",
                         action="store_true")
    options.add_argument("-b", "--backup",
                         help="Only performs a backup of current resolv.conf",
                         action="store_true")
    options.add_argument("-r", "--restore",
                         help="Restores previous backup.",
                         action="store_true")
    args = options.parse_args()

    if args.overwrite and args.force:
        print("Warning: resolf.conf exists. Force overwriting.")
        print("Safety first: Making a backup.")
        backup_resolv()
        print("Proceeding to overwrite resolv.conf")
        replace_resolv()

    elif args.overwrite:
        if check_resolv_exist():
            print("Warning: resolv.conf exist.")
            proceed = input("Proceed? [y/N]: ")
            proceed.lower()
            if proceed is 'y':
                print("Warning: resolf.conf exists. Force overwriting.")
                print("Safety first: Making a backup.")
                backup_resolv()
                print("Proceeding to overwrite resolv.conf")
                replace_resolv()
            else:
                print("Exiting...")
                exit()
        else:
            print("Proceeding to overwrite resolv.conf")
            replace_resolv()

    elif args.append:
        print("\nMaking a backup first.")
        backup_resolv()
        print("Appending to resolv.conf")
        append_to_resolv()

    elif args.backup:
        if check_resolv_exist():
            backup_resolv()

    elif args.restore:
        print("restoring - work in progress")
    else:
        print("You need to provide an options.\n")
        options.print_help()
