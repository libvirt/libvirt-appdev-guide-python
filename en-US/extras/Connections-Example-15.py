# Example-15.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

ver = conn.getVersion()
print('Version: '+str(ver))

conn.close()
exit(0)
