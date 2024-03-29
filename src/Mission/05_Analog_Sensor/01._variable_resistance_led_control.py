# ******************************************************************************************
# FileName     : 01._variable_resistance_led_control
# Description  : 가변저항 값에 따라 LED 켰다 꺼 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.28 : PEJ : 코드 수정, 딜레이 추가
# ******************************************************************************************


# import
import time                                # 시간 관련 라이브러리
from machine import Pin, ADC               # 핀 관련 모듈
from ETboard.lib.pin_define import *       # ETboard 핀 관련 모듈


# global variable
sensor = ADC(Pin(A0))                      # 가변저항 핀 지정

led_red = Pin(D2)                          # 빨강 LED 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)            # 가변저항을 입력 모드로 설정
    
    led_red.init(Pin.OUT)                  # 빨강 LED를 출력 모드로 설정


# main loop
def loop():
    sensor_result = sensor.read()          # 가변저항 값 저장

    print(sensor_result)                   # 쉘에 가변저항 값 출력

    if sensor_result < 1000:               # 가변저항의 값이 1000보다 작으면
        led_red.value(HIGH)                # 빨강 LED 켜기
    else:
        led_red.value(LOW)                 # 빨강 LED 끄기

    time.sleep(0.1)                        # 0.1초 기디리기


# start point
if __name__ == "__main__":
    setup()
    while True:
        loop()


# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
