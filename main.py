
import RPi.GPIO as GPIO # GPIO를 사용하기 위해 모듈 import
from led import * # led.py에 있는 함수를 사용하기 위해 import
from temp import * # temp.py에 있는 함수를 사용하기 위해 import
from time import * # sleep 함수를 사용하기 위해 import
from face_recog import * # face_recog.py에 있는 함수를 사용하기 위해 import

led2_clean() # led 및 LCD를 초기화해주기 위해 clean

led_pins = [18, 19, 21] # 18,9,21을 삼색 LED 포트로 지정
GPIO.setmode(GPIO.BOARD) # 핀번호를 사용하는 BOARD모드 사용

# 삼색 LED 핀을 모두 출력으로 설정
GPIO.setup(led_pins[0], GPIO.OUT) 
GPIO.setup(led_pins[1], GPIO.OUT)
GPIO.setup(led_pins[2], GPIO.OUT)

# 삼색 LED 핀을 모두 0으로 초기화
GPIO.output(led_pins[0], 0)
GPIO.output(led_pins[1], 0)
GPIO.output(led_pins[2], 0)

# LCD에 인코딩을 하기 전 "Ready..." 메세지를 표시
lcd.print("Ready...")
# Turn off the cursor
lcd.noCursor()

# face_recog.py에 있는 face_encoding 함수를 사용하여 인코딩할 데이터 파일들의 인코딩 값과 이름을 가져옴
family_encodings,family_list=face_encoding()

#LCD clear
lcd.clear()

while True:
    try:
        lcd.print("Reading temp...") # 온도를 읽기 전 메세지를 표시해 방문객이 손을 온도 센서에 갖다 댈 수 있게 함
        sleep(2)
        lcd.clear()
        temp=temp_read() # temp.py에 있는 temp_read함수를 이용하여 온도를 읽어옴
        print("Temperature in Celsius : %.2f C" %temp) 
        lcd.clear()
        lcd.print("Temp:%.2f C" %temp) # 온도를 LCD에 표시

        # Turn off the cursor
        lcd.noCursor()
        
        # 온도가 26도 이상 38도 이하면 face_recog_start함수로 얼굴인식을 시작하고, 38도 이상이면 빨간 경고등이 들어오며 출입이 제한됨
        if temp>26 and temp<38:
            buzzer_in() # 긍정적인 부저음
            led_yellow(led_pins) # 얼굴 인식 시작을 알리는 노란색 경고등
            print(family_list)
            # face_recog_start함수에 미리 인코딩된 (폴더에 넣어놓은 데이터)얼굴의 인코딩 값과 이름 리스트 넣어줌으로써 얼굴인식 시작
            face_recog_start(family_encodings,family_list) 
            sleep(1)
            led_clean(led_pins)
        elif temp>38:
            buzzer_out() # 부정적인 부저음
            led_red(led_pins) # 빨간 LED 표시
            sleep(1)
            led_clean(led_pins)
            continue

        else:
            sleep(1)
            continue



    except KeyboardInterrupt:
        break
