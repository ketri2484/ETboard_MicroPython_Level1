# ********************************************************************************
# FileName     : 05._find_out_if_conditional_statements_1.Ex
# Description  : if 조건문을 이용하여 LED 켜지게 해 보기_1
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    : A 값에 HIGH를 넣으면 어떻게 될까요?
# Question     : 
# Modified     : 
# ********************************************************************************


# import
from ETboard.lib.pin_define import *
from machine import Pin
import time


# global variable
A = "LOW"                  # A 라는 변수에 LOW 넣기


# setup
PinD2 = Pin(D2, Pin.OUT)   # 빨강 LED를 출력으로 설정
PinD3 = Pin(D3, Pin.OUT)   # 파랑 LED를 출력으로 설정


# main loop

# A값이 LOW 와 같으면 빨강 LED 켜지게 하기
if A == "LOW":
    PinD2.value(HIGH)      # 빨강 LED 켜기

# A값이 HIGH 와 같으면 파랑 LED 켜지게 하기
if A == "HIGH":
    PinD3.value(HIGH)      # 파랑 LED 켜기


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘