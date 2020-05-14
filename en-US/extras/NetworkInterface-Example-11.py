# Example-11.py
#!/usr/bin/env python3
import sys
import libvirt

xml = """
<interface type='ethernet' name='eth0'>
  <start mode='onboot'/>
  <mac address='aa:bb:cc:dd:ee:ff'/>
  <protocol family='ipv4'>
    <ip address="192.168.0.5" prefix="24"/>
    <route gateway="192.168.0.1"/>
  </protocol>
</interface>"""

conn = None
try:
    conn = libvirt.open('qemu:///system')
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

# create/modify a network interface
iface = conn.interfaceDefineXML(xml, 0)
# activate the interface
try:
    iface.create(0)
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    iface.undefine()
    conn.close()
    exit(1)

print("The interface name is: "+iface.name())

iface.destroy()
iface.undefine()
conn.close()
exit(0)
