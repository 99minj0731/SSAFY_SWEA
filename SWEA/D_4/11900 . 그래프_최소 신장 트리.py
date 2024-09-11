import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    for _ in range(E):
        s, e, weight = map(int, input().split())

    # dfs()
    print(f'#{weight}')