#!/home/pi/Documents/pycharmProject/env01/bin/python3

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if __name__ == '__main__':
    cred = credentials.Certificate('/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-65514e121f.json')