import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):  #총 10개의 테케 주어진다.

    #옮기는 횟수
    dump = int(input())

    arr = list(map(int, input().split()))

    for _ in range(dump): # i = 0 ~ 833

        max_num = - float('inf')
        max_idx = 0
        min_num = float('inf')
        min_idx = 0

        #최대, 최솟값 구하기
        for i in range(100):
            if max_num < arr[i]:
                max_num = arr[i]
                max_idx = i
            if min_num > arr[i]:
                min_num = arr[i]
                min_idx = i

        # 덤프 실행하기
        arr[max_idx] -= 1
        arr[min_idx] += 1

    # 최종적인 격차 출력하기
    result_min = float('inf')
    result_max = -float('inf')

    for i in range(100):
        if result_min > arr[i]:
            result_min = arr[i]
        if result_max < arr[i]:
            result_max = arr[i]

    result = result_max - result_min

    print(f'#{test_case} {result}')






