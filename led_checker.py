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
    if not ledforsyning.is_active and tallerlader < 2:
        lader_resource.write(0)
        fejl_resource.write(0)
        slukket_resource.write(0)
        tendt_resource.write(1)
        print ("Laderen er taendt")
        return opstart()
    else:
        return opstart()
        
def slukket():
    sleep(1)
    lader_resource.write(0)
    fejl_resource.write(0)
    slukket_resource.write(1)
    tendt_resource.write(0)
    print("laderen er slukket")
    return opstart()
    
def lader():
    global tallerlader
    tallerlader = tallerlader +1
    if not ledforsyning.is_active and tallerlader > 2:
        lader_resource.write(1)
        fejl_resource.write(0)
        slukket_resource.write(0)
        tendt_resource.write(0)
        print("Bilen lader")
        sleep(1)
        return opstart()
    else:
        return opstart()
        
def fejl():
    global tallerfejl
    tallerfejl = tallerfejl + 1
    print("fejl pa lader")
    if not ledforsyning.is_active and tallerfejl == 6:
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



