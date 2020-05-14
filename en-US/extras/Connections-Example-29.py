# Example-29.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

map = conn.getCPUMap()

print("CPUs: " + str(map[0]))
print("Available: " + str(map[1]))

conn.close()
exit(0)
