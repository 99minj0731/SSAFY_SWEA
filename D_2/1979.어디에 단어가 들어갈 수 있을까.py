import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #10

for i in range(1, T+1):
    N, K = map(int, input().split())   # N * N 으로 구성된, K=3
    arr = [list(map(int, input().split()))for _ in range(N)]

    count = 0
    for i in range(N-1):
        for j in range(N-1):
            if arr[i][j] == 1:  #해당 값이 1이고
                if arr[i][j-1] == 0 or j == 0:   # 확인하려는 원소의 왼쪽 값이 0이거나 j가 0이라면
                    for k in range(K):  # 찾을 글자수만큼 돌아서
                        if arr[i][j] == 1 #그 곳도 1이라면
                            pass
                        else:
                            break  #그렇지 않다면 break
                    if arr[i][j+N] == 0:
                        break
                    else:
                        count += 1








    # 만약 확인하려는 원소의 왼쪽 값이 0(검은색)이거나 확인하려는 원소의 j 인덱스가 0이면
    # 오른쪽으로 탐색을 한다.
    # 만약 K번째까지 원소의 값이 1이고 K+1의 값이 0이라면
    # count 에 1을 더해주겠다.

    # 만약 확인하려는 원소의 위쪽 값이 0(검은색)이거나 확인하려는 원소의 i의 인덱스가 0이라면
    # 아래로 탐색을 한다.
    # 만약 아래로 k번째까지 값이 같고 K+1의 값이 다르다면
    # count 에 1을 더해주겠다.