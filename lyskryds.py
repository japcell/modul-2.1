from gpiozero import LED, Button
from time import sleep

ledrød1 = LED(22)
ledgul1 = LED(27)
ledgrøn1 = LED(17)
ledrød2 = LED(13)
ledgul2 = LED(19)
ledgrøn2 = LED(26)

x = 0

def taller(x):
    ledgul1.off()
    ledgul2.off()
    ledrød1.on()
    ledrød2.on()
    sleep (5)
    if x == 0:
        x = 1
        return YGOV(x)
    
    elif x == 1:
        x = 0
        return YGNS(x)

def YGNS(x): #yellow green nord syd
    ledgul1.on()
    sleep(1)
    ledrød1.off()
    ledgul1.off()
    ledgrøn1.on()
    sleep(3)
    return GYNS(x)
    
def GYNS(x): #green yellow nord syd
    ledgrøn1.off()
    ledgul1.on()
    sleep(1)
    return taller(x)

def YGOV(x): # Yello, green øst vest
    ledgul2.on()
    sleep(1)
    ledrød2.off()
    ledgul2.off()
    ledgrøn2.on()
    sleep(3)
    return GYOV(x)
    
def GYOV(x): #green yellow nord syd
    ledgrøn2.off()
    ledgul2.on()
    sleep(1)
    return taller(x)

state = taller(x)
while state: state = taller(x)
print("Der gik noget galt")