import sys
sys.stdin = open('input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 오목판의 크기 N * N
    arr = [list(map(str, input()))for _ in range(N)]

    dr = [-1, 0, 1, 0, 1]  # 상 우 하 좌 대각선
    dc = [0, 1, 0, -1, 1]

    # 오른쪽 탐색
    for i in range(N):     # 0, 1, 2, 3, 4
        count = 0
        for j in range(0, N-4): # 0 첫번쨰 열만 탐색
            if arr[i][j] == 'o':    # 기준 값에 오목이 있다면 탐색을 시작하겠다.
                while count >= 5:  # count의 값이 5이상이 될 때까지 반복
                    nr = i + dr[0]
                    nc = j + dc[1]
                    # 만약 배열 안에 있고 그 값에 오목이 있다면
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        count += 1
                    print('YES')
                    break

    # 아래 탐색
    for i in range(N):     # 0, 1, 2, 3, 4
        count = 0
        for j in range(0, N-4): # 0
            if arr[i][j] == 'o':    # 기준 값에 오목이 있다면 탐색을 시작하겠다.
                while count >= 5:  # count의 값이 5이상이 될 때까지 반복
                    nr = i + dr[2]
                    nc = j + dc[2]
                    # 만약 배열 안에 있고 그 값에 오목이 있다면
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        count += 1
                    print('YES')
                    break

    # 대각선 탐색
    for i in range(0, N-4):     # 0, 1, 2, 3, 4
        count = 0
        for j in range(0, N-4): # 0, 1, 2, 3, 4
            if arr[i][j] == 'o':    # 기준 값에 오목이 있다면 탐색을 시작하겠다.
                while count >= 5:  # count의 값이 5이상이 될 때까지 반복
                    nr = i + dr[5]
                    nc = j + dc[5]
                    # 만약 배열 안에 있고 그 값에 오목이 있다면
                    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'o':
                        count += 1
                    print('YES')
                else:
                    print('NO')

