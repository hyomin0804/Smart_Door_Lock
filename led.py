
import RPi.GPIO as GPIO    
# led를 사용하기 위해 GPIO 모듈 선언
import time   # time 내의 sleep 함수를 사용하기 위한 모듈 선언

def led_red(pins):      # 빨간색 led  출력
    GPIO.output(pins[0], 0)    
    GPIO.output(pins[1], 1)    
    GPIO.output(pins[2], 1)
    
def led_green(pins):        # 초록색 led  출력
    GPIO.output(pins[0], 1)    
    GPIO.output(pins[1], 0)    
    GPIO.output(pins[2], 1)
     
def led_yellow(pins):       # 노란색 led  출력
    GPIO.output(pins[0], 0)    
    GPIO.output(pins[1], 0)    
    GPIO.output(pins[2], 1)  
      
def led_clean(pins):         # led 초기화
    GPIO.output(pins[0], 0)    
    GPIO.output(pins[1], 0)    
    GPIO.output(pins[2], 0)  
