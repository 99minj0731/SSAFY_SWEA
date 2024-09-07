import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):

    # N = 정수의 개수, M = 구간의 개수
    N, M = map(int,input().split()) # N = 10, M = 3
    arr = list(map(int, input().split()))
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 최소 최대 가정
    min_val = float('inf')
    max_val = - float('inf')

    # 최소값 찾기
    for i in range(N - M + 1) :   # arr[7] = 8까지만 탐색
        min_sum = 0
        max_sum = 0

        # 구간합만큼 반복해서 더해줌 M = 0, 1, 2
        for j in range(M):
            min_sum += arr[i+j]
            max_sum += arr[i + j]

        # 최솟값 작은 값으로 교체
        if min_val > min_sum:
            min_val = min_sum
        # 최대값 큰 값으로 교체
        if max_val < max_sum:
            max_val = max_sum

    result = max_val - min_val

    print(f'#{test_case} {result}')

