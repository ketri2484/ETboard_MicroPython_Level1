# ********************************************************************************
# FileName     : 09._red_led_button_control
# Description  : 빨강 버튼 눌러서 빨강 LED 켜 보기
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
led_red = Pin(D2)                           # 빨강 LED 지정

button_red = Pin(D6)                        # 빨강 버튼 지정

button_red_value = 0                        # 빨강 버튼의 상태


# setup
def setup():
    led_red.init(Pin.OUT)                   # 빨강 LED를 출력으로 설정
    
    button_red.init(Pin.IN)                 # 빨강 버튼을 입력으로 설정

# mainloop
def loop():

    button_red_value = button_red.value()   # 빨강 버튼의 상태 값 저장
    
    if button_red_value == LOW:             # 빨강 버튼을 누르면
        led_red.value(HIGH)                 # 빨강 LED 켜기
    else:
        led_red.value(LOW)                  # 빨강 LED 끄기
        

if __name__ == "__main__":
    setup()
    while True:
        loop()


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘