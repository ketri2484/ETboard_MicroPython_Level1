# ********************************************************************************
# FileName     : 06._find_out_if_conditional_statements_2.Ex
# Description  : if 조건문을 사용하여 LED 켜지게 해 보기_2
# Description  : A 값이 100 보다 크면 빨강, 150보다 크면 파랑 LED 켜지게 해 보기
# Author       : 오경석
# Created Date : 2023.11.02
# Reference    :
# Question     : A에 151 넣으면 어떻게 될까요?
# Modified     : 
# ********************************************************************************


# import
from ETboard.lib.pin_define import*
from machine import Pin
import time


# global variable
A = 101                    # A 라는 변수에 101 넣기


# setup
PinD2 = Pin(D2, Pin.OUT)   # 빨강 LED를 출력으로 설정
PinD3 = Pin(D3, Pin.OUT)   # 파랑 LED를 출력으로 설정


# main loop

# A값이 100 보다 크면 빨강 LED가 켜지게 하기
if A > 100:
    PinD2.value(HIGH)      # 빨강 LED 켜기
    PinD3.value(LOW)       # 파랑 LED 끄기

# A값이 150 보다 크면 파랑 LED가 켜지게 하기
if A > 150:
    PinD3.value(HIGH)      # 파랑 LED 켜기
    PinD2.value(LOW)       # 빨강 LED 끄기    


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘