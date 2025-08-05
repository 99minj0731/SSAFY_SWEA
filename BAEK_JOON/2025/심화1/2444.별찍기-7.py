'''
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

N = int(input()) # N = 5

# 규칙 : 1, 3, 5, 7, 9 ,7, 5, 3, 1

start_star = -1 # 일단 -1부터 시작

for i in range(1, N * 2) : # i = 12345 6789
    
    # i가 1.2.3.4.5 < 5 작을때까지는 2개씩 늘려서 출력 
    # 일단 최대의 별의 개수는  2 * N - 1 이다. 
    # 1일 때는 최대 개수 - 1 % 2를 한 값이다. 
    if i <= N : 
        start_star += 2
        blank_number = ((2 * N - 1) - start_star) // 2
        result = (" " * blank_number) + "*" * (start_star)
        print(result)
    # i가 5.6.7.8 일때는 2개찍 줄여서 출력 현재 9잖아. 
    elif i > N :
        start_star -= 2 
        blank_number = ((2 * N - 1) - start_star) // 2
        result = (" " * blank_number) + "*" * (start_star)
        print(result)

    # print("*" * start_star)     
    