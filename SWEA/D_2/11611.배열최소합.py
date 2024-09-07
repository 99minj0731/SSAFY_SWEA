import sys
sys.stdin = open('input.txt', 'r')

# def min_num_n(num_arr):
#     sum_min_num = 0
#     min_num = arr[0][0]  #일단 0행 0번째라고 가정을 하고 갱신할거다.
#     for i in range(num_arr):
#         for j in range(num_arr):
#             if num_arr[i][j] < min_num:  #만약 min_num 보다 값이 작다면
#                 min_num = num_arr[i][j]  #해당 값으로 바꿔주겠다.

# T = int(input()) #3
#
# for test_case in range(1, T+1):
#     N = int(input()) #3
#     num_arr = [list(map(int, input().split()))for _ in range(N)]   #[[2, 1, 2], [5, 8, 5], [7, 2, 2]]
#     arr= list(range(N))
#     # result = min_num_n(arr)
#
#     print(arr)

T = int(input())


def find_minsum(i, n, cur_sum):
    global min_sum

    if cur_sum > min_sum:
        return

    if i == n:
        min_sum = cur_sum
    else:
        for j in range(n):
            if visited_col[j] == 0:
                visited_col[j] = 1
                find_minsum(i + 1, n, cur_sum + arr[i][j])
                visited_col[j] = 0


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited_col = [0] * N
    min_sum = float('inf')

    find_minsum(0, N, 0)
    print('#{} {}'.format(tc, min_sum))