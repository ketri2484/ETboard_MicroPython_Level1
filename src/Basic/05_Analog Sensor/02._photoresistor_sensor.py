# ******************************************************************************************
# FileName     : 02._photoresistor_sensor
# Description  : 조도 센서 값 출력해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.13 : PEJ : 주석 수정
# ******************************************************************************************


# import
import time                                  # 시간 관련 라이브러리
from machine import Pin, ADC                 # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *         # ETboard 핀 관련 모듈


# global variable
sensor = ADC(Pin(A1))                        # 조도 센서 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)              # 조도 센서 입력 모드 설정


# main loop
def loop():
    sensor_result = sensor.read()            # 조도 센서 값 저장

    print(sensor_result)                     # 조도 센서 값 출력

    time.sleep(0.1)                          # 0.1초 기다리기


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
