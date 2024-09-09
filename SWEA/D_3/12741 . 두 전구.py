import sys
sys.stdin = open('input.txt')

T = int(input())
result_list = []

for test_case in range(1,  T + 1):
    A, B, C, D = map(int, input().split())

    start = max(A, C)
    end = min(B, D)

    result = end - start

    if result <= 0:
        result = 0

    result_list.append(result)

for index, result in enumerate(result_list):
    print(f'#{index + 1} {result}')
