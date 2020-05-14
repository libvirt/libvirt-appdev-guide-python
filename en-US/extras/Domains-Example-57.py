# Example-57.py
#!/usr/bin/env python3
import sys, time
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

# Ensure the domain is running first:
if dom.state() == libvirt.VIR_DOMAIN_RUNNING:
    struct = dom.getTime()
    timestamp = time.ctime(float(struct['seconds']))
    print('The domain current time is ' + timestamp)
else:
    print('The domain is not running, cannot get time information!')

conn.close()
exit(0)
