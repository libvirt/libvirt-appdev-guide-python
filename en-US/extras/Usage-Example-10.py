file = "Screenshot of " + dom.name()
fileHandler = open(file, 'wb')
streamBytes = stream.recv(262120)
while streamBytes != b'':
    fileHandler.write(streamBytes)
    streamBytes = stream.recv(262120)
fileHandler.close()
print('Screenshot saved as type: ' + imageType)
