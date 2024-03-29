# ******************************************************************************************
# FileName     : 01._if_led_control_2
# Description  : 조건문 if를 이용하여 LED 제어해 보기_2
# Description  : data 값이 100보다 크면 빨강 LED, 150보다 크면 파랑 LED 켜지게 해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Question     : data에 151 넣으면 어떻게 될까요?
# Reference    :
# Modified     : 2024.03.28 : PEJ : 파일명, 코드, 주석 수정
# ******************************************************************************************


# import
import time                                  # 시간 관련 라이브러리
from machine import Pin                      # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *         # ETboard 핀 관련 모듈


# global variable
data = 101                                   # data 변수에 101 저장
led_red = Pin(D2)                            # 빨강 LED 핀 지정
led_blue = Pin(D3)                           # 파랑 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)                    # 빨강 LED를 출력 모드로 설정
    led_blue.init(Pin.OUT)                   # 파랑 LED를 출력 모드로 설정


# main loop
def loop():
    if data > 100:                           # data의 값이 100보다 크다면
        led_red.data(HIGH)                   # 빨강 LED 켜기
        led_blue.data(LOW)                   # 파랑 LED 끄기

    if data > 150:                           # data의 값이 150보다 크다면
        led_red.data(LOW)                    # 빨강 LED 끄기
        led_blue.data(HIGH)                  # 파랑 LED 켜기


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
