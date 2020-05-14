# Example-27.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

model = conn.getSecurityModel()

print(model[0] + " " + model[1])

conn.close()
exit(0)
