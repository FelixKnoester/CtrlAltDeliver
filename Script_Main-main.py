# Imports go at the top
from microbit import *
#from X import *
#from X import *
#from X import *

#declarations
LICHT_SENSOR_PIN = pin1
ADDRESS = 0x10

def read16(register):

    i2c.write(ADDRESS, bytes([register]))
    data = i2c.read(ADDRESS, 2)

    value = data[0] | (data[1] << 8)

    return value

# VEML6040 inschakelen
# Register 0x00 = config
# 0x00, 0x00 betekent: sensor aan, normale meting
i2c.write(ADDRESS, bytes([0x00, 0x00, 0x00]))

sleep(100)

devices = i2c.scan()
display.scroll(str(devices))
ADDRESS = 0x10

def read16(register):

    i2c.write(ADDRESS, bytes([register]))
    data = i2c.read(ADDRESS, 2)

    value = data[0] | (data[1] << 8)

    return value

# VEML6040 inschakelen
# Register 0x00 = config
# 0x00, 0x00 betekent: sensor aan, normale meting
i2c.write(ADDRESS, bytes([0x00, 0x00, 0x00]))

devices = i2c.scan()
display.scroll(str(devices))

while True:
    red   = read16(0x08)
    green = read16(0x09)
    blue  = read16(0x0A)
    white = read16(0x0B)

    print("R:", red,
          "G:", green,
          "B:", blue,
          "W:", white)

    sleep(500)


    pin14.write_analog(75) #startpositie
    sleep(1000)
    
    pin14.write_analog(125) #eindpositie

#0x08	Red
#0x09	Green
#0x0A	Blue
#0x0B	White
