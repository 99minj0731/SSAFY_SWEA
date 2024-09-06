import sys
sys.stdin = open('input.txt')

def value (sum_k, sum_c, k):  # sum_k = 부피 합계, sum_c = 물건의 가치 합계, k = 넘으면 안되는 부피
    global max_V

    # 가지치기 : 만약 지금까지 합한 부피가 k를 넘는다면 돌아간다.
    if sum_k > k:
        return

    # 만약 최대 부피를 넘지 않았다면 값 비교해서 갱신한다.
    if sum_k <= k:
        if sum_c >= max_V:
            max_V = sum_c

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            value(sum_k + V[i], sum_c + C[i], k)
            visited[i] = 0


T = int(input())

for test_case in range(1, T + 1):
    # N = 물건 개수, K = 가방최대 부피
    N, K = map(int, input().split())   # 4 5

    # V = 물건의 부피, C = 물건의 가치
    V = [] * N   #[1, 3, 4, 2]
    C = [] * N   #[2, 2, 4, 3]

    arr = [list(map(int, input().split())) for _ in range(N)] #[[1, 2], [3, 2], [4, 4], [2, 3]]
    for i in range(N):
        V.append(arr[i][0])
        C.append(arr[i][1])

    # 최대 가치를 0이라고 가정
    max_V = 0
    # 방문했는지 확인
    visited = [0] * N

    value(0, 0, K)

    print(f'#{test_case} {max_V}')