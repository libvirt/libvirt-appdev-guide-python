# Example-20.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

secmodel = conn.getSecurityModel()

print('Security Model: '+secmodel[0])
print('Security DOI:   '+secmodel[1])

conn.close()
exit(0)
