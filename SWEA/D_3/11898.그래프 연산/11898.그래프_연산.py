import sys
sys.stdin = open('../input.txt')

from collections import deque
def bfs(n):  # n = 처음 숫자
    Q = deque([(n, 0)])

    visited = [0] * 1000001
    visited[n] = 1

    while Q != 0:
        cur, cnt = Q.popleft()

        # 만약 목표 숫자에 도달한다면 연산 횟수 반환
        if cur == M:
            return cnt

        # 네가지 연산 하기
        for number in [cur+1, cur-1, cur*2, cur-10]:
            # 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
            if 1 <= number <= 1000000:
                if visited[number] == 0:
                    visited[number] = 1
                    Q.append((number, cnt + 1))

T = int(input())

for test_case in range(1, T + 1):
    # N = 시작 숫자, M = 만들숫자
    N, M = map(int,input().split())

    result = bfs(N)

    print(f'#{test_case} {result}')




