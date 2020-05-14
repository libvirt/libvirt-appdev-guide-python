# Example-24.py
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

dest_conn = None
try:
    dest_conn = libvirt.open('qemu+ssh://desthost/system')
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

dom = None
try:
    dom = conn.lookupByID(6)
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

new_dom = None
try:
    new_dom = dom.migrate(dest_conn, libvirt.VIR_MIGRATE_LIVE, None, None, 0)
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

print('Domain was migrated successfully.', file=sys.stderr)

dest_conn.close()
conn.close()
exit(0)
