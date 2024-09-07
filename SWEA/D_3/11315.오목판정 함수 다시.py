import sys
sys.stdin = open('input.txt', 'r')

def check(N, arr):

    delta = [(1, -1), (1, 0), (1, 1), (0, 1)]  # 왼쪽대각선, 아래, 오른쪽대각선, 오른쪽

    for r in range(N): # 행 탐색
        for c in range(N): # 열 탐색
            for dr, dc in delta:     # delta 탐색 (1, -1)부터 탐색
                for k in range(5):   # 0(자기자신) ~ 4까지 총 5개
                    nr = r + dr * k
                    nc = c + dc * k
                    #조건이 안될 경우 : 해당 값이 밖으로 벗어나거나 오목이 없을 떄
                    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 'o':
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input()) #4

for test_case in range(1, T + 1):
    N = int(input())  # N * N 의 행렬 #5
    arr = [list(map(str, input()))for _ in range(N)]

    result = check(N, arr)
    print(f'#{test_case} {result}')


