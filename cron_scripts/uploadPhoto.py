from time import sleep

import datetime
import picamera
import os

PHOTO_DIR = './photo'
BACKUP_FOLDER_ID = u'0B-8dkW850O9RZlgtbkw0T00wckU'

def main():
    print 'Running reboot script...'

    with open('/home/pi/cron_scripts/reboot.log', 'a') as f:
        timeStr = datetime.datetime.now(EST()).strftime('%Y-%m-%d_%H%M%S')
        print 'Output: ', timeStr
        f.write(timeStr + '\n')

    if not os.path.isdir(PHOTO_DIR):
        os.makedirs(PHOTO_DIR)

    takePhotoAndVideo(os.path.join(PHOTO_DIR, timeStr))

    print 'End reboot script...'

def takePhotoAndVideo(savePath):
    camera = picamera.PiCamera()
    camera.resolution = 1024, 768
    camera.rotation = 270

    title = savePath.split('/')[-1]
    photoPath = savePath + '.jpg'
    print 'Taking photo to:', photoPath
    camera.capture(photoPath)
    
    videoPath = savePath + '.h264'
    print 'Recording video to:', videoPath
    camera.start_recording(videoPath)
    sleep(10)
    camera.stop_recording()

    mp4Path = savePath + '.mp4'
    print 'Convert to mp4', mp4Path
    cmd = 'MP4Box -fps 30 -add ' + videoPath + ' ' + mp4Path
    os.system(cmd)

    import driveUtils
    import httplib2
    from apiclient import discovery
    credentials = driveUtils.get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v2', http=http)
    driveUtils.uploadFileToFolder(service, photoPath, title, 'image/jpeg', BACKUP_FOLDER_ID)
    driveUtils.uploadFileToFolder(service, mp4Path, title, 'video/mp4', BACKUP_FOLDER_ID)

class EST(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=+8)

    def dst(self, dt):
        return datetime.timedelta(0)

if __name__ == '__main__':
    main()
