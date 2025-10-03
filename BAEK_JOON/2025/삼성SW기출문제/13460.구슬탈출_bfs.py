import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())

board = [list(input().strip()) for _ in range(N)]

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

rx = ry = bx = by = 0

# R, B 초기 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j

# 구슬 굴리기
def move(x, y, dx, dy):
    cnt = 0
    while True:
        if board[x+dx][y+dy] == "#":
            break
        x += dx
        y += dy
        # 몇 칸 이동을 했는지, 파란공이 먼저 들어갈 수도 있고, 파란공과 빨간공이 같은 위치에 있을 수 있기 때문에 
        cnt += 1  
        if board[x][y] == "O":
            break
    return x, y, cnt

def bfs():
    global rx, ry, bx, by
    visited = set()
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            return -1 
    
        for i in range(4): # 상우하좌 탐색하기
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])

            # 공중에 하나라도 구멍을 찾았다면
            if board[nbx][nby] == "O":
                continue
            if board[nrx][nry] == "O":
                return depth + 1
            
            # 만약 공들이 같은 자리에 있다면 멀리서 온 공을 그 전으로 돌리기
            if nrx == nbx and nry == nby:
                if rcnt > bcnt :
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1

print(bfs())