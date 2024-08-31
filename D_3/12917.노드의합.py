import sys
sys.stdin = open('input.txt')

'''
T = int(input())

for test_case in range(1, T + 1):

    #노드의 개수 N과 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())  #5 3 2

    tree = [0] * (N + 1)

    for _ in range(M):
        idx, num = map(int, input().split())
        # 해당 자리에 해당 값을 일단 넣음
        tree[idx] = num
    # print(tree)  # [0, 0, 0, 3, 1, 2]

         # 자식들의 합으로 부모노드 값 채우기
    for i in range(N - M, 0, -1): # i = 2, 1
        # 오른쪽 자식이 없을 경우가 있으니 왼쪽 값만 먼저 더해줌
        tree[i] = tree[i*2]
        # 만약 오른쪽 자식이 있을 경우 이 값도 더해줌
        if i*2+1 <= N:
            tree[i] += tree[i*2+1]

    ans = tree[L]
    print(f'#{test_case} {ans}')
'''

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val

    def dfs(v):
        if v > N: return 0
        l = dfs(v * 2)
        r = dfs(v * 2 + 1)
        tree[v] += l + r
        return tree[v]
    dfs(1)
    print(f'#{tc} {tree[L]}')


