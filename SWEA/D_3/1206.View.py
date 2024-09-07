import sys
sys.stdin = open('../D_2/input.txt', 'r')

T = 10

for test_case in range(1, T+1):
    N = int(input())  # 건물의 갯수
    arr = list(map(int, input().split()))

    view = 0  # 조망이 모두 확보된 가구 수

    for i in range(2, N-2): # 앞뒤 각각 2개의 값은 0 이니까 2부터 N-3까지 돌겠다.
        right_view = 0
        left_view = 0
        #좌우 두 개 건물의 높이가 해당 건물보다 낮을 경우만 계산한다.
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            # 해당 건물 높이에서 좌우 두 개의 건물 중 더 높은 값을 빼준다.
            if arr[i-1] >= arr[i-2]:
                left_view = arr[i] - arr[i-1]
            elif arr[i-1] < arr[i-2]:
                left_view = arr[i] - arr[i-2]

            if arr[i+1] >= arr[i+2]:
                right_view = arr[i] - arr[i+1]
            elif arr[i+1] < arr[i+2]:
                right_view = arr[i] - arr[i+2]

        if right_view >= left_view:
            view += left_view
        elif right_view < left_view:
            view += right_view
        # else:
        #     break
    print(f'#{test_case} {view}')


