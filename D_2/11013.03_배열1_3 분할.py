import sys
sys.stdin = open('input.txt', 'r')



T = int(input()) #3

for test_case in range(1, T + 1):
    N = int(input()) #5
    arr = list(map(int, input().split()))  #[2, 6, 8, 5, -8]

    result = float('inf')

    # 3분할 하기
    for i in range(0, N - 2):  # i = 0, 1, 2
        for j in range(i + 1, N - 1): # j = 1, 2, 3
            # 각 구간의 합 구하기
            sum_1 = sum(arr[:i + 1])  # 0, 1, 2
            sum_2 = sum(arr[i + 1 : j + 1]) # 1, 2, 3
            sum_3 = sum(arr[j + 1 :]) # 2, 3, 4

            max_num = max(sum_1, sum_2, sum_3)
            min_num = min(sum_1, sum_2, sum_3)

            D_num = max_num - min_num
            if result > D_num:
                result = D_num

    print(f'#{test_case} {result}')





