# Path to desired '.iso' file
diskFile = "/tmp/debian.iso"
diskXML = """    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='""" + diskFile + """'/>
      <target dev='hdb' bus='ide'/>
      <address type='drive' controller='0' bus='0' target='0' unit='1'/>
    </disk>"""
dom.updateDeviceFlags(diskXML, 0)
