import sys
sys.stdin = open("input.txt", "r")

T = int(input()) #5

for test_case in range(1, T + 1):
    string = input()  # 22220228 , type=str

    #년, 월, 일 기준으로 구분, 셋 다 문자열
    year = string[0:4]
    month = string[4:6]
    date = string[6:9]

    # 마지막 날짜 기준 분류
    date_31 = [1, 3, 5, 7, 8, 10, 12]
    date_30 = [4, 6, 9, 11]
    date_28 = [2]

    #마지막 날 지정
    last_day = 0
    if int(month) in date_31:
        last_day = 31
    elif int(month) in date_30:
        last_day = 30
    elif int(month) in date_28:
        last_day = 28
    else:
        last_day = -1

    if int(date) <= 0:
        print(f'#{test_case} -1')
    elif last_day < int(date):
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {year}/{month}/{date}')


