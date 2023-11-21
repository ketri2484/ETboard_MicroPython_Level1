# ********************************************************************************
# FileName     : 08._button_all_state.Ex
# Description  : 모든 버튼 눌렀다, 뗐다 해 보기
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
button_red = Pin(D6)                              # 빨강 버튼 지정
button_blue = Pin(D7)                             # 파랑 버튼 지정
button_green = Pin(D8)                            # 초록 버튼 지정
button_yellow = Pin(D9)                           # 노랑 버튼 지정


# setup
def setup():
    button_red.init(Pin.IN)                       # 빨강 버튼을 입력으로 설정
    button_blue.init(Pin.IN)                      # 파랑 버튼을 입력으로 설정
    button_green.init(Pin.IN)                     # 초록 버튼을 입력으로 설정
    button_yellow.init(Pin.IN)                    # 노랑 버튼을 입력으로 설정


# main loop
def loop():
    button_red_state = button_red.value()         # 빨강 버튼의 값을 저장
    button_blue_state = button_blue.value()       # 파랑 버튼의 값을 저장
    button_green_state = button_green.value()     # 초록 버튼의 값을 저장
    button_yellow_state = button_yellow.value()   # 노랑 버튼의 값을 저장
    
    if button_red_state == LOW:                   # 빨강 버튼을 누르면 "빨강 버튼이 눌림" 출력
        print("빨강 버튼이 눌림")
        
    if button_blue_state == LOW:                  # 파랑 버튼을 누르면 "빨강 버튼이 눌림" 출력
        print("파랑 버튼이 눌림")
    
    if button_green_state == LOW:                 # 초록 버튼을 누르면 "빨강 버튼이 눌림" 출력
        print("초록 버튼이 눌림")
        
    if button_yellow_state == LOW:                # 노랑 버튼을 누르면 "빨강 버튼이 눌림" 출력
        print("노랑 버튼이 눌림")

    time.sleep(0.1)                               # 0.1초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()
 
 
# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘