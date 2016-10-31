import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
from sys import argv
import cPickle as pickle
import datetime

OUTPUT_PIN = 18
COUNTER_FILE = "counter.pickle"

def saveObj2Pickle(dumpFilePath, obj):
    ''' Save a single object to pickle file '''
    try:
        print '[saveObj2Pickle] pickle path: %s' % (dumpFilePath,)
        pickle.dump(obj, open(dumpFilePath, 'wb'), pickle.HIGHEST_PROTOCOL)
    except IOError:
        print '[saveObj2Pickle] Error: fail to open or save to setting file'
    except pickle.PicklingError:
        print '[saveObj2Pickle] Error: passed unpicklable object'

def readObjFromPickle(dumpFilePath, default=None):
    ''' Read a single object from pickle file '''
    obj = default
    try:
        print '[readObjFromPickle] read from: %s' % (dumpFilePath,)
        obj = pickle.load(open(dumpFilePath, 'rb'))
    except IOError:
        print '[readObjFromPickle] Error: fail to load settings from file'
    except pickle.UnpicklingError:
        print '[readObjFromPickle] Error: there is a problem unpickling the setting file'

    return obj

def lightOn():
    print 'Turn on the light'
    
    count = readObjFromPickle(COUNTER_FILE, 0)
    print 'count', count
    count += 1
    saveObj2Pickle(COUNTER_FILE, count)

def lightOn():
    print 'Feed the fish, run the wheels'

    t = int(datetime.datetime.now(EST()).strftime('%H%M'))
    print 'Now is %4d' % (t, )
    if t >= 2200 and t <= 2300:
        print 'Let''s go baby!'
    else:
        print 'Hold on, baby!'
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)
    p = GPIO.PWM(OUTPUT_PIN, 50)
    p.start(12.5)

    count = readObjFromPickle(COUNTER_FILE, 0)
    count += 1
    cycle = 12.5 if count % 2 == 0 else 2.5
    print cycle
    
    try:
        p.ChangeDutyCycle(cycle)
        sleep(2)

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

    saveObj2Pickle(COUNTER_FILE, count)

    print 'End script'

class EST(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=+8)

    def dst(self, dt):
        return datetime.timedelta(0)

if __name__ == '__main__':
    lightOn()
