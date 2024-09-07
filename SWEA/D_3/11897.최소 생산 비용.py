# import sys
# sys.stdin = open('input.txt')

def factory(row, sum_num):
    global result, visited

    # 종료조건 : 만약 행을 마지막까지 확인했다.
    if row == N:
        # 비교를 한다.
        if sum_num < result:
            result = sum_num
            return

    # 가지치기 : 지금까지 확인한게 원래 result 값보다 크다면 그 뒤로부터는 볼 필요 없습니다.
    if sum_num >= result:
        return

    # 행만큼 반복해서 확인하겠다.
    for i in range(N):
        # 만약 방문하지 않은 곳이라면
        if visited[i] == 0:
            # 방문했다고 표시하고
            visited[i] = 1
            # 행을 한 칸 가고, 현재 값을 더해준다.
            factory(row + 1, sum_num + arr[row][i])
            # 돌아왔으면 다시 0으로 만들어준다.
            visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, (input().split()))) for _ in range(N)]

    # 일단 제일 큰 값으로 정한다.
    result = float('inf')
    # 방문한 행을 확인하겠다.
    visited = [0] * N

    factory(0, 0)

    print(f'#{test_case} {result}')