'''
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.

출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

import math
def prime_number(num):

    # 만약 1이라면 무조건 1력
    if num == 1: 
        return 1
    
    result = 0
    for i in range(num+1, 2 * num + 1): # 2, 3, 4까지 탐색
        if is_prime(i):
            result += 1
    
    return result
            
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 :
            return False
    return True

is_zero = True

while is_zero:
    N = int(input())

    if N == 0 :
        is_zero = False
        break

    print(prime_number(N))
