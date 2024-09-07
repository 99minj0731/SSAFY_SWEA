import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #10

for test_case in range(1, T+1):
    N, M = map(int,input().split())        #3 5
    Ai = list(map(int, input().split()))   #1 5 3
    Bj = list(map(int, input().split()))   #3 6 -7 5 4

    max_sum = -float('inf')                    #일단 엄청 작은 값으로 지정을 한다.
    if N < M :
        for i in range(M-N+1):                 # 5-3+1=3이니까 i = 0, 1, 2 반복, 움직일 수 있는 횟수
            sum_num = 0                        # 일단 0으로 가정한다.
            for j in range(N):                 # Bj는 N의 길이만큼만 계산을 진행하겠다.  0, 1, 2
                sum_num += Ai[j] * Bj[j+i]
            if max_sum < sum_num:
                max_sum = sum_num

    else: # N > M 일 경우 반대로 해준다
        for i in range(N - M + 1):
            sum_num = 0
            for j in range(M):
                sum_num += Bj[j] * Ai[j + i]
            if max_sum < sum_num:
                max_sum = sum_num

    print(f'#{test_case} {max_sum}')







    # AI의 0번째와 BJ의 0번째의 값을 곱하고
    # AI의 1번째와 BJ의 1번째의 값을 곱하고
    # AI의 2번째와 BJ의 2번째의 값을 곱하고
    # Ai의 N -1 번째와 Bj의 N- 1 번째의 값까지 곱하고
    # 그 값을 모두 더해준다
    # 만약 그 값이 max_sum 보다 크다면
    # 그 값으로 바꿔준다.





