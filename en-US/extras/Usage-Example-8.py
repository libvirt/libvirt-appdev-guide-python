import sys, libvirt
conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)
domain = conn.lookupByName('TestDomain')
