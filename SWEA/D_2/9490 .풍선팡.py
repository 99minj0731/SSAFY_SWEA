T = int(input()) #3

for test_case in range(1, T+1):
    # N = 행, M = 열
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    max_cnt = 0

    di = [0, 1, 0, -1]  #우하좌상
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            count = arr[i][j]      # 자기자신은 포함시켜 놓고
            for l in range(1, arr[i][j] + 1):  # 4방향으로 해당 꽃개수만큼 더해준다. 만약에 2개라면 # 1, 2
                for k in range(4):             # 4방향으로 으로 총 4번 반복 # 0, 1, 2, 3
                    ni = i + di[k] * l         # 0, 1, 2, 3 >  0, 2, 0, -2
                    nj = j + dj[k] * l
                    if 0 <= ni < N and 0 <= nj < M:     # 영역을 벗어나지 않는다면
                        count += arr[ni][nj]

            if max_cnt < count:
                max_cnt = count

    print(f'#{test_case} {max_cnt}')