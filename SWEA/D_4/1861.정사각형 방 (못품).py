import sys; sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 2
    arr = [list(map(int, input().split()))for _ in range(N)] #[[1, 2], [3, 4]]

    visited = [0] * (N*N+1)  #[0, 0, 0, 0, 0] -> [0, 1, 0, 1, 0]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

    for i in range(N):
        for j in range(N):
            for r, c in delta:
                nr, nc = i + r, j + c
                # 배열 안에 있는지 확인 & 자신보다 1이 크다면
                if 0 <= nr < N and 0 <= nc < N and arr[i][j]+1 == arr[nr][nc]:
                    visited[arr[i][j]] = 1
                    # 숫자가 중복되지 않으니 확인 즉시 break
                    break

    result = 0
    count = 0
    start = 0

    for i in range(N*N, -1, -1): # i= 4, 3, 2, 1, 0 / 0까지 봐야 1의 자리가 1인지 아닌지 확인가능
        if visited[i] == 1:
            count += 1
        else:
            # 앞에 만약에 똑같이 최대로 갈 수 있는 값이 있다면 그 값으로 수정해야하니 같거나 클경우여야함.
            if count >= result:
                result = count
                start = i + 1
            count = 0

    # print(visited)  [0, 0, 0, 1, 1, 0, 1, 1, 0, 0] [0, 1, 0, 1, 0]
    print(f'#{test_case} {start} {result + 1}')



'''
# 해당 자리 값을 어떻게 출력해야 할지 모르겠다ㅏ

def room(row, col):

    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] #상우하좌

    # 이미 본 곳이라면 그 자리값을 반환한다.
    if dp[row][col] != 0:
        return dp[row][col]

    max_move = 1

    for r, c in delta:
        nr, nc = row + r, col + c
        # 배열 안에 있고 현재 값보다 1만큼 크다면
        if 0 <= nr < N and 0 <= nc < N and arr[row][col] + 1 == arr[nr][nc]:
            max_move = max(max_move, room(nr, nc) + 1)

    dp[row][col] = max_move
    return dp[row][col]



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * N for _ in range(N)]

    # 일단 0 이라고 가정 계속 갱신될거임
    max_count = 0
    result_room = arr[0][0]

    # 모든 곳 탐색
    
    for i in range(N):
        for j in range(N):
            max_count = max(max_count, room(i, j))
            result_room = arr[i][j]


    print(f'#{test_case} {result_room} {max_count}')

'''

