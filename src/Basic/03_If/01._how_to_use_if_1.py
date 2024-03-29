# ******************************************************************************************
# FileName     : 01._how_to_use_if_1
# Description  : if 조건문 알아보기_1
# Description  : data의 값이 LOW와 같으면 쉘에 "data의 값은 LOW입니다."를 출력해 보기
# Author       : 오경석
# Created Date : 2023.11.01
# Reference    :
# Modified     : 2024.03.13 : 변수명, 파일명, 주석 수정
# Modified     : 2024.03.26 : PEJ : 코드 구조 변경(setup, loop)
# ******************************************************************************************


# import
import time                                      # 시간 관련 라이브러리


# global variable
data = "LOW"                                     # data 변수에 "LOW" 저장


# setup
def setup():
    pass                                         # 아무것도 하지 않고 건너뜀


# main loop
def loop():
    if data == "LOW":                            # data의 값이 "LOW"라면
        print("data의 값은 LOW입니다.")          # 쉘에 "data 값은 LOW입니다." 출력

    time.sleep(1)                                # 1초간 대기


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
