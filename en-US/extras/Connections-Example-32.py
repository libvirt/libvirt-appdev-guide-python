# Example-32.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('lxc://')
if conn == None:
    print('Failed to open connection to lxc://', file=sys.stderr)
    exit(1)
conn.close()
exit(0)
