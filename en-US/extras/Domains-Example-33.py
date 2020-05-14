# Example-33.py
#!/usr/bin/env python3
import sys
import libvirt

domName = 'Fedora22-x86_64-1'

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

dom = conn.lookupByID(5)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

cpu_stats = dom.getCPUStats(False)
for (i, cpu) in enumerate(cpu_stats):
   print('CPU '+str(i)+' Time: '+str(cpu['cpu_time'] / 1000000000.))

conn.close()
exit(0)
