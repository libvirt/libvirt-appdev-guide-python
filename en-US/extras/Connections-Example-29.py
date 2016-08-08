# Example-29.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

xml = '<interface type="ethernet" name="eth0">' + \
  '<start mode="onboot"/>' + \
  '<mac address="aa:bb:cc:dd:ee:ff"/>' + \
  '<protocol family="ipv4">' + \
    '<ip address="192.168.1.5" prefix="24"/>' + \
    '<route gateway="192.168.0.1"/>' + \
  '</protocol>' + \
'</interface>'


iface = conn.interfaceDefineXML(xml)

if iface == -1 | iface == None:
    print('The interface was not defined.')
else:
    print('The interface was defined successfully.')

conn.close()
exit(0)
