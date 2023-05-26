#nacitanie potrebnych kniznic pre spustanie
import machine
import time

#Ulozenie vystupneho pinu ako premennu pre lahsie pouzitie
led = machine.Pin('LED', machine.Pin.OUT)

#telo samostatneho kodu
try:
        #nekonecny cyklus pre neustale prehravanie kodu
    while True:
        #zapnutie LED svetla
        led.value(True)
        time.sleep(1)
        print("On")
        #vypnutie LED svetla
        led.value(False)
        time.sleep(1)
        print("Off")
        
except:
    pass