import os

TARGET_PATH = '/home/pi/photo'
FILE_LEAVE_COUNT = 3 * 6	# 1-DAYS

l = sorted(os.listdir(TARGET_PATH))
delete = l[:-FILE_LEAVE_COUNT]

totalSize = 0
for name in delete:
    f = os.path.join(TARGET_PATH, name)
    s = os.path.getsize(f)
    totalSize += s

    os.remove(f)

print '%d files deleted, %d Bytes freed' % (len(delete), totalSize)