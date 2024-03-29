# ******************************************************************************************
# FileName     : 03._led_button_control_1
# Description  : 파랑 버튼 눌러서 파랑 LED 켜 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.28 : PEJ : 파일명, 주석 수정
# ******************************************************************************************


# import
import time                                 # 시간 관련 라이브러리
from machine import Pin                     # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *        # ETboard 핀 관련 모듈


# global variable
button_blue = Pin(D7)                       # 파랑 버튼 핀 지정

led_blue = Pin(D3)                          # 파랑 LED 핀 지정


# setup
def setup():
    led_blue.init(Pin.OUT)                  # 파랑 LED를 출력 모드로 설정
    
    button_blue.init(Pin.IN)                # 파랑 버튼을 입력 모드로 설정


# main loop
def loop():
    button_blue_value = button_blue.value() # 파랑 버튼의 값을 저장
    
    if button_blue_value == LOW:            # 파랑 버튼의 값이 LOW라면
        led_blue.value(HIGH)                # 파랑 LED 켜기
        print("파랑 버튼이 눌림")           # 쉘에 "파랑 버튼이 눌림" 출력
    else:                                   # 파랑 버튼의 값이 LOW가 아니라면
        led_blue.value(LOW)                 # 파랑 LED 끄기
        print("파랑 버튼이 눌리지 않음")    # 쉘에 "파랑 버튼이 눌리지 않음" 출력

    time.sleep(1)


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
