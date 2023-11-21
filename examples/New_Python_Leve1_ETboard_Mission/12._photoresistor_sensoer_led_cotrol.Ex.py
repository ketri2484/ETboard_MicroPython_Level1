# ********************************************************************************
# FileName     : 12._photoresistor_sensoer_led_cotrol.Ex
# Description  : 조도 센서 값이 500 이하이면 순차적으로 LED 켜지게 해 보기
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
sensor = ADC(Pin(A1))                 # 조도 센서 지정
led_red = Pin(D2)                     # 빨강 LED 지정
led_blue = Pin(D3)                    # 파랑 LED 지정
led_green = Pin(D4)                   # 초록 LED 지정
led_yellow = Pin(D5)                  # 노랑 LED 지정
sensor_result = 0                     # 조도 센서 결과 값 설정

# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)       # 조도센서 입력 모드 설정
    
    led_red.init(Pin.OUT)             # 빨강 LED를 출력으로 설정
    led_blue.init(Pin.OUT)            # 파랑 LED를 출력으로 설정
    led_green.init(Pin.OUT)           # 초록 LED를 출력으로 설정
    led_yellow.init(Pin.OUT)          # 노랑 LED를 출력으로 설정


# main loop
def loop():
    sensor_result = sensor.read()     # 조도 센서 결과 값 저장
    print(sensor_result)              # 조도 센서 결과 값 출력
    
    if sensor_result < 600:           # 조도 센서 결과 값이 600보다 작으면
        led_red.value(HIGH)           # 빨강 LED 켜기
        time.sleep(1)                 # 1초 기다리기
        led_green.value(HIGH)         # 초록 LED 켜기
        time.sleep(1)                 # 1초 기다리기
        led_yellow.value(HIGH)        # 노랑 LED 켜기
        time.sleep(1)                 # 1초 기다리기
        led_blue.value(HIGH)          # 파랑 LED 켜기
        time.sleep(1)                 # 1초 기다리기
    
    if sensor_result > 600:           # 조도 센서 결과 값이 600보다 크면
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