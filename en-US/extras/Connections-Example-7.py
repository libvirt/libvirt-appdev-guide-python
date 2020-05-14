# Example-7.py
#!/usr/bin/env python3
import sys
import libvirt

conn = None
try:
    conn = libvirt.open('qemu+tls://host2/system')
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)
conn.close()
exit(0)
