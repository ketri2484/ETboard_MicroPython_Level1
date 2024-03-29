# ******************************************************************************************
# FileName     : 03._if_led_control_3
# Description  : 조건문 if를 이용하여 LED 제어해 보기_3
# Description  : data의 숫자에 따라 다른 LED 켜 보기
# Author       : 박은정
# Created Date : 2023.03.28
# Reference    :
# Question     : data의 값이 달라진다면 어떻게 될까요?
# Modified     :
# ******************************************************************************************


# import
from machine import Pin                      # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *         # ETboard 핀 관련 모듈


# global variable
led_red = Pin(D2)                            # 빨강 LED 핀 지정
led_blue = Pin(D3)                           # 파랑 LED 핀 지정
led_green = Pin(D4)                          # 초록 LED 핀 지정
led_yellow = Pin(D5)                         # 노랑 LED 핀 지정

data = 50                                    # data 변수에 50 저장


# setup
def setup():
    led_red.init(Pin.OUT)                    # 빨강 LED를 출력 모드로 설정
    led_blue.init(Pin.OUT)                   # 파랑 LED를 출력 모드로 설정
    led_green.init(Pin.OUT)                  # 초록 LED를 출력 모드로 설정
    led_yellow.init(Pin.OUT)                 # 노랑 LED를 출력 모드로 설정


# main loop
def loop():
    if data < 100:                           # data의 값이 100보다 작다면
        led_red.value(HIGH)                  # 빨강 LED 켜기
        led_blue.value(LOW)                  # 파랑 LED 끄기
        led_green.value(LOW)                 # 초록 LED 끄기
        led_yellow.value(LOW)                # 노랑 LED 끄기
    elif data < 200:                         # data의 값이 200보다 작다면
        led_red.value(LOW)                   # 빨강 LED 끄기
        led_blue.value(HIGH)                 # 파랑 LED 켜기
        led_green.value(LOW)                 # 초록 LED 끄기
        led_yellow.value(LOW)                # 노랑 LED 끄기
    elif data < 300:                         # data의 값이 300보다 작다면
        led_red.value(LOW)                   # 빨강 LED 끄기
        led_blue.value(LOW)                  # 파랑 LED 끄기
        led_green.value(HIGH)                # 초록 LED 켜기
        led_yellow.value(LOW)                # 노랑 LED 끄기
    else:                                    # data의 값이 300보다 같거나 크다면
        led_red.value(LOW)                   # 빨강 LED 끄기
        led_blue.value(LOW)                  # 파랑 LED 끄기
        led_green.value(LOW)                 # 초록 LED 끄기
        led_yellow.value(HIGH)               # 노랑 LED 켜기


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

