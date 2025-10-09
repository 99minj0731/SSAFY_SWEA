import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
tomato = [list(input().split())for _ in range(M)]

q = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 익은 토마토 위치와 날짜 deque에 넣기
for i in range(M):
    for j in range(N):
        if tomato[i][j] == "1":
            q.append((i, j, 0))


def bfs():

    final_day = 0

    while q:
        x, y, day = q.popleft()
        final_day = day
        # 사분면으로 익은토마토로 만들기
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            # 범위 내에 있고, 0일 때만 1로 바꾸고 날짜 +1 해서 q에 넣기
            if 0 <= nx < M and 0 <= ny < N:
                if tomato[nx][ny] == "0":
                    tomato[nx][ny] = "1"
                    q.append((nx, ny, day + 1))

    # 만약 0이 존재한다면 토마토는 다 익을 수 없는것
    for n in range(M):
        for m in range(N):
            if tomato[n][m] == "0": 
                return -1
            
    return final_day
print(bfs())