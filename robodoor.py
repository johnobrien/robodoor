import time
import RPi.GPIO as GPIO
from smc import SMC


def print_counter(n):
    for i in range(1, n):
        print(i)
        time.sleep(1)


def extend_pause_restract_arm():
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


def button_callback():
    print("Button was pushed!")
#    extend_pause_restract_arm()


GPIO.setwarnings(True)
# Set mode to use the pin labels that match the cobbler board
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Press ctrl-c to quit.\n\n")

prev_input = 0
try:
    while True:
        GPIO.wait_for_edge(18, GPIO.RISING, bouncetime=2000)
        button_callback()

except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
