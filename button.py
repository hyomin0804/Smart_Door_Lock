#!/usr/bin/env python3
import time    # sleep 함수를 사용하기 위해 time 선언 
Import Rpi.GPIO as GPIO    # GPIO를 통한 버튼 조작을 위해 선언
#  pushover 사용을 위해 필요한 모듈 선언
Import http.client as httplib
import urllib.parse as urllib
from buzzer import *    # buzzer.py에서 지정한 소리를 출력하기 위해 모듈을 불러옴 

# Pushover API setup
PUSH_TOKEN = "a1usw9krqv2zhecgofinfpnt2uwidr"     # API Token/Key
PUSH_USER = "u11ai9x8thzurhpgjqbt2xwegb9cmg"     # Your User Key

def sendPush(  ):    # 알림을 보내는 함수 선언
    conn = httplib.HTTPSConnection("api.pushover.net:443")    
    conn.request("POST", "/1/messages.json",            
          urllib.urlencode({                    
                    "token": PUSH_TOKEN,                    
                    "user": PUSH_USER,                    
                    "message": "visitor has arrived! \n http://192.168.0.64:8080/video_feed",# 보내고자 하는 메시지 설정           
          }), { "Content-type": "application/x-www-form-urlencoded" })
    
    conn.getresponse()
    
    return

BUTTON_GPIO = 36 # 버튼의 핀번호를 36번으로 설정



pressed = False # 눌린 상태를 false로 초기화

while True:
    GPIO.setmode(GPIO.BOARD) # GPIO 설정을 핀번호를 사용하는 BOARD모드 사용
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP) # 버튼을 입력으로 사용하고 풀업저항으로 설정함
    # button is pressed
    if (GPIO.input(BUTTON_GPIO) == 0):
        print("pressed") # 초인종이 눌렸음을 print
        buzzer_bell() # 딩동~ 소리가 나는 buzzer_bell함수 호출
        sendPush() # pushover로 메세지를 보냄
        time.sleep(1)
