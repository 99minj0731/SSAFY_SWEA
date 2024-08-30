import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    # N = 4 (M을 2진수로 표현했을 때 마지막 N개의 값이 모두 1인지 확인하려고 있는 값) , M = 47 (이진수로 표현할 정수)

    for i in range(N):  # i = 0, 1, 2, 3
        result = M & (1 << i)
        if result == 0:
            print(f'#{test_case} OFF')
            break
    else:
        print(f'#{test_case} ON')

'''
result = M & (1 << i)
result   M = 101111


i = 1   1<<i = 1
 101111
&     1
 000001
 
i = 2   1<<i = 10
 101111
&    10
 000010

i = 3   1<<i = 100
 101111
&   100
 000100
 
i = 4   1<<i = 1000
 101111
&  1000
 001000
 
 => 탐색하는 이진수의 자리값이 모두 1이라면 0이 나오지 않음!
 
 
# 0 이 나오는 경우
 101110
&     1
 000000

 => 탐색하는 이진수의 자리값이 0 이 있다면 0이 나옴!


'''

