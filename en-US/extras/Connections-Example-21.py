# Example-21.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

alive = conn.isAlive()

print("Connection is alive = " + str(alive))

conn.close()
exit(0)
