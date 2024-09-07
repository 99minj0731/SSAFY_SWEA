import sys
sys.stdin = open("input.txt", "r")

T = int(input())   #3

for test_case in range(1, T + 1):
    N,M = map(int, input().split()) # N=3, M=5
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1] #우 하 좌 상
    dj = [1, 0, -1, 0]

    max_sum_num = 0
    for i in range(N):
        for j in range(M):
            sum_num = arr[i][j]
            for k in range(4):     #기준 원소 기준 상하좌우의 원소의 idx
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:    #배열 안에 있을 경우에만
                    sum_num += arr[ni][nj]
            if max_sum_num < sum_num :
                max_sum_num = sum_num

    print(f'#{test_case} {max_sum_num}')

