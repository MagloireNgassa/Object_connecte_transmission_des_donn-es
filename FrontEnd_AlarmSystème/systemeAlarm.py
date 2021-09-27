from gpiozero import Button,LED
from signal import pause
from alarmClass import *
from interface_Graphyque import *
from datetime import datetime

alarm = Alarm()
graphique = Graphique()

btn_Z1 = Button(17)
btn_Z2 = Button(6)
btn_Z3 = Button(5)
btn_Z4 = Button(18)
btn_Act = Button(2)
btn_Reset = Button(15)
btn_Desact = Button(20)



def zone1():
    alarm.Zone_1()
    graphique.colorZone1_on()
    graphique.construire()
    
def zone2():
    alarm.Zone_2()
    graphique.colorZone2_on()
    graphique.construire()
    
def zone3():
    alarm.Zone_3()
    graphique.colorZone3_on()
    graphique.construire()
    
def zone4():
    alarm.Zone_4()
    graphique.colorZone4_on()
    graphique.construire()
    
def reset():
    alarm.Reset()
    graphique.colorReset_on()
    graphique.construire()
    
def desact():
    alarm.AlarmOff()
    graphique.colorDesactivate_on()
    graphique.construire()
    
    
  
    
def active():
    alarm.AlarmOn()
    graphique.colorActivate_on()
    graphique.construire()
    btn_Z1.when_pressed = zone1
    btn_Z2.when_pressed = zone2
    btn_Z3.when_pressed = zone3
    btn_Z4.when_pressed = zone4
    btn_Reset.when_pressed = reset
    btn_Desact.when_pressed = desact

graphique.construire()
print ('systeme de securite demarrer')
btn_Act.when_pressed = active
 
root.mainloop()

 



