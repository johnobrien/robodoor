import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from smc import SMC


def print_counter(n):
    for i in range(1, n):
        print(i)
        time.sleep(1)


def button_callback(channel):
    print("Button was pushed!")
    mc = SMC('/dev/ttyACM0', 115200)

    # drive using 12b mode
    print("Arm extending...")
    mc.init()
    mc.speed(-1000)
    print_counter(15)
    print("Arm stopped...")
    mc.stop()
    print_counter(10)
    print("Arm retracting...")
    mc.init()
    mc.speed(1000)
    print_counter(15)
    mc.stop()


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up


