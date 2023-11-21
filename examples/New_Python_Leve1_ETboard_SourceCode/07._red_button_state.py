# ********************************************************************************
# FileName     : 07._red_button_state
# Description  : 빨강 버튼 눌렀다, 뗐다 해 보기
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
button_red = Pin(D6)                         # 빨강 버튼 지정


# setup
def setup():
    button_red.init(Pin.IN)                  # 빨강 버튼을 입력으로 설정


# main loop
def loop():
    button_red_status = button_red.value()   # 빨강 버튼의 값을 저장

    if button_red_status == LOW:             # 빨강 버튼 상태 체크
        print("버튼이 눌림")                  # 빨강 버튼이 눌리면 쉘에 "버튼이 눌림" 출력
    else:
        print("버튼이 눌리지 않음")           # 빨강 버튼이 눌리면 쉘에 "버튼이 눌리지 않음" 출력

    time.sleep(0.1)                           # 0.1초 대기



if __name__ == "__main__":
    setup()
    while True:
        loop()


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘