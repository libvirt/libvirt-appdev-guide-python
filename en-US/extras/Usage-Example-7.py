# List all the snapshots
snapshotList = dom.listAllSnapshots()
# Find the snapshot with the name we want:
revertTo = None
for snap in snapshotList:
    if snap.getName() == 'FirstSnapshot':
        revertTo = snap
if revertTo is not None:
    dom.revertToSnapshot(revertTo)
