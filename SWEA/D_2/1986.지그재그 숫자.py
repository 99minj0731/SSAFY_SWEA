import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #2

for test_case in range(1, T+1):
    N = int(input()) # 5

    result = 0                #일단 0이라고 가정하고

    for i in range(1, N+1):   # 0번째는 무시할꺼고 1번째부터 N까지 반복
        if i % 2 == 1:        # i의 값이 홀수면 더하고
            result += i
        else:                 # 짝수면 뺄거다.
            result -= i

    print(f'#{test_case} {result}')