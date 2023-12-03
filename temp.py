import smbus # I2C 통신과 비슷하게 저속도 장치와 통신하는 데 사용하는 간단한 모듈
import time # sleep 함수를 사용하기 위해 임포트
 
def temp_read():

    # I2C bus를 정의
    bus = smbus.SMBus(1)
     
    # HDC1000 address, 0x40 / Configuration register 0x02 / heater on 0x30로 설정
    bus.write_byte_data(0x40, 0x02, 0x30)
     
    # 온도 측정을 하는 0x00 명령을 줌
    bus.write_byte(0x40, 0x00)
     
    time.sleep(0.5)
     
    # 사용한 온도센서는 2-byte로 temp 데이터를 읽음 
    data0 = bus.read_byte(0x40)
    data1 = bus.read_byte(0x40)
     
    # celsTemp type으로 데이터 변환
    temp = (data0 * 256) + data1
    celsTemp = (temp / 65536.0) * 165.0 - 40

    return celsTemp
