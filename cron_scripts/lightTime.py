import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
from sys import argv

OUTPUT_PIN = 15

def lightOn(t):
    print 'Turn on the light for %d seconds' % (timeInSec)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)

    try:  
        GPIO.output(OUTPUT_PIN, 1)
        sleep(t)
    # trap a CTRL+C keyboard interrupt  
    except KeyboardInterrupt:
        pass

    GPIO.cleanup()
    print 'End script'

if __name__ == '__main__':
    if len(argv) > 1:
        timeInSec = int(argv[1])
        lightOn(timeInSec)
    else:
        print 'Usage: sudo python %s <time-in-seconds>' % argv[0]