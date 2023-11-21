# ********************************************************************************
# FileName     : 09._blue_led_button_control.Ex
# Description  : 파랑 버튼 눌러서 파랑 LED 켜 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 
# ********************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
led_blue = Pin(D3)                            # 파랑 LED 지정

button_blue = Pin(D6)                         # 파랑 버튼 지정

button_blue_value = 0                         # 파랑 버튼의 상태


# setup
def setup():
    led_blue.init(Pin.OUT)                    # 파랑 LED를 출력으로 설정
    
    button_blue.init(Pin.IN)                  # 파랑 버튼을 입력으로 설정


# mainloop
def loop():
    
    button_blue_value = button_blue.value()   # 파랑 버튼의 상태 값 저장
    
    if button_blue_value == LOW:              # 파랑 버튼을 누르면
        led_blue.value(HIGH)                  # 파랑 LED 켜기
    else:
        led_blue.value(LOW)                   # 파랑 LED 끄기
        

if __name__ == "__main__":
    setup()
    while True:
        loop()


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘