from time import sleep
from gpiozero import LED, InputDevice
import smtplib
import config
import emailsent
import Adafruit_DHT
from beebotte import *

bbt = BBT('rUc4tAg6ieLqPyVoF2A6wif0', 'CHeRlsjCoOU9u1DoMCPdPckO3ji9cy0T')

ledforsyning = InputDevice(19)
ledfejl = InputDevice(6)
ledlader = InputDevice(5)
tallerfejl = 0
tallerlader = 0

tendt_resource = Resource(bbt, 'rasberry_pie_modul', 'tendt')
slukket_resource = Resource(bbt, 'rasberry_pie_modul', 'slukket')
lader_resource = Resource(bbt, 'rasberry_pie_modul', 'lader')
fejl_resource = Resource(bbt, 'rasberry_pie_modul', 'fejl')

def opstart():
    while True:
        if not ledforsyning.is_active:
            if not ledforsyning.is_active and not ledlader.is_active:
                return lader()
            elif not ledforsyning.is_active and not ledfejl.is_active:
                return fejl()
            else:
                return taendt()
        else:
            return slukket()

def taendt():
    tallerlader = 0
    lader_resource.write(0)
    fejl_resource.write(0)
    slukket_resource.write(0)
    tendt_resource.write(1)
    print("Laderen er taendt")
    sleep(1)
    return opstart()

def slukket():
    tallerlader = 0
    lader_resource.write(0)
    fejl_resource.write(0)
    slukket_resource.write(1)
    tendt_resource.write(0)
    print("laderen er slukket")
    sleep(1)
    return opstart()

def lader():
    global tallerlader
    end_time = time.time() + 1
    while time.time() < end_time:
        if not ledforsyning.is_active and not ledlader.is_active:
            tallerlader = tallerlader +1
            
            if tallerlader >= 4:
                lader_resource.write(1)
                fejl_resource.write(0)
                slukket_resource.write(0)
                tendt_resource.write(0)
                print("Bilen lader")
                return opstart()
        elif not ledforsyning.is_active and ledlader.is_active:
            print("Lader LED slukket")
    return fejl()

def fejl():
    tallerlader = 0
    end_time = time.time() + 3
    while time.time() < end_time:
        if not ledforsyning.is_active and not ledfejl.is_active:
            global tallerfejl
            tallerfejl = tallerfejl + 1
            if tallerfejl == 1:
                print("fejl pa lader")
                return email()
            tallerfejl = 0
            return opstart()

def email():
    lader_resource.write(0)
    fejl_resource.write(1)
    slukket_resource.write(0)
    tendt_resource.write(0)
    subjectfejl ="OPLADEFEJL!"
    msgfejl="Hej *navn* din billader melder fejl."
    emailsent.send_email(subjectfejl, msgfejl)


state = opstart()
while state: state = opstart()
print("Laderen melder fejl. System skal genstartes.")