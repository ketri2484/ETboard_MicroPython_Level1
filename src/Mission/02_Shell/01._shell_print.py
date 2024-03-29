# ******************************************************************************************
# FileName     : 04._shell_print
# Description  : 쉘에 반려동물 이름 출력해 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 2024.03.28 : PEJ : 파일명, 코드, 주석 수정
# ******************************************************************************************


# import
import time                           # 시간 관련 라이브러리


# setup
def setup():
    pass                              # 아무것도 하지 않고 건너뜀


# main loop
def loop():
    print("puppy_name")               # 큰따옴표 사이에 반려동물 이름을 작성해 주세요.
    time.sleep(1)                     # 1초 기다리기


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
