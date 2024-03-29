# ******************************************************************************************
# FileName     : 04._led_button_control_2
# Description  : 빨강, 파랑 버튼 눌러서 모든 LED 켰다 껐다 해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.28 : PEJ : 파일명, 코드, 주석 수정
# ******************************************************************************************


# import
import time                                 # 시간 관련 라이브러리
from machine import Pin                     # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *        # ETboard 핀 관련 모듈


# global variable
button_red = Pin(D6)                        # 빨강 버튼 핀 지정
button_blue = Pin(D7)                       # 파랑 버튼 핀 지정

led_red = Pin(D2)                           # 빨강 LED 핀 지정
led_blue = Pin(D3)                          # 파랑 LED 핀 지정
led_green = Pin(D4)                         # 초록 LED 핀 지정
led_yellow = Pin(D5)                        # 노랑 LED 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)                    # 빨강 LED를 출력 모드로 설정
    led_blue.init(Pin.OUT)                   # 파랑 LED를 출력 모드로 설정
    led_green.init(Pin.OUT)                  # 초록 LED를 출력 모드로 설정
    led_yellow.init(Pin.OUT)                 # 노랑 LED를 출력 모드로 설정
    
    button_red.init(Pin.IN)                  # 빨강 버튼을 입력 모드로 설정
    button_blue.init(Pin.IN)                 # 파랑 버튼을 입력 모드로 설정


# main loop
def loop():
    button_red_value = button_red.value()    # 빨강 버튼의 값 저장
    button_blue_value = button_blue.value()  # 파랑 버튼의 값 저장

    if button_red_value == LOW:              # 빨강 버튼의 값이 LOW라면
        led_red.value(HIGH)                  # 빨강 LED 켜기
        led_blue.value(HIGH)                 # 파랑 LED 켜기
        led_green.value(HIGH)                # 초록 LED 켜기
        led_yellow.value(HIGH)               # 노랑 LED 켜기
        print("빨강 버튼이 눌림")            # 쉘에 "빨강 버튼이 눌림" 출력

    if button_blue_value == LOW:             # 파랑 버튼의 값이 LOW라면
        led_red.value(LOW)                   # 빨강 LED 끄기
        led_blue.value(LOW)                  # 파랑 LED 끄기
        led_green.value(LOW)                 # 초록 LED 끄기
        led_yellow.value(LOW)                # 노랑 LED 끄기
        print("파랑 버튼이 눌림")            # 쉘에 "파랑 버튼이 눌림" 출력      


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
