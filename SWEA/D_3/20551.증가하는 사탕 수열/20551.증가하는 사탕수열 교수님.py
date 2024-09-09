import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    A, B, C =  map(int, input().split())

    # 안된는 경우
    if B < 2 or C < 3:
        print(f'#{test_case} -1')
        continue

    # 먹은 사탕 개수
    eat = 0

    if B >= C:
        B = C -1
        eat += B - (C - 1)

    if A >= B:
        A = B - 1
        eat += A - (B - 1)

    print(f'#{test_case} {eat}')