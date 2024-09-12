# ********************************************************************************
# FileName     : 13._temperature_sensor
# Description  : 온도 센서 값 출력해 보기
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
sensor = ADC(Pin(A2))               # 온도 센서 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)     # 온도 센서 입력 모드 설정


# main loop
def loop():
    sensor_result = sensor.read()   # 온도 센서 결과 값 저장
    print(sensor_result)            # 온도 센서 결과 값 출력
    
    time.sleep(0.2)                 # 0.2초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘