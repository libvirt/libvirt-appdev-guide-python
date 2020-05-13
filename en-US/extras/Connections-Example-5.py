# Example-5.py
#!/usr/bin/env python3
import sys
import libvirt

conn1 = libvirt.open('qemu:///system')
if conn1 == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
conn2 = libvirt.open('qemu:///system')
if conn2 == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
conn1.close()
conn2.close()
exit(0)
