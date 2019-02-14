from smc import SMC
import time

mc = SMC('/dev/ttyACM0', 115200)
# open serial port and exit safe mode
mc.init()

# drive using 12b mode
mc.speed(1000)
time.sleep(30)
mc.speed(-1000)
time.sleep(30)

# drive using 7b mode
mc.speed7b(100)
time.sleep(30)
mc.speed7b(-100)
time.sleep(30)

# and stop motor
mc.stop()
