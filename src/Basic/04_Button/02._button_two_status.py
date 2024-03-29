# ******************************************************************************************
# FileName     : 02._button_two_status
# Description  : 초록, 노랑 버튼을 눌렀다 뗐다 해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.13 : PEJ : 파일명, 주석 수정
# ******************************************************************************************


# import
import time                                      # 시간 관련 라이브러리
from machine import Pin                          # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *             # ETboard 핀 관련 모듈


# global variable
button_green = Pin(D8)                           # 초록 버튼 핀 지정
button_yellow = Pin(D9)                          # 노랑 버튼 핀 지정


# setup
def setup():
    button_green.init(Pin.IN)                    # 초록 버튼을 입력 모드로 설정
    button_yellow.init(Pin.IN)                   # 노랑 버튼을 입력 모드로 설정


# main loop
def loop():
    button_green_value = button_green.value()    # 초록 버튼의 값을 저장
    button_yellow_value = button_yellow.value()  # 노랑 버튼의 값을 저장

    if button_green_value == LOW:                # 초록 버튼의 값이 LOW라면
        print("초록 버튼이 눌림")                # 쉘에 "초록 버튼이 눌림" 출력  
    elif button_yellow_value == LOW:             # 노랑 버튼의 값이 LOW라면
        print("노랑 버튼이 눌림")                # 쉘에 "노랑 버튼이 눌림" 출력
    else:                                        # 빨강, 파랑 버튼의 값이 LOW가 아니라면
        print("버튼이 눌리지 않음")              # 쉘에 "노랑 버튼이 눌림" 출력

    time.sleep(0.1)                              # 0.1초 기다리기


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
