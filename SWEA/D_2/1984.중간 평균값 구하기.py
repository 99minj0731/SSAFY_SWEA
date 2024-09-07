import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #3

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))  #[3, 17, 1, 39, 8, 41, 2, 32, 99, 2]

    # 0부터 10000이하의 정수가 주어진다.
    min_num = 100000
    max_num = 0

    for i in numbers:           # 0번째부터 끝까지 돌아서
        if i < min_num:         # 만약 해당 숫자가 min_num보다 작다면
            min_num = i         # 그 해당 값으로 바꿔주고
        if i > max_num:         # 만약 해당 숫자가 max_num보다 크다면
            max_num = i         # 그 해당 값으로 바꿔준다.
    # print(min_num, max_num)     # 1 99

    sum_num = 0
    for i in numbers:  # 그러고 다 끝났으면 한 번 더 돌아서
        sum_num += i   # 해당 값을 더해준다.

    # print(sum_num)   #244
    result = (sum_num - (min_num + max_num)) / 8   #최소값과 최대값을 뺴준 거에 8을 나눈다.

    print(f'#{test_case} {round(result)}')