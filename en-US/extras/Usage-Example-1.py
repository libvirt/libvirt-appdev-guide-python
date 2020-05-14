import libvirt, sys

conn = None
try:
    conn = libvirt.open("qemu:///system")
except libvirt.libvirtError as e:
    print(repr(e), file=sys.stderr)
    exit(1)

# We do not need to define a capacity as we want it to be unlimited.
poolXML = """<pool type='dir'>
  <name>ExamplePool</name>
  <uuid/>
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
