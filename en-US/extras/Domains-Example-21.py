# Example-21.py
#!/usr/bin/env python3
import sys
import libvirt

filename = '/var/lib/libvirt/save/demo-guest.img'

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

if id = conn.restore(filename)) < 0:
    print('Unable to restore guest from '+filename, file=sys.stderr)
    exit(1)

dom = conn.lookupByID(id);
if dom == None:
    print('Cannot find guest that was restored', file=sys.stderr)
    exit(1)

print('Guest state restored from '+filename, file=sys.stderr)

conn.close()
exit(0)
