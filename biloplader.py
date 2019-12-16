from time import sleep
from gpiozero import LED, InputDevice
import smtplib
import config
import emailsent
import Adafruit_DHT
from beebotte import *

lader_resource.write(0)
fejl_resource.write(0)
slukket_resource.write(0)
tendt_resource.write(1)


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

end_time = time.time() + 3

def opstart():
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
    print("Laderen er taendt")
    return opstart()

def slukket():
    print("laderen er slukket")
    return opstart()

def lader():
    end_time = time.time() + 3
    while time.time() < end_time:
        if not ledforsyning.is_active:
            tallerlader = tallerlader +1
            global tallerlader

            if tallerlader > 2:
                lader_resource.write(1)
                fejl_resource.write(0)
                slukket_resource.write(0)
                tendt_resource.write(0)
                print("Bilen lader")
                sleep(1)
        return fejl()
    else:
        return opstart()

def fejl():
    end_time = time.time() + 3
    while time.time() < end_time:
        if not ledforsyning.is_active:
            global tallerfejl
            tallerfejl = tallerfejl + 1

            if tallerfejl > 2:
                print("fejl pa lader")
            return email()
        return opstart()

def email():
    if not ledforsyning.is_active and tallerfejl == 6:
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
