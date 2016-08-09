# Example-36.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

ifaces = conn.listInterfaces()

for iface in ifaces:
    print(iface)

conn.close()
exit(0)
