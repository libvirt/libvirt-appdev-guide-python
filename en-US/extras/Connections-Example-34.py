# Example-34.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

try:
    iface = conn.interfaceLookupByName("enp0s25")
except:
    print("No interface was found.")
else:
    print(iface)

conn.close()
exit(0)
