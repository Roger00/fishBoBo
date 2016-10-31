import datetime
import os

T_START = 1820
T_MID_NIGHT = 2359
T_END = 620

SCRIPT_DIR = '/home/pi/cron_scripts/'

def main():
    print os.getcwd()
    t = int(datetime.datetime.now(EST()).strftime('%H%M'))
    print 'Now is %4d' % (t, )

    isNight = t > T_START and t < T_MID_NIGHT
    isMidNight = t >= 0 and t < T_END
    print t > T_START
    print t < T_MID_NIGHT
    print t > 0
    print t < T_END
    print 'isNight:', isNight
    print 'isMidNight:', isMidNight
    if isNight or isMidNight:
        print 'Time to turn up the light'
        os.system('python ' + SCRIPT_DIR + 'lightOn.py')
    else:
        print 'Time to turn off the light'
        os.system('python ' + SCRIPT_DIR + 'lightOff.py')

    print 'End script'

class EST(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=+8)

    def dst(self, dt):
        return datetime.timedelta(0)

if __name__ == '__main__':
    main()
