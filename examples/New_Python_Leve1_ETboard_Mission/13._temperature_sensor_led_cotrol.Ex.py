# ********************************************************************************
# FileName     : 13._temperature_sensor_led_cotrol.Ex
# Description  : 온도 센서 결과 값이 일정 값보다 크면 LED 켜지게 해보기
# Description  : 값이 2100 보다 크면 빨강,노랑, 2150 보다 크면 파랑, 초록 LED 켜지게 해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 
# ********************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A2))                 # 온도 센서 지정
led_red = Pin(D2)                     # 빨강 LED 지정
led_blue = Pin(D3)                    # 파랑 LED 지정
led_green = Pin(D4)                   # 초록 LED 지정
led_yellow = Pin(D5)                  # 노랑 LED 지정
sensor_result = 0                     # 온도 센서 결과 값 설정

# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)       # 온도 센서 입력 모드 설정
    
    led_red.init(Pin.OUT)             # 빨강 LED를 출력으로 설정
    led_blue.init(Pin.OUT)            # 파랑 LED를 출력으로 설정
    led_green.init(Pin.OUT)           # 초록 LED를 출력으로 설정
    led_yellow.init(Pin.OUT)          # 노랑 LED를 출력으로 설정


# main loop
def loop():
    sensor_result = sensor.read()     # 온도 센서 결과 값 저장
    print(sensor_result)              # 온도 센서 결과 값 출력
    
    if sensor_result > 2100:          # 온도 센서 결과 값이 2100 보다 크면
        led_red.value(HIGH)           # 빨강 LED 켜기
        led_yellow.value(HIGH)        # 노랑 LED 켜기
        
    if sensor_result > 2150:          # 온도 센서 결과 값이 2150 보다 크면
        led_blue.value(HIGH)          # 파랑 LED 켜기
        led_green.value(HIGH)         # 초록 LED 켜기
    

    if sensor_result < 2100:          # 온도 센서 결과 값이 2100 보다 작으면
        led_red.value(LOW)            # 빨강 LED 끄기
        led_blue.value(LOW)           # 파랑 LED 끄기
        led_green.value(LOW)          # 초록 LED 끄기
        led_yellow.value(LOW)         # 노랑 LED 끄기
        
    time.sleep(0.2)                   # 0.2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘