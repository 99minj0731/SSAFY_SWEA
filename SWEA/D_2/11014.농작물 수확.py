import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  #3

for test_case in range(1, T+1):
    N = int(input())    # N * N, N = 5
    arr = [list(map(int, input().split()))for _ in range(N)]

    # 최대 최소값의 차이를 가장 큰 값으로 가정
    min_max_D = float('inf')

    # 기준선
    for i in range(1, N-1):  #기준 가로선
        for j in range(1, N-1):  #기준 세로선

            # 첫 번째 영역 / 가로선 기준 위쪽, 세로선 기준 위쪽
            sum_1 = 0
            for k in range(0, i):
                for l in range(0, j):
                    sum_1 += arr[k][l]

            # 두 번째 영역 / 가로선 기준 아래쪽, 세로선 기준 왼쪽
            sum_2 = 0
            for k in range(i, N):
                for l in range(0, j):
                    sum_2 += arr[k][l]

            # 세 번째 영역 / 가로선 기준 없음, 세로선 기준 오른쪽
            sum_3 = 0
            for k in range(0, N):
                for l in range(j, N):
                    sum_3 += arr[k][l]

            # 차이가 가장 적을 때 차이가 얼마나 나는지 출력하기
            result = max(sum_1, sum_2, sum_3) - min(sum_1, sum_2, sum_3)
            if result < min_max_D:
                min_max_D = result

    print(f'#{test_case} {min_max_D}')

