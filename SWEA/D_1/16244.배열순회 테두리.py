import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    # i = 행, j = 열, N = 상자의 크기  / 3, 4, 3
    i, j, N = list(map(int, input().split()))

    arr = [[0] * 10 for _ in range(10)]

    # 가로로 먼저 1을 만들어 준다.
    for k in range(N):   # k = 0, 1, 2 (자신부터 끝까지)
        arr[i][j + k] = 1
        arr[i + N - 1][j + k] = 1

    # 세로로 1을 만들어 준다.
    for k in range(1, N): # k = 1, 2
        arr[i + k][j] = 1
        arr[i + k][j + N - 1] = 1


    print(f'#{test_case}')

    for result in arr:
        print(*result)