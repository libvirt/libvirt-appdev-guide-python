# Example-1.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

domainID = 6
dom = conn.lookupByID(domainID)
if dom == None:
    print('Failed to get the domain object', file=sys.stderr)

conn.close()
exit(0)
