# PIA DNS Patcher
This script replaces the */etc/resolv.conf* with the PIA DNS's to evade DNS leaking.
It **O**verwrites or **A**ppends your resolv.conf file.

# Installation
You can call it from everywhere with an absolute path but for convenience make a symbolic link:

`$ sudo ln -s $PWD/pia-patcher.py /usr/bin/pia-patcher`

And then execute it:
```
$ pia-patcher
usage: pia-patcher.py [-h] [-o] [-f] [-a] [-b] [-r]

optional arguments:
  -h, --help       show this help message and exit
  -o, --overwrite  Overwrites the entire resolv.conf file.
  -f, --force      Forces overwrite. Use with -o
  -a, --append     Append resolv.conf instead of overwriting.
  -b, --backup     Only performs a backup of current resolv.conf
  -r, --restore    Restores previous backup
```

```
$ sudo pia-patcher.py -of
Warning: resolf.conf exists. Force overwriting.
Safety first: Making a backup.
Successfully backup resolv.conf
Proceeding to overwrite resolv.conf
DNS successfully patched.
```

# Procedure
* Makes a backup of the original resolv.conf
* Replaces resolv.conf with a new resolv.conf file with PIA DNS addresses.
*	OR appends it if you choose to.