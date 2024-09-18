import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N:가야할 곳, E:도로의 수
    N, E = map(int, input().split()) # 2, 3

    G = [[]for _ in range(N+1)]
    # [[(1, 1), (2, 1)], [(2, 6)]. []]

    # 도로의 정보
    for _ in range(E):
        # s=시작, e=끝, w=거리
        s, e, w = map(int,input().split())

        G[s].append((e, w))

    D = [1e9] * (N+1)
    D[0] = 0

    # 방문할 노드 저장
    Q = [0]

    while Q:
        s = Q.pop(0)

        for e, w in G[s]:
            if D[e] > D[s] + w:
                D[e] = D[s] + w
                Q.append(e)

    print(f'#{test_case} {D[N]}')







