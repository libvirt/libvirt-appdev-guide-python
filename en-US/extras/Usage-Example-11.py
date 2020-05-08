# Example-11.py
import sys
import libvirt

domName = 'TestAppliance'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

stream = conn.newStream()

# This function supports up to three arguments:
#   stream, screen number and flags.
# We do not need to supply anything for the flags argument.
# The screen number is the sequential number of the screen
#   we want to take a screenshot of.

imageType = domain.screenshot(stream,0)

file = "Screenshot of " + dom.name()
fileHandler = open(file, ’wb’)
streamBytes = stream.recv(262120)

while streamBytes != b’’:
    fileHandler.write(streamBytes)
    streamBytes = stream.recv(262120)
fileHandler.close()

print(’Screenshot saved as type: ’ + imageType)
stream.finish()

conn.close()
exit(0)
