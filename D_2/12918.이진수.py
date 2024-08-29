import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    N, arr = input().split() # 일단 문자열로 받고
    N = int(N)  # 문자 개수는 숫자로 바꿔줌

    ans = []

    for i in arr:  # i = 4, 7, F, E 이건 16진수

        # 숫자일 경우
        if arr[i] ==