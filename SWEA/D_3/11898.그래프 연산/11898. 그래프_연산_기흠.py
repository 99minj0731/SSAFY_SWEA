import sys
sys.stdin = open('../input.txt')

from collections import deque

def bfs(n):
    q = deque()
    q.append((n, 0))
    visited = [0] * 100001
    visited[n] = 1

    while q != 0:
        v, cnt = q.popleft()
        if v == M:
            return cnt
        else:
            for k in range(4):
                if k == 0:
                    if v + 1 <= 1000000 and visited[v+1] == 0:
                        q.append((v + 1, cnt + 1))
                        visited[v+1] = 1
                elif k == 1:
                    if v - 1 <= 1000000 and visited[v-1] == 0:
                        q.append((v - 1, cnt + 1))
                        visited[v-1] = 1
                elif k == 2:
                    if v * 2 <= 1000000 and visited[v*2] == 0:
                        q.append((v*2, cnt + 1))
                        visited[v * 2] = 1
                else:
                    if v - 10 <= 1000000 and visited[v - 10] == 0:
                        q.append((v - 10, cnt + 1))
                        visited[v-10] = 1

T = int(input())

for test_case in range(1, T + 1):
    # N에다가 연산시작, M = 만들어야하는 수
    N, M = map(int, input().split())  # 2 7
    result = bfs(N)

    print(f'#{test_case} {result}')


'''
def make_M(n, cur_N, count): # cur_N: 연산된 숫자, count = 몇 번 계산했는지
    global cnt

    # 종료조건
    # 해당 M값을 만들었으면 계산 횟수를 비교한다.
    if cur_N == M:
        if count < cnt:
            cnt = count
        return

    # 만약 계산 횟수가 현재 찾아놓은 최소 계산 횟수보다 크다면
    if count >= cnt:
        return

    # 계산하기
    cur_N = (n - 1)
'''