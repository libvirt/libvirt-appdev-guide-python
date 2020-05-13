# Example-32.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('lxc://')
if conn == None:
    print('Failed to open connection to lxc://', file=sys.stderr)
    exit(1)
conn.close()
exit(0)
