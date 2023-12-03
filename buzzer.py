import RPi.GPIO as GPIO  # 부저를 사용하기 위해 GPIO 모듈 선언
import time  # sleep 함수를 

def buzzer_in():  
  
    gpio_pin = 32    # 부저 핀 설정
    list=[262,330,392,554] #도 미 솔 높은 레
    
    GPIO.setup(gpio_pin, GPIO.OUT) # 부저를 출력 모드로 설정  
  
    # 주파수를 100으로 설정
    ck_pwm = GPIO.PWM(gpio_pin, 100)

    for i in range(len(list)):  # list 개수만큼 반복 
     
        # 초기 출력을 50% 듀티싸이클로 설정 
        ck_pwm.start(50)
        ck_pwm.ChangeFrequency(list[i])  
        # 주파수를 list 내 숫자로 변환      
        time.sleep(0.5)    
    
    ck_pwm.stop()  # 부저 출력을 멈춤



def buzzer_out():    

    gpio_pin = 32    
    list=[554,392,330,262] # 높은 레 솔 미 도
    
    GPIO.setup(gpio_pin, GPIO.OUT) 
   
    ck_pwm = GPIO.PWM(gpio_pin, 100)   

    for i in range(len(list)):  
      
        ck_pwm.start(50)        
        ck_pwm.ChangeFrequency(list[i])        
        time.sleep(0.5)
    
    ck_pwm.stop()


def buzzer_bell():    

    gpio_pin = 32    
    list=[494,392]   # 시 솔
  
    GPIO.setup(gpio_pin, GPIO.OUT) 
   
    ck_pwm = GPIO.PWM(gpio_pin, 100)    

    for i in range(len(list)):    
    
        ck_pwm.start(50)        
        ck_pwm.ChangeFrequency(list[i])        
        time.sleep(0.7)
    
    ck_pwm.stop()




#buzzer_in()
#buzzer_out()
#buzzer_bell()
