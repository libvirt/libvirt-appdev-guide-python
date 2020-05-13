# Example-7.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('qemu+tls://host2/system')
if conn == None:
    print('Failed to open connection to qemu+tls://host2/system', file=sys.stderr)
    exit(1)
conn.close()
exit(0)
