import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input()) #3

for text_case in range(1, T+1):
    N, M = list(map(int, input().split()))   # N=피자 개수 3, M = 치즈 양 5
    pizza = list(map(int, input().split()))  # 7 2 6 5 3

    pizza_list = deque(pizza)


    for i in range(N):
        if pizza[i]
        pizza[i] // 2


