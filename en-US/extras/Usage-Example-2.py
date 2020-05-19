volumeXML = """
<volume>
  <name>Volume.qcow2</name>
  <allocation>0</allocation>
  <capacity unit="G">16</capacity>
  <target>
    <path>/var/lib/libvirt/images/Volume.qcow2</path>
    <format type='qcow2'/>
    <permissions>
      <owner>107</owner>
      <group>107</group>
      <mode>0744</mode>
     <label>ExampleVolume</label>
    </permissions>
  </target>
</volume>"""

pool.createXML(volumeXML, 0)
