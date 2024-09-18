import sys
sys.stdin = open('input.txt')

def cal(a, b, count):

    # 종료조건 : 만약 a나 b가 N을 초과했을 경우
    if a > N:
        print(f'{count}')
        return
    if b > N:
        print(f'{count}')
        return

    # a와 b중에 큰 값을 더해준다.
    A = max(a, b)
    B = min(a, b)

    cal(A, B+A, count + 1)

T = int(input())

for test_cast in range(1, T + 1):
    A, B, N = map(int, input().split())

    cal(max(A, B),min(A, B), 0)

'''
def cal(count, cur_sum):
    global result
    # 종료 조건: 만약 cur_sum이 현재 result 보다 크다면 종료
    if cur_sum > N:
        result = count
        return

    # 목표수를 초과할 때까지 계산하기 ( A에다가 B를 더함)
    cal(count + 1, cur_sum + B)

def cal2(count, cur_sum):
    global result2
    # 종료 조건: 만약 cur_sum이 현재 result 보다 크다면 종료
    if cur_sum > N:
        result2 = count
        return

    # 목표수를 초과할 때까지 계산하기 ( A에다가 B를 더함)
    cal2(count + 1, cur_sum + A)

T = int(input())

for test_case in range(1, T + 1):
    A, B, N = map(int,input().split())  #1 2 5

    result = 1e9
    result2 = 1e9

    cal(0, A)
    cal2(0, B)
    ans = min(result, result2)

    print(f'#{test_case} {ans}')
'''