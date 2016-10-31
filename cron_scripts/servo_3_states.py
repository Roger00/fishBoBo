import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
from sys import argv

OUTPUT_PIN = 18

def lightOn():
    print 'Turn on the light'

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)
    p = GPIO.PWM(OUTPUT_PIN, 50)
    p.start(7.5)
    
    try:
        while True:
            p.ChangeDutyCycle(7.5)
            sleep(1)
            p.ChangeDutyCycle(12.5)
            sleep(1)
            p.ChangeDutyCycle(2.5)
            sleep(1)

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

    print 'End script'

if __name__ == '__main__':
    lightOn()
