# ******************************************************************************************
# FileName     : 01._button_one_status
# Description  : 빨강 버튼을 눌렀다 뗐다 해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Modified     : 2024.03.13 : PEJ : 파일명, 주석 수정
# ******************************************************************************************


# import
import time                                # 시간 관련 라이브러리
from machine import Pin                    # 핀 및 시간 관련 모듈
from ETboard.lib.pin_define import *       # ETboard 핀 관련 모듈


# global variable
button_red = Pin(D6)                       # 빨강 버튼 핀 지정


# setup
def setup():
    button_red.init(Pin.IN)                # 빨강 버튼을 입력 모드로 설정


# main loop
def loop():
    button_red_value = button_red.value()  # 빨강 버튼의 값을 저장

    if button_red_value == LOW:            # 빨강 버튼의 값이 LOW라면
        print("버튼이 눌림")               # 쉘에 "버튼이 눌림" 출력
    else:                                  # 빨강 버튼의 값이 LOW가 아니라면
        print("버튼이 눌리지 않음")        # 쉘에 "버튼이 눌리지 않음" 출력

    time.sleep(0.1)                        # 0.1초 기다리기


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
