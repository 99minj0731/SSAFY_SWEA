import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]


    result = 0

    for i in range(N): # 행,렬의 수만큼 반복을 해서
        count = 0
        # 가로로 탐색하기
        for j in range(N):
            if arr[i][j] == 1:   #만약 해당 값이 흰색(1)이라면
                count += 1       #1을 더해주고
            # 만약 해당 값이 검은색(0)이거나 열의 위치가 끝이라면
            if arr[i][j] == 0 or j == N-1:
                if count == K:  #만약 딱 K의 값이라면
                    result += 1
                count = 0    #카운트 값 초기화
                
        # 세로로 탐색하기
        for k in range(N):
            if arr[k][i] == 1:   #만약 해당 값이 흰색(1)이라면
                count += 1
            # 검은색(0)을 만나거나 위치가 끝이라면
            if arr[k][i] == 0 or k == N-1:
                if count == K:
                    result += 1
                count = 0

    print(f'#{test_case} {result}')

