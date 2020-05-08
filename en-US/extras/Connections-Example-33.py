# Example-33.py
from __future__ import print_function
import sys
import libvirt

# use VPX over HTTPS, select ESX server 'srv1' in datacenter 'dc1'
conn = libvirt.open('vpx://example-vcenter.com/dc1/srv1')
if conn == None:
    print('Failed to open connection to vpx://example-vcenter.com/dc1/srv1', file=sys.stderr)
    exit(1)
conn.close()
exit(0)
