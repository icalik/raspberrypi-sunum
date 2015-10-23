#!/usr/bin/env python

from imapclient import IMAPClient
import time

import RPi.GPIO as GPIO

DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = 'test@gmail.com'
PASSWORD = 'PASSWORD'
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 1   # Okunmamis mail sayisi
MAIL_CHECK_FREQ = 5 # 5 sn de 1 kontrol et

GPIO.setwarnings(False) #GPIO uyarisi verme
GPIO.setmode(GPIO.BCM) #BCM dizilimini ayarla
GREEN_LED = 4 #Yesil Led
RED_LED = 17 #Kirmizi Led
GPIO.setup(GREEN_LED, GPIO.OUT) #led cikisi
GPIO.setup(RED_LED, GPIO.OUT) #led cikisi

while True: #sonsuz dongu
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=False) #maile baglanti
    server.login(USERNAME, PASSWORD) #login ol

    if DEBUG:
        print('Giris yapildi >> ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d adet mail var!' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN') # okunmamis mail kontrolu
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print newmails, "yeni mail!"

    if newmails > NEWMAIL_OFFSET:
        GPIO.output(GREEN_LED, True) #led kontrolleri
        GPIO.output(RED_LED, False)
    else:
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)

    time.sleep(MAIL_CHECK_FREQ)

GPIO.cleanup()
