# Example-25.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

buf = conn.getMemoryParameters()

for parm in buf:
    print(parm)

conn.close()
exit(0)
