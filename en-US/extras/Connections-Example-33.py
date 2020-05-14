# Example-33.py
#!/usr/bin/env python3
import sys
import libvirt

# use VPX over HTTPS, select ESX server 'srv1' in datacenter 'dc1'
conn = None
try:
    conn = libvirt.open('vpx://example-vcenter.com/dc1/srv1')
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)
conn.close()
exit(0)
