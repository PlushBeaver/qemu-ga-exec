# Command executor for QEMU Windows guests

This package provides `qemu-ga-exec` script to run a command inside a Windows
guest using QEMU Guest Agent (GA). User must set up GA socket as described
in [QEMU wiki](https://wiki.qemu.org/Features/GuestAgent).

```
usage: qemu-ga-exec [-h] --connect CONNECT [--verbose] [--env NAME=VALUE]
                    [--path PATH] [--no-default-path] [--no-default-env]
                    COMMAND [COMMAND ...]

Command executor for QEMU Windows guests.

positional arguments:
  COMMAND               guest command

optional arguments:
  -h, --help            show this help message and exit
  --connect CONNECT, -c CONNECT
                        virtio-serial Unix socket path
  --verbose, -v         increase output verbosity
  --env NAME=VALUE, -e NAME=VALUE
                        guest environment variable
  --path PATH, -p PATH  guest PATH component
  --no-default-path, -P
                        do not prepend PATH with system folders
  --no-default-env, -E  do not prepend environment with default values
```

The script requires Python 3 with standard library only, as it utilizes
[QEMU GA protocol](https://qemu.weilnetz.de/doc/3.1/qemu-ga-ref.html).
License is MIT.
