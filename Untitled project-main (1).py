from microbit import *
import machine
import utime

# Constants. Stel hier in welke pinnen je gebruikt.
SONAR_SIGNAL_PIN = pin0
SONOR_ECHO_PIN   = pin1

# Variablen
    
def get_afstand():
    # Berekent afstand in cm
    SONAR_SIGNAL_PIN.write_digital(0)   # Zet speaker sonar uit
    utime.sleep_us(2)                   # Wacht 2 microseconden
    SONAR_SIGNAL_PIN.write_digital(1)   # Zet speaker sonar aan (verzend geluid)
    utime.sleep_us(10)                  # Laat het geluid aan voor 10 microseconden
    SONAR_SIGNAL_PIN.write_digital(0)   # Zet speaker sonar uit
    afstandtijd = machine.time_pulse_us(SONOR_ECHO_PIN,1,11600) # Meet tijd tot geluid wordt gemeten
    afstand_cm = afstandtijd / 580       # Deel door 2 (heen en terug) en door snelheid geluid
    return afstand_cm
    
# Hoofdprogramma
SONOR_ECHO_PIN.set_pull(SONOR_ECHO_PIN.NO_PULL)

while True:
    if button_a.was_pressed():        # als op knop A wordt gedrukt, gaan we de afstand meten
        afstand = int(get_afstand())  
        display.scroll(afstand)
       

