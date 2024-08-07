import sys
sys.stdin = open("input.txt", "r")

T = int(input())   #10

for test_case in range(1, T + 1):
    N, M = map(int,input().split()) # N = 행,열의 수, 5*5  / M = 파리채의 크기, 2*2
    arr = [list(map(int, input().split()))for _ in range(N)]
    # print(arr)

    max_kill = 0  #제일 많이 죽인 파리 개수
    for i in range(N):
        for j in range(N):
            M_kill = 0   #파리채로 몇 마리를 죽일 수 있는지
            for k in range(i, i+M):  #세로로 i부터 파리채의 크기까지
                for v in range(j, j+M):  #가로로 j부터 파리채의 크기까지
                    if 0 <= k < N and 0 <= v <N: #그 범위가 arr 안에 있다면
                        M_kill += arr[k][v]   #M_kill에다가 그 값을 더해준다
            if max_kill < M_kill: #만약 그 값이 max_kill값보다 작으면
                max_kill = M_kill #그 값을 바꿔준다

    print(f'#{test_case} {max_kill}')

