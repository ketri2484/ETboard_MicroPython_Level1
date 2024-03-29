# ******************************************************************************************
# FileName     : 02._led_red_blink
# Description  : 빨강 LED를 켰다 껐다 해 보기
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
led_red = Pin(D2)                           # 빨강 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)                   # 빨강 LED를 출력 모드로 설정


# main loop
def loop():
    led_red.value(HIGH)                     # 빨강 LED 켜기
    time.sleep(2)                           # 2초 기다리기

    led_red.value(LOW)                      # 빨강 LED 끄기
    time.sleep(2)                           # 2초 기다리기


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
