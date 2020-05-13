# Example-57.py
#!/usr/bin/env python3
import sys, time
import libvirt
from xml.dom import minidom

domName = 'CentOS7'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
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
