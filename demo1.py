import RPi.GPIO as GPIO  
import time  
  
def blink(pin): #Yordam olusturuldu 
        GPIO.output(pin,GPIO.HIGH) #Pini ac
        time.sleep(1)  #1sn bekle
        GPIO.output(pin,GPIO.LOW)  #Pini kapat
        time.sleep(1)  #1sn bekle
        return  
  
GPIO.setmode(GPIO.BOARD) #Pin dizilimi 

GPIO.setup(11, GPIO.OUT) #11.pin cikis olarak ayarla
 
for i in range(0,50):  #for dongusu 0 > 50
        blink(11)	#11 degerini yordama gonder

GPIO.cleanup()  #Pinleri sifirla
