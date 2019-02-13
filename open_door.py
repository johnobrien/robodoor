from smc import SMC
import time

mc = SMC('/dev/ttyUSB0', 115200)
# open serial port and exit safe mode
mc.init()

# drive using 12b mode
mc.speed(1000)
time.sleep(3)
mc.speed(-1000)
time.sleep(3)

# drive using 7b mode
mc.speed7b(100)
time.sleep(3)
mc.speed7b(-100)
time.sleep(3)

# and stop motor
mc.stop()
