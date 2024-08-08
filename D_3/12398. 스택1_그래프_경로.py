import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #3

for test_case in range(1, T+1):
    V, E = map(int, input().split())  # V=노드의 갯수 6개, E=간선의 갯수 5개
    G = [[] for _ in range(V+1)]   #빈 리스트를 만들고   ???????????

    for _ in range(E):
        u, v = map(int, input().split())  # u=시작점 v =방문하지않음
        G[u].append(v)    #시작점이랑 연결된거를 리스트로 정리를 해

    v, goal = map(int, input().split())   #v는 시작점, goal은 찾아야하는거  ????????????

    S = []          #빈 스택을 만들구
    visited = [0] * (V + 1)  #방문했는지 확인해야하니까 빈 리스트 만들어
    visited[v] = 1  #방문하지 않은게 곧 시작 정점이 될거니까 방문한 거는 1을 만들어 ????????

    while True:
        for w in G[v]:            #방문하지 않은 것들 중에     ??????????
            if not visited[w]:    #??????
                S.append(v)       #스택에다가 넣고
                visited[w] = 1    #얘는 방문할거니까 1을 만들어
                v = w             #w를 v다가 넣고
                break
        else:                      #브레이크가 안걸리고 계속 갔어
            if not S:  #S리스트 안ㅇㅔ 아무것도 없다.
                break
            v = S.pop()

    print(f'#{test_case} {visited[goal]}')
