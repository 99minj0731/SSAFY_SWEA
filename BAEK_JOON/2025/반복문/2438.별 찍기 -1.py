'''
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

# for i in range(1, T + 1):
#     result = '*' * i
#     print(result)

n = 1

while n <= T :
    result = '*' * n
    n = n + 1
    print(result)