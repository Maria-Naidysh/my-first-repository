import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
sensor_pin = 6
GPIO.setup(sensor_pin, GPIO.IN)
while True:
    sensor_state = GPIO.input(sensor_pin)
    GPIO.output(led, not sensor_state)    
    time.sleep(1)
