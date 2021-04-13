# Example-8.py
#!/usr/bin/env python3
import sys
import libvirt

xmlconfig = '<domain>........</domain>'

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

dom = None
try:
    dom = conn.defineXMLFlags(xmlconfig, 0)
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

if dom.create() < 0:
    print('Can not boot guest domain.', file=sys.stderr)
    exit(1)

print('Guest '+dom.name()+' has booted', file=sys.stderr)

conn.close()
exit(0)
