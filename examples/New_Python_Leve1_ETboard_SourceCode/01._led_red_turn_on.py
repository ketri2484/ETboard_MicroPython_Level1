# ********************************************************************************
# FileName     : 01._red_led_turn_on
# Description  : 빨강 LED 켜 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 
# ********************************************************************************


# import
from ETboard.lib.pin_define import *
from machine import Pin
import time


#global definition


# setup
PinD2 = Pin(D2, Pin.OUT)   # 빨강 LED를 출력으로 설정


# main loop
time.sleep(2)              # 2초 기다리기

PinD2.value(HIGH)          # 빨강 LED 켜기


# ┌───────────────────────────────────────────┐
# │                                           │
# │(주)한국공학기술연구원 http://et.ketri.re.kr │
# │                                           │
# └───────────────────────────────────────────┘