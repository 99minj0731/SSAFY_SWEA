import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #10

for test_case in range(1, T+1):
    N, K = map(int, input().split())   # N * N 으로 구성된, K=3
    arr = [list(map(int, input().split()))for _ in range(N)]

    count = 0

    # 가로 열 탐색
    for i in range(N-1):
        for j in range(N - K + 1):
            if arr[i][j] == 1:  #해당 값이 1이고
                if arr[i][j-1] == 0 or j == 0:   # 확인하려는 원소의 왼쪽 값이 검은색(0)이거나 j가 0이라면 탐색하겠다.
                    for k in range(K):           # 찾을 글자수만큼 돌아서
                        if arr[i][j+k] == 1:     #그 곳도 흰색(1)이라면 넘어간다.
                            pass
                        else:
                            break
                    # 만약 마지막으로 본 숫자의 바로 다음이 표를 벗어나지 않고 검은색(0)이라면
                    if j+K < N-1 and arr[i][j+K] == 0:
                        count += 1
                    # 만약 마지막으로 본 숫자의 바로 다음이 표를 벗어나지 않고 검은색(0)이라면
                    elif j+K >= N :
                        count += 1
                    # 아닌경우에는 break 해준다.
                    else:
                        break

    # 세로 열 탐색
    for j in range(N-1):       # j = 0, 1, 2, 3, 4
        for i in range(N - K + 1):   # i = 0, 1, 2, 3, 4
            if arr[i][j] == 1:       # 만약 해당 값이 1이라면
                if arr[i-1][j] == 0 or i == 0:  # 확인하려는 원소의 위의 값이 검은색(0)이거나 i == 0이라면 탐색하겠다.
                    for k in range(K):          # 찾을 글자수만큼 돌아서
                        if arr[i+k][j] == 1:    # 만약 찾은 글자가 흰색이라면 넘기고
                            pass
                        else:                   # 검은색 이라면 멈춘다.
                            break
                    # 만약 마지막으로 본 숫자의 바로 다음이 표를 벗어나지 않고 검은색(0)이라면
                    if i+K < N-1 and arr[i+K][j] == 0:
                        count += 1
                    # 만약 마지막으로 본 숫자의 바로 다음이 표를 벗어나지 않고 검은색(0)이라면
                    elif i+K >= N :
                        count += 1
                    # 아닌경우에는 break 해준다.
                    else:
                        break

    print(f'#{test_case} {count}')









    # 만약 확인하려는 원소의 왼쪽 값이 0(검은색)이거나 확인하려는 원소의 j 인덱스가 0이면
    # 오른쪽으로 탐색을 한다.
    # 만약 K번째까지 원소의 값이 1이고 K+1의 값이 0이라면
    # count 에 1을 더해주겠다.

    # 만약 확인하려는 원소의 위쪽 값이 0(검은색)이거나 확인하려는 원소의 i의 인덱스가 0이라면
    # 아래로 탐색을 한다.
    # 만약 아래로 k번째까지 값이 1이고 K+1의 값이 검은색 0이라면
    # count 에 1을 더해주겠다.