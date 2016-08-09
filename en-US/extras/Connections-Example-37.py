# Example-37.py
from __future__ import print_function
import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

xml = '<domain type="kvm">' + \
  '<name>demo2</name>' + \
  '<uuid>4dea24b3-1d52-d8f3-2516-782e98a23fa0</uuid>' + \
  '<memory>131072</memory>' + \
  '<vcpu>1</vcpu>' + \
  '<os>' + \
    '<type arch="i686">hvm</type>' + \
  '</os>' + \
  '<clock sync="localtime"/>' + \
  '<devices>' + \
    '<emulator>/usr/bin/qemu-kvm</emulator>' + \
    '<disk type="file" device="disk">' + \
      '<source file="/var/lib/libvirt/images/demo2.img"/>' + \
      '<target dev="hda"/>' + \
    '</disk>' + \
    '<interface type="network">' + \
      '<source network="default"/>' + \
      '<mac address="24:42:53:21:52:45"/>' + \
    '</interface>' + \
    '<graphics type="vnc" port="-1" keymap="de"/>' + \
  '</devices>' + \
'</domain>'

dom = conn.createXML(xml)

if dom == None:
    print('Error creating domain.')
else:
    print('Domain created successfully.')

conn.close()
exit(0)
