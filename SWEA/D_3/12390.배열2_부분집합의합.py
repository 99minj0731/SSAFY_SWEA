import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #3

for tese_case in range(1, T + 1):
    # N = 부분집합 원소의 수 , K = 부분집합의 합
    N, K = map(int, input().split())
    arr = [i for i in range(1, N+1)]

    cnt = 0
    def subset(k, n, cur_sum):  # cur_sum: 현재까지 선택한 요소의 합
        if cur_sum > K:         # 만약 찾으려는 합보다 크다면 돌아간다.
            return

        if k == n:
            global cnt
            if cur_sum == K:  #부분집합의 합이 찾으려는 합과 동일할 경우
                cnt += 1
        else:
            subset(k + 1, n, cur_sum)
            subset(k + 1, n, cur_sum + arr[k])


    subset(0, N, 0);
    print(cnt)

'''  
    # N = 부분집합 원소의 수 , K = 부분집합의 합
    N, K = map(int, input().split())
    arr = []
    for i in range(1, N + 1):
        arr.append(i)
    #탐색 확인 용 리스트
    bits = [0] * N

    def subset(k, n, cur_sum):
        if k == n:
            S = 0
            for i in range(n):
                if bits[i]:  # 해당 자리를 봤다면
                    S += arr[i]
        else:
            bits[k] = 0
            subset(k+1, n, cur_sum)
            bits[k] = 1
            subset(k + 1, n, cur_sum + arr[k])
            
    subset(0, N, 0)
'''


