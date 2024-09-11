import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N번까지의 최소 거리, E = 도로의개수(간선의 개수)
    N, E = map(int, input().split()) # 2, 3

    G = [[] for _ in range(N + 1)]
    # [[], [], []] --> [[(1, 1), (2, 6)], [(2, 1)], []]
    # 해당 자리값(인덱스) 에서 (갈수있는곳, 거리) 저장

    for _ in range(E):
        # s: 시작, e: 도착, weight: 거리
        s, e, weight = map(int, input().split())   # 0, 1, 1

        G[s].append((e, weight))

    D = [1e9] * (N+1)
    D[0] = 0
    Q = [0]

    while Q:
        # 0부터 시작
        s = Q.pop(0)

        # 인접 정점을 찾아서, 간선완화 작업 수행
        for e, weight in G[s]:  # (1, 1), (2, 6)
            if D[e] > D[s] + weight:
                D[e] = D[s] + weight
                Q.append(e)

    print(f'#{test_case} {D[N]}')











