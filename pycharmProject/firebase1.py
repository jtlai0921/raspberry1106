#!/home/pi/Documents/pycharmProject/env01/bin/python3

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from gpiozero import LED

led = LED(25)

def ledControlDataChange(even):
    print('內容改變')
    ledState = even.data['LED25']
    if ledState == 'OPEN':
        print('Open')
        led.on()
    else:
        print('Close')
        led.off()

if __name__ == '__main__':
    cred = credentials.Certificate('/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-65514e121f.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
    })
    ledControlRef = db.reference('raspberrypi/LED_Control')
    ledControlRef.listen(ledControlDataChange)

