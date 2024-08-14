import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    i, j = [list(map(int, input().split()))for _ in range(M)]

    print(N,M)