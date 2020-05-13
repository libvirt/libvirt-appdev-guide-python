# Example-2.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.openReadOnly('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
conn.close()
exit(0)
