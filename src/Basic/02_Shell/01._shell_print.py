# ******************************************************************************************
# FileName     : 01._shell_print
# Description  : 쉘에 "Hello ETboard!" 출력해 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 2024.03.13 : PEJ : 파일명, 코드 수정
# Modified     : 2024.03.26 : PEJ : 코드 구조 변경(setup, loop)
# ******************************************************************************************


# import
import time                           # 시간 관련 라이브러리


# setup
def setup():
    pass                              # 아무것도 하지 않고 건너뜀


# main loop
def loop():
    print("Hello ETboard!")           # 쉘에 "Hello ETboard!" 출력

    time.sleep(1)                     # 1초간 대기

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
