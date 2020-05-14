# Example-11.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

node_free_memory = conn.getFreeMemory()
print('Node free memory: '+str(node_free_memory))

conn.close()
exit(0)
