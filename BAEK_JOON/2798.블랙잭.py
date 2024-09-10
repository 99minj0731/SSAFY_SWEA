import sys
sys.stdin = open('input.txt')

def dfs(cur_sum, cnt):
    global result, visited

    # 종료조건: 3장을 다 골랐다.
    if cnt == 3:
        if result < cur_sum <= M:
            result = cur_sum
        return

    # 가지치기
    if cur_sum >= M:
        return

    for i in range(N):  # i=0,1,2,3,4
        if visited[i] == 0:
            visited[i] = 1
            dfs(cur_sum+arr[i], cnt+1)
            visited[i] = 0

T = int(input())

for test_case in range(1, T + 1):
    # N = 카드의 개수, M = 만들 수
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    #[5, 6, 7, 8, 9]

    result = 0
    visited = [0] * N

    dfs(0, 0)
    print(result)