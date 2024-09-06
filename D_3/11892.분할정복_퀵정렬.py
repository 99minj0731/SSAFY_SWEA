import sys
sys.stdin = open('input.txt')

# 퀵정렬 _ lomuto_partition

def lumuto_partition(left, right):

    # 피봇값을 오른쪽으로 가정한다.
    p = arr[right]

    i = left - 1      # [2, 2, 1, 1, 3]
    for j in range(left, right): # 0, 1, 2, 3
        # 만약 피봇의 값보다 작다면
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

def quick_sort(left, right):
    # 만약 오른쪽 인덱스가 더 크다면
    if left < right:

        # 피봇의 값은 계속 바뀔거임
        p = lumuto_partition(left, right)
        quick_sort(left, p-1) # 왼쪽 자리를 바꿈
        quick_sort(p+1, right) # 오른쪽 자리를 바꿈

T = int(input())

for test_case in range(1,  T + 1):
    N = int(input())
    arr = list(map(int, input().split()))  # [2, 2, 1, 1, 3]

    quick_sort(0, N -1)  # 0, 4

    print(f'#{test_case} {arr[N//2]}')