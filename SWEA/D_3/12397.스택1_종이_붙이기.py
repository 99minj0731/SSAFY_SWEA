import sys
sys.stdin = open('input.txt', 'r')

#DP
# def fibo(n):  #만약 30이 들어왔다면
#     f = [0] * (n//10 + 1)   #f = [0, 0, 0, 0]
#     f[0] = 0
#     f[1] = 1
#     f[2] = 3  #여기까지는 수식에 안맞으니까
#     for i in range(3, n//10 +1):  #f[2]의 값은 수식에 안맞고 위에 해놨으니까 3부터 시작
#         f[i] = f[i-1] + f[i-2] * 2  #전의 값 + 전전의 값*2 = 현재 값
#     return f[n//10]
#
# T = int(input()) #3
#
# for test_case in range(1, T+1):
#     n = int(input())  # 10의 배수가 입력될거다
#     print(f'#{test_case} {fibo(n)}')


#메모제이션
def fibo(n):
    global memo
    if 2 < n and memo[n] == 0:  #n이 3 이상이고 메모의 그 위치값이 0이라면
        memo[n] = fibo(n-1) + fibo(n-2) * 2
    return memo[n]


T = int(input()) #3

for test_case in range(1, T+1):
    n = int(input()) // 10
    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 3
    print(f'#{test_case} {fibo(n)}')