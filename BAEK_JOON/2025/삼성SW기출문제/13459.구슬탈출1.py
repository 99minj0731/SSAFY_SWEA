'''
스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 10번 이하로 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

출력
파란 구슬을 구멍에 넣지 않으면서 빨간 구슬을 10번 이하로 움직여서 빼낼 수 있으면 1을 없으면 0을 출력한다.
'''

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# R, B공 위치 찾기
rx = ry = bx = by = 0 
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i, j
        if board[i][j] == "B":
            bx, by = i, j

# 구슬 굴리기 
def move(x, y, dx, dy):
    cnt = 0 # 몇 칸 이동했는지

    while True:
        nx, ny = x+dx, y+dy # 다음칸
        if board[nx][ny] == "#":
            break 
        
        if board[nx][ny] == "O":
            x, y = nx, ny
            cnt += 1
            break
        
        x, y = nx, ny
        cnt += 1

    return x, y, cnt # 이동한 자리 위치값 및 몇 칸 이동했는지

def bfs():
    global rx, ry, bx, by
    visited = set()
    q = deque()
    q.append((rx, ry, bx, by, 0)) # 빨간공, 파란공 위치 및 이동횟수
    visited.add((rx, ry, bx, by)) # 방문 표시

    while q:
        rx, ry, bx, by, num = q.popleft() 

        # 10 이하일때만 찾아보기
        if num < 10:

            # 사방면으로 굴리기
            for k in range(4):
                nrx, nry, rcnt = move(rx, ry, dx[k], dy[k])
                nbx, nby, bcnt = move(bx, by, dx[k], dy[k])
                
                # 만약에 파란공이 탈출 했을 경우 실패
                if board[nbx][nby] == "O":
                    continue # 다음 for문으로 넘어감
                if board[nrx][nry] == "O":
                    return 1
                
                # 자리 재정비 하기 (같은 위치에 R, B가 있을 수 있으니)
                if nrx == nbx and nry == nby :
                    if rcnt > bcnt:
                        nrx -= dx[k]
                        nry -= dy[k]
                    else:
                        nbx -= dx[k]
                        nby -= dy[k]
                
                # 간곳이 아니라면 갔다고 표시
                if ((nrx, nry, nbx, nby)) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby, num + 1))

        # 10회 안에 공 탈출 실패
        else:
            return 0
        
    # 10번 이하로 다 돌아봤는데 안됨
    return 0

print(bfs())
        