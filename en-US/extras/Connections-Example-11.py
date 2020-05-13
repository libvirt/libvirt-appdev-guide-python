# Example-11.py
#!/usr/bin/env python3
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

node_free_memory = conn.getFreeMemory()
print('Node free memory: '+str(node_free_memory))

conn.close()
exit(0)
