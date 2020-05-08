import libvirt, sys

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

# We set capacity to 0, because that stands for unlimited.
poolXML = """<pool type='dir'>
  <name>ExamplePool</name>
  <uuid/>
  <capacity unit='bytes'>0</capacity>
  <source>
  </source>
  <target>
    <path>/var/lib/libvirt/images</path>
    <permissions>
      <mode>0755</mode>
      <owner>-1</owner>
      <group>-1</group>
    </permissions>
  </target>
</pool>"""

pool = conn.storagePoolDefineXML(poolXML, 0)
pool.setAutostart(1)
pool.create()
