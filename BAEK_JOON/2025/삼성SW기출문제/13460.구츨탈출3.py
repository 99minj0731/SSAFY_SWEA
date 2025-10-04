import sys
sys.stdin = open('input.txt')
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]

rx = ry = bx = by = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 빨간공, 파란공 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

# 구슬 이동하기
def move(x, y, dx, dy):
    cnt = 0
    while True:
        if board[x+dx][y+dy] == "#": # '#'이 나올때까지 이동 
            break
        cnt += 1
        x += dx
        y += dy

        if board[x][y] == 'O':
            break
    return x, y, cnt

def bfs():
    global rx, ry, bx, by
    visited = set()
    q= deque()
    q.append((rx, ry, bx, by, 0))
    visited.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth >= 10:
            return -1 
        
        for l in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[l], dy[l])
            nbx, nby, bcnt = move(bx, by, dx[l], dy[l])

            if board[nbx][nby] == "O":
                continue
            if board[nrx][nry] == "O":
                return depth + 1
            
            # r, b 공이 같은 위치에 있다면
            if nrx == nbx and nry == nby :
                if rcnt > bcnt :
                    nrx = nrx - dx[l]
                    nry = nry - dy[l]
                else:
                    nbx = nbx - dx[l]
                    nby = nby - dy[l]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))
    return -1

print(bfs())