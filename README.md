# PIA DNS Patcher
This script replaces the */etc/resolv.conf* with the PIA DNS's to evade DNS leaking.
It **O**verwrites or **A**ppends your resolv.conf file.

# Installation
You can call it from everywhere with an absolute path but for convenience make a symbolic link:

`$ sudo ln -s $PWD/pia_patcher.py /usr/bin/pia-patcher`

And then execute it:
```
$ pia-patcher
Warning: resolv.conf exist.
[O]verwrite / [A]ppend / [B]reak
~> O
Making a backup first...
Replacing file...
DNS successfully patched.
```

# Procedure
* Makes a backup of the original resolv.conf
* Replaces resolv.conf with a new resolv.conf file with PIA DNS addresses.
*	OR appends it if you choose to.

# TODO
* Ability to restore
* CLI arguments