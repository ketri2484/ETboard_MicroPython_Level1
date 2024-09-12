# ********************************************************************************
# FileName     : 01._led_blue_turn_on
# Description  : 파랑 LED 켜 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 
# ********************************************************************************


# import
from ETboard.lib.pin_define import *
from machine import Pin
import time


# global definition


# setup
PinD3 = Pin(D3, Pin.OUT)   # 파랑 LED를 출력으로 설정


# main loop

time.sleep(2)              # 2초 기다리기

PinD3.value(HIGH)          # 파랑 LED 켜기


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘