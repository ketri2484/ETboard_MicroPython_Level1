# ******************************************************************************************
# FileName     : 02._led_blue_blink
# Description  : 파랑 LED를 켰다, 껐다 해 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 2024.03.13 : PEJ : 주석 수정
# ******************************************************************************************


# import
import time                                # 시간 관련 라이브러리
from machine import Pin                    # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *       # ETboard 핀 관련 모듈


# global variable
led_blue = Pin(D3)                         # 파랑 LED 핀 지정


# setup
def setup():
    led_blue.init(Pin.OUT)                 # 파랑 LED를 출력 모드로 설정


# main loop
def loop():
    led_blue.value(HIGH)                   # 파랑 LED 켜기
    time.sleep(2)                          # 2초 기다리기

    led_blue.value(LOW)                    # 파랑 LED 끄기
    time.sleep(2)                          # 2초 기다리기


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
