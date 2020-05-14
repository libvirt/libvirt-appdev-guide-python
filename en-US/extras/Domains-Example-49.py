# Example-49.py
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

name = dom.hostname()
print('The hostname of the domain  is ' + str(name))

conn.close()
exit(0)
