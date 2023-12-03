
import RPi_I2C_driver   # i2c 통신을 사용하기 위한 모듈 선언
From time import *   # time 내의 sleep 함수를 사용하기 위한 모듈 선언

#Rpi_I2C_driver.lcd( I2C address )
Lcd = Rpi_I2C_driver.lcd(0x27)   # lcd의 I2C 통신 주소를 할당해 줌
Lcd.cursor()   # lcd cursor를 보여줌

Def lcd_unknown():    
    # Print a message to the LCD.    
    lcd.print(＂You＇re unknown..＂)    
    lcd.noCursor()    # 커서를 없애줌
  
Def lcd_known():    
    lcd.print(＂Come in!!＂)    
    lcd.noCursor()

Def lcd_clear():    # lcd를 초기화하는 함수 선언
    lcd.clear()
