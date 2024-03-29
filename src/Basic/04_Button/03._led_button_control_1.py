# ******************************************************************************************
# FileName     : 03._led_button_control_1
# Description  : 빨강 버튼 눌러 빨강 LED 켜 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.13 : PEJ : 파일명, 주석 수정
# ******************************************************************************************


# import
import time                                 # 시간 관련 라이브러리
from machine import Pin                     # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *        # ETboard 핀 관련 모듈


# global variable
led_red = Pin(D2)                           # 빨강 LED 핀 지정

button_red = Pin(D6)                        # 빨강 버튼 핀 지정


# setup
def setup():
    led_red.init(Pin.OUT)                   # 빨강 LED를 출력 모드로 설정

    button_red.init(Pin.IN)                 # 빨강 버튼을 입력 모드로 설정


# main loop
def loop():
    button_red_value = button_red.value()   # 빨강 버튼의 값을 저장

    if button_red_value == LOW:             # 빨강 버튼의 값이 LOW라면
        led_red.value(HIGH)                 # 빨강 LED 켜기
        print("빨강 버튼이 눌림")           # 쉘에 "빨강 버튼이 눌림" 출력
    else:                                   # 빨강 버튼의 값이 LOW가 아니라면
        led_red.value(LOW)                  # 빨강 LED 끄기
        print("빨강 버튼이 눌리지 않음")    # 쉘에 "빨강 버튼이 눌리지 않음" 출력

    time.sleep(0.1)


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
