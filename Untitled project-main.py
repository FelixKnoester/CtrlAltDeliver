from microbit import *
import machine
import utime

# Constants. Stel hier in welke pinnen je gebruikt.
SONAR_SIGNAL_PIN = pin0
SONOR_ECHO_PIN   = pin1
servoPIN1 = pin9
servoPIN2 = pin8
# Variablen
    
def get_afstand():
    # Berekent afstand in cm
    SONAR_SIGNAL_PIN.write_digital(0)   # Zet speaker sonar uit
    utime.sleep_us(2)                   # Wacht 2 microseconden
    SONAR_SIGNAL_PIN.write_digital(1)   # Zet speaker sonar aan (verzend geluid)
    utime.sleep_us(10)                  # Laat het geluid aan voor 10 microseconden
    SONAR_SIGNAL_PIN.write_digital(0)   # Zet speaker sonar uit
    afstandtijd = machine.time_pulse_us(SONOR_ECHO_PIN,1,11600) # Meet tijd tot geluid wordt gemeten
    afstand_cm = afstandtijd / 5.8       # Deel door 2 (heen en terug) en door snelheid geluid
    return afstand_cm
    
# Hoofdprogramma
SONOR_ECHO_PIN.set_pull(SONOR_ECHO_PIN.NO_PULL)
#servoPIN1.set_pull(servoPIN1.PULL_UP)

while True:
    if button_b.was_pressed():
        sleep(1000)
        afstand = int(get_afstand())  
        sleep(1000)
        display.scroll(afstand)
        sleep(1000)
        servoPIN1.write_analog(132)
        sleep(1000)
        servoPIN1.write_analog(20)
        sleep(200)
    
    if button_a.was_pressed():
        servoPIN2.write_analog(132)
        sleep(1000)
        servoPIN2.write_analog(20)
        sleep(200) 
       
