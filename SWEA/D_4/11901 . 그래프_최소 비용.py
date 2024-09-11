import sys
sys.stdin = open('input.txt')
from collections import deque

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def bfs(col, row):
    global visited

    Q = deque()
    Q.append((col, row))
    # 시작점은 0으로 만들고
    visited[col][row] = 0

    # Q가 빌 때까지 실행
    while Q:
        c, r = Q.popleft()

        for dx, dy in delta:
            nc = c + dx
            nr = r + dy
            # 배열 안에 있을 때만
            if 0 <= nc < N and 0 <= nr < N:
                cont = 1
                # 다음 가는 곳의 경사가 더 높다면 경사 차이만큼 더해줌
                if arr[nc][nr] > arr[c][r]:
                    cont += arr[nc][nr] - arr[c][r]
                # 최소값으로 갱신해줌
                if visited[nc][nr] > visited[c][r] + cont:
                    visited[nc][nr] = visited[c][r] + cont
                    Q.append((nc, nr))

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 3
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[1e9] * N for _ in range(N)]

    bfs(0, 0)

    print(f'#{test_case} {visited[N-1][N-1]}')

