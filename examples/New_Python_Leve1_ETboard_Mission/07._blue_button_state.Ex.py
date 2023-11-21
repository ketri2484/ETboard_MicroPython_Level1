# ********************************************************************************
# FileName     : 07._blue_button_state.Ex
# Description  : 파랑 버튼 눌렀다, 뗐다 해 보기
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
button_blue = Pin(D7)                         # 파랑 버튼 지정


# setup
def setup():
    button_blue.init(Pin.IN)                  # 파랑 버튼을 입력으로 설정


# main loop
def loop():
    button_blue_state = button_blue.value()   # 파랑 버튼의 값을 저장

    if button_blue_state == LOW:              # 파랑 버튼 상태 체크
        print("버튼이 눌림")                   # 파랑 버튼이 눌리면 쉘에 "버튼이 눌림" 출력
    else:
        print("버튼이 눌리지 않음")            # 파랑 버튼이 눌리지 않으면 쉘에 "버튼이 눌리지 않음" 출력

    time.sleep(0.1)                            # 0.1초 대기



if __name__ == "__main__":
    setup()
    while True:
        loop()


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘