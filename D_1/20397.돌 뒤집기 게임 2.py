import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    # N = 돌의 수, M = 뒤집기 횟수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        i, j = list(map(int, input().split()))
        i = i - 1

        for k in range(1, j + 1):
            if 0 <= i-k < N and 0 <= i+k < N:
                if arr[i-k] == arr[i+k]:
                    if arr[i-k] == 0:
                        arr[i-k] = 1
                        arr[i+k] = 1
                    else:
                        arr[i - k] = 0
                        arr[i + k] = 0
                else:
                    pass


    print(f'#{test_case}', *arr)
