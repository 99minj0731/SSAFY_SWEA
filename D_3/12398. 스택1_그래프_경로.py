import sys
sys.stdin = open('input.txt', 'r')

def DFS(S, V):             #S시작점 = 1, V= 노드 갯수 6개
    visited = [0] * (V+1)   #방문한 정점을 1로 표시 [0, 0, 0, 0, 0, 0, 0]   #왜 +1을 할까?????????????????
    stack = []              #빈 스택을 만들어 줬어
    visited[S] = 1          #다녀간 적 있으면 1로 바꿔
    vv = S                  #vv에다가 시작점을 넣어
    while True:
        for w in adjL[vv]:         #vv에 인접하고
            if visited[w] == 0:   #방문안한 w가 있다면
                stack.append(vv)  #현재 노드를 넣고
                vv = w            #w를 이제 볼거다
                visited[w] = 1    #그러고 방문했으니까 1로 만들어줘
                break             #이제 다시 반복을 할거다.
        else:                     #주변에 방문하지 않은 노드들이 없어서 break가 걸리지 않은 경우
            if stack:             #이전으로 돌아가 if top > -1 그니까 top에 뭐가 있는거지
                vv = stack.pop()   #top에 있는걸 꺼내
            else:                 #갈 곳이 없다
                break             #while True

T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())   # V = 노드 갯수 6개, E = 간선 갯수 5개
    adjL = [[]for _ in range(V+1)]
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())   # S = 노드 시작점 1, G = 찾아갈 곳 6
    # for i in range(E):

    DFS(S, G)