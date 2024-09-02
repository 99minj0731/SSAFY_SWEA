import sys
sys.stdin = open('input.txt')

def cart(v, count, sum_num):
    global min_number

    # 만약 현재 최솟값보다 크다면 더 이상 탐색하지 않겠다.
    if sum_num > min_number:
        return

    # count가 0부터 시작했으니까 N-1이랑 같다면 다 방문한거다.
    if count == N - 1:
        if min_number > sum_num + arr[v][0]:
            min_number = sum_num + arr[v][0]

    else:
        for i in range(1, N): #i=1, 2
            if v == i:
                continue
            if visited[i] == 0:
                visited[i] = 1
                cart(i, count + 1, sum_num + arr[v][i])
                visited[i] = 0

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    visited = [0] * N

    min_number = 9999999999

    cart(0, 0, 0)

    print(f'#{test_case} {min_number}')