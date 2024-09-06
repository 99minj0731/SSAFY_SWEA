import sys
sys.stdin = open('input.txt')

# 육지와 육지 사이중에서 가장 먼곳에 보물 놓기
def treasure(r, c, sum_d): #sum_d : 지금까지 간 거리
    global max_distance

    # 해당 위치가 육지일 때 탐색
    while arr[r][c] == 'L':
        # 상우하좌 탐색해서 육지가 있는 곳이라면 cnt += 1
        for k, l in delta:
            nr, nc = r+k, c+l
            # 해당 범위 내에 있을 때만
            if 0 <= nr < N and 0 <= nc < M:
                # 육지일 경우
                if arr[nr][nc] == 'L':
                    visited[nr][nc] = 1
                    max_distance += 1
                    treasure(nr, nc, sum_d + 1)


# N = 세로, M = 가로
N, M = map(int, input().split())
arr = [input()for _ in range(N)]
#['WLLWWWL', 'LLLWLLL', 'LWLWLWW', 'LWLWLLL', 'WLLWLWW']

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌


# 방문을 표시할 곳
visited = [[0] * N for _ in range(M)]

max_distance = 0
result = 0

treasure(0, 0, 0)
