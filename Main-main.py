from microbit import *

#declarations
kleurSensorPIN = pin0
afstandSensorPIN = pin1
servoPIN1 = pin2 #pin2 tot pin5 zijn servo's
servoPIN1 = pin3 #pin2 tot pin5 zijn servo's
servoPIN1 = pin4 #pin2 tot pin5 zijn servo's
servoPIN1 = pin5 #pin2 tot pin5 zijn servo's

LED_AAN = 1
LED_UIT = 0
kleinRood = 0
grootRood = 0
kleinBlauw = 0
grootBlauw = 0

ADDRESS = 0x10

def read16(register):
    i2c.write(ADDRESS, bytes([register]))
    data = i2c.read(ADDRESS, 2)
    value = data[0] | (data[1] << 8)
    return value

# Kleursensor inschakelen
#i2c.write(ADDRESS, bytes([0x00, 0x00, 0x00]))

sleep(100)
devices = i2c.scan()

while True:
    afstandWaarde = afstandSensorPIN.read_analog()
    red   = read16(0x08)
    green = read16(0x09)
    blue  = read16(0x0A)
    white = read16(0x0B)

    print("R:", red,
          "G:", green,
          "B:", blue,
          "W:", white)

    sleep(500)
    if blue == 1 and afstandWaarde >= 9:
        print("grootBlauw")
    if blue == 1 and afstandWaarde <= 8:
        print("kleinBlauw")
    if red == 1 and afstandWaarde >= 9:
        print("grootRood")
    if red == 1 and afstandWaarde <= 8:
        print("kleinRood")

    #servoPIN1.write_analog(75) #startpositie
    #sleep(1000)
    
    #servoPIN1.write_analog(125) #eindpositie
