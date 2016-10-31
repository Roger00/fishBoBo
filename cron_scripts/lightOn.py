import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
from sys import argv

OUTPUT_PIN = 15

def lightOn():
    print 'Turn on the light'

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)
    GPIO.output(OUTPUT_PIN, 1)

    print 'End script'

if __name__ == '__main__':
    lightOn()
