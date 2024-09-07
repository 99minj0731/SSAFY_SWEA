def work(row, sum_v):
    global visited, ans

    # 가지치기
    # 만약 지금까지 한 게 앞에 값보다 작다면 그 뒤부터는 볼 필요 없음
    if sum_v <= ans:
        return

    # 성공할 확률 갱신
    if row == N:
        if sum_v >= ans:
            ans = sum_v
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            work(row + 1, sum_v * (arr[row][i] * 0.01))
            visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  # 3
    arr = [list(map(int, input().split())) for _ in range(N)]

    # col을 방문했는지 안했는지 확인
    visited = [0] * N
    ans = -99999

    work(0, 1)

    result = ans * 100

    print(f'#{test_case} {result:.6f}')