import RPi.GPIO as GPIO  
import time  

def blink(pin1,pin2):
	GPIO.output(pin1,GPIO.HIGH) #1.acik
	GPIO.output(pin2,GPIO.LOW) #2.kapali
	time.sleep(1) #1sn bekle
	GPIO.output(pin1,GPIO.LOW) #1.kapali
	GPIO.output(pin2,GPIO.HIGH) #2.acik
	time.sleep(1) #1sn bekle

	return

GPIO.setmode(GPIO.BOARD) #Pin dizilimi 

GPIO.setup(11, GPIO.OUT) #11.pin cikis olarak ayarla
GPIO.setup(7,GPIO.OUT)	#7.pin cikis olarak ayarla
for i in range(0,50):  #for dongusu 0 > 50
        blink(11,7)	#11 ve 7 degerini yordama gonder

GPIO.cleanup()  #Pinleri sifirla
