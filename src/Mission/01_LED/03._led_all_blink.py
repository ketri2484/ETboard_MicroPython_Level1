# ******************************************************************************************
# FileName     : 03._led_all_blink
# Description  : 모든 LED를 켰다 껐다 해 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 2024.03.28 : PEJ : 주석 수정
# ******************************************************************************************


# import
import time                                # 시간 관련 라이브러리
from machine import Pin                    # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *       # ETboard 핀 관련 모듈


# global variable
led_red = Pin(D2)                          # 빨강 LED 핀 지정
led_blue = Pin(D3)                         # 파랑 LED 핀 지정
led_green= Pin(D4)                         # 초록 LED 핀 지정
led_yellow = Pin(D5)                       # 노랑 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)                  # 빨강 LED를 출력 모드로 설정
    led_blue.init(Pin.OUT)                 # 파랑 LED를 출력 모드로 설정
    led_green.init(Pin.OUT)                # 초록 LED를 출력 모드로 설정
    led_yellow.init(Pin.OUT)               # 노랑 LED를 출력 모드로 설정


# main loop
def loop():
    led_red.value(HIGH)                    # 빨강 LED 켜기
    led_blue.value(HIGH)                   # 파랑 LED 켜기
    led_green.value(HIGH)                  # 초록 LED 켜기
    led_yellow.value(HIGH)                 # 노랑 LED 켜기
    time.sleep(2)                          # 2초 기다리기

    led_red.value(LOW)                     # 빨강 LED 끄기
    led_blue.value(LOW)                    # 파랑 LED 끄기
    led_green.value(LOW)                   # 초록 LED 끄기
    led_yellow.value(LOW)                  # 노랑 LED 끄기
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
