# Example-52.py
#!/usr/bin/env python3
import sys
import libvirt
from xml.dom import minidom

domName = 'CentOS7'

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

dom = None
try:
    dom = conn.lookupByName(domName)
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

flag = None
try:
    flag = dom.isPersistent()
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    conn.close()
    exit(1)

if flag == 1:
    print('The domain is persistent.')
elif flag == 0:
    print('The domain is not persistent.')

conn.close()
exit(0)
