from gpiozero import LED, Button
from signal import pause
import requests
from datetime import datetime
from interface_Graphyque import *

graphique = Graphique()
class Alarm:
    def __init__(self):
        self.segmentA = LED(8)
        self.segmentB = LED(9)
        self.segmentC = LED(10)
        self.segmentD = LED(11)
        self.segmentE = LED(12)
        self.segmentF = LED(13)
        self.segmentG = LED(14)
        self.piezo = LED(3)
        self.detecteurZone1 = False
        self.detecteurZone2 = False
        self.detecteurZone3 = False
        self.detecteurZone4 = False
        self.alarmActive = False
        self.btn_Reset = False
        
    def Transmission(self):
        url = 'http://192.168.2.11:3535/alarm'
        myobj = {'zone1': self.detecteurZone1,'zone2':self.detecteurZone2,
                 'zone3':self.detecteurZone3,'zone4':self.detecteurZone4,
                 'alarmOn':self.alarmActive,'reset':self.btn_Reset,'dateHeure': str(datetime.now())}
        x = requests.post(url, data = myobj)

        return(x.text)
        
    
    
    def AlarmOn(self):
        self.segmentA.on()
        self.segmentB.on()
        self.segmentC.on()
        self.segmentE.on()
        self.segmentF.on()
        self.segmentG.on()
        self.detecteurZone1 = False
        self.detecteurZone2 = False
        self.detecteurZone3 = False
        self.detecteurZone4 = False
        print ('systeme activer')
        self.alarmActive = True
        self.Transmission()
        
    def AlarmOff(self):
        self.segmentA.on()
        self.segmentB.on()
        self.segmentC.on()
        self.segmentD.on()
        self.segmentE.on()
        self.segmentF.on()
        print ('systeme désactiver')
        self.alarmActive = False
        self.Transmission()

    
    def Zone_1(self):
        print ('zone 1 detecter')
        self.btn_Reset = False
        self.segmentA.off()
        self.segmentB.off()
        self.segmentC.off()
        self.segmentE.off()
        self.segmentF.off()
        self.detecteurZone1 = True
        self.Transmission()
        self.piezo.on()
        self.segmentB.on()
        self.segmentC.on()
             
            
        
    def Zone_2(self):
        print ('zone 2 detecter')
        self.btn_Reset = False
        self.segmentA.off()
        self.segmentB.off()
        self.segmentC.off()
        self.segmentE.off()
        self.segmentF.off()
        self.detecteurZone2 = True
        self.Transmission()
        self.piezo.on()
        self.segmentA.on()
        self.segmentB.on()
        self.segmentG.on()
        self.segmentE.on()
        self.segmentD.on()
             
        
    def Zone_3(self):
        print ('zone 3 detecter')
        self.btn_Reset = False
        self.segmentA.off()
        self.segmentB.off()
        self.segmentC.off()
        self.segmentE.off()
        self.segmentF.off()
        self.detecteurZone3 = True
        self.Transmission()
        self.piezo.on()
        self.segmentA.on()
        self.segmentB.on()
        self.segmentG.on()
        self.segmentC.on()
        self.segmentD.on()
             
        
    def Zone_4(self):
        print ('zone 4 detecter')
        self.btn_Reset = False
        self.segmentA.off()
        self.segmentB.off()
        self.segmentC.off()
        self.segmentE.off()
        self.segmentF.off()
        self.detecteurZone4 = True
        self.Transmission()
        self.piezo.on()
        self.segmentF.on()
        self.segmentB.on()
        self.segmentG.on()
        self.segmentC.on()
            
    def Reset(self):
        self.btn_Reset = True
        print ('Reset active')
        self.piezo.off()
        self.segmentF.off()
        self.segmentB.off()
        self.segmentG.off()
        self.segmentC.off()
        self.AlarmOn()
         
            
