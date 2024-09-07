import sys
sys.stdin = open("input.txt", "r")

T = int(input())  #1

for test_case in range(1, T + 1):
    N = int(input())  #4
    arr = [([0] * N)for _ in range(N)]    #일단 0으로 채워서 만들고 4*4

    n, m = 0, -1 #현재 달팽이의 위치 지정 arr[0][0]부터 1로 만들어야하니까
    move = [[0,1],[1,0],[0,-1],[-1,0]]  # 우 하 좌 상

    for i in range(N*N) :  #총 16번 반복
        nn, nm = n + move[0][0], m + move[0][1]   #새로운 위치 지정 일단 오른쪽으로 이동
        if 0 <= nn < N and 0 <= nm < N: #새로운 위치들이 arr범위를 벗어나지 않는다면
            arr[nn][nm] = arr[n][m] + 1  #새로운 위치에 현재 위치 + 1을 더하겠다.
            n, m = nn, nm  #그리고 현재 위치를 새로운 위치로 바꾸겠다.
        else: #범위를 벗어나면 move의 다음걸로 이동??
    print(arr)









    # print(arr) #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # print(*arr) #[0, 0, 0, 0] [0, 0, 0, 0] [0, 0, 0, 0] [0, 0, 0, 0]
    # for row in arr:    #리스트에 담긴상태로 아래 정렬
    #     print(row)
    # for row in arr:    #숫자로만 아래 정렬
    #     print(*row)
