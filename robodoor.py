import time
import RPi.GPIO as GPIO
from smc import SMC
import subprocess

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


def door_button_callback(channel):
    print("Door button was pushed!")
    extend_pause_restract_arm()

def power_button_callback(channel):
    print("Power Button was pressed!")
    subprocess.call(['sudo', 'poweroff'])


GPIO.setwarnings(True)
# Set mode to use the pin labels that match the cobbler board
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(3, GPIO.IN)

GPIO.add_event_detect(18, GPIO.RISING, callback=door_button_callback, bouncetime=2000)
GPIO.add_event_detect(3, GPIO.RISING, callback=power_button_callback, bouncetime=2000)


print("Press ctrl-\ to quit.\n\n")


def main():
    try:
        while True:
            pass

    except KeyboardInterrupt:
        GPIO.cleanup()
    GPIO.cleanup()


if __name__ == "__main__":
    main()
