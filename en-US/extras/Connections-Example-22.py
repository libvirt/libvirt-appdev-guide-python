# Example-22.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

retc = conn.compareCPU('<cpu><arch>x86</arch><model>kvm64</model><vendor>Intel</vendor><topology sockets="2" cores="2" threads="1"/></cpu>')

if retc == -1:
    print("CPUs are not the same.")
else:
    print("CPUs are the same.")

conn.close()
exit(0)
