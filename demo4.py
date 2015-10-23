import RPi.GPIO as GPIO
import time
#PIR sensoru
GPIO.setmode(GPIO.BOARD) #Pin dizilimi secildi

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) #12.Pin giris olarak ayarlandi

GPIO.setup(11,GPIO.OUT) #11.Pin cikis olarak ayarlandi

while True:
    input_state = GPIO.input(12)
    if input_state == False:
        print('Hareket Algilandi!')
        GPIO.output(11,1) #GPIO.HIGH = 1
        time.sleep(0.2)	#0.2sn bekle
        GPIO.output(11,0) #GPIO.LOW = 0