import sys
sys.stdin = open('input.txt', 'r')

dr = [-1, -1, -1, 0, 1, 1, 1, 0] #시계방향
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

T = int(input()) #1

for test_case in range(1, T + 1):
    # N = 보드의 한 변의 길이 , M = 플레이어가 돌을 놓는 횟수
    N, M = map(int, input().split()) # 4, 12
    board = [[0] * N for _ in range(N)]

    # 기본 돌 4개 셋팅하기 // 흑돌 = 1 , 백돌 = 2
    mid = N // 2 - 1

    board[mid][mid] = 2
    board[mid][mid + 1] = 1
    board[mid + 1][mid + 1] = 2
    board[mid + 1][mid] = 1
    # print(board) #[[0, 0, 0, 0], [0, 2, 1, 0], [0, 1, 2, 0], [0, 0, 0, 0]]

    for _ in range(M):
        r, c, col = map(int, input().split())
        r, c = r - 1, c - 1

        board[r][c] = col   # 돌을 해당 위치에 놓는다.

        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]       #주변 탐색 시작!
            while 0 <= nr < N and 0 <= nc < N : # board 안을 벗어나지 않을 때까지 쭉 직진
                if board[nr][nc] == 0:          #만약 주변에 돌이 없으면 break
                    break
                if board[nr][nc] == col:        #만약에 쭉 갔는데 나랑 같은 색의 돌을 만났다.
                    nr, nc = nr - dr[i], nc - dc[i]  #한 칸 전으로 이동
                    while not (r == nr and c == nc):     #나의 위치까지 올 때까지
                        board[nr][nc] = col       #나랑 같은 색으로 색을 바꿔준다
                        nr, nc = nr - dr[i], nc - dc[i]  #계속 한 칸 전으로 이동
                    break

                nr, nc = nr + dr[i], nc + dc[i]  #나랑 같은 돌이 아닐경우 계속 직진

    B = W = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                B += 1
            elif board[r][c] == 2:
                W += 1

    print(f'#{test_case} {B} {W}')