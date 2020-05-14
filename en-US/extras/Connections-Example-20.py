# Example-20.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

secmodel = conn.getSecurityModel()

print('Security Model: '+secmodel[0])
print('Security DOI:   '+secmodel[1])

conn.close()
exit(0)
