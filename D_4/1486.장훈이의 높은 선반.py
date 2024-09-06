# import sys
# sys.stdin = open('input.txt')

# # count = 직원들의 수, sum_top = 지금까지 쌓은 탑
# def shelf(count, sum_top):
#     global min_top
#
#     # 기저조건
#     # 직원들이 모두 탑을 쌓았다면
#     if count == N:
#         return
#
#     # 가지치기
#     # 만약 지금까지 더한 값이 그 전의 더한 값보다 크다면
#     if sum_top >= min_top:
#         return
#
#     # 만약 지금까지 쌓은 탑이 선반의 높이 보다 같거나 높아진다면
#     if sum_top >= B:
#         if min_top >= sum_top:
#             min_top = sum_top
#             return

# # 부분집합 구하기 # i = 0 ~ 7까지 부분집합의 개수 = 2^N
# for i in range(1 << N):
#
#     for j in range(N):   # j = 0, 1, 2
#         if i & (1 << j) != 0:
#             sum_top += arr[j]
#             count += 1
#     shelf(count, sum_top)


T = int(input())

for test_case in range(1, T + 1):
    # N = 직원들의 수, B = 선반의 높이
    N, B = map(int, input().split())  # 3 6
    # 각 점원의 키
    arr = list(map(int, input().split()))  # [1, 3, 4]

    min_top = float('inf')

    # shelf(N, 0)

    # 부분집합 구하기 # i = 0 ~ 7까지 부분집합의 개수 = 2^N
    for i in range(1 << N):
        result = 0
        for j in range(N):  # j = 0, 1, 2
            if i & (1 << j) != 0:
                result += arr[j]
        # 만약 선반의 높이 이상이 됐다면
        if result >= B:
            if result < min_top:
                min_top = result

    result = min_top - B

    print(f'#{test_case} {result}')