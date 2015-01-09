import RPi.GPIO as GPIO
import time

led_val = 0

def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)

def update_leds():
    if led_val==0:
        GPIO.output(5, 0)
        GPIO.output(6, 0)
    elif led_val==1:
        GPIO.output(5, 1)
        GPIO.output(6, 0)
    elif led_val==2:
        GPIO.output(5, 1)
        GPIO.output(6, 1)

def button_pressed(channel):
    global led_val
    if channel==26:
        led_val = led_val + 1
    if channel==27:
        led_val = led_val - 1
    if led_val > 2:
        led_val=2
    if led_val < 0:
        led_val = 0
    update_leds()
        
setup_gpio()
GPIO.add_event_detect(26, GPIO.RISING, callback=button_pressed, bouncetime=100)
GPIO.add_event_detect(27, GPIO.RISING, callback=button_pressed, bouncetime=100)

    
    
while True:
    time.sleep(0.5)
