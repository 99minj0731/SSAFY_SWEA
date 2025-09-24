'''
골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

입력
첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

출력
각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

import math
N = int(input())
MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 소수인지 판별
for i in range(2, int(math.sqrt(MAX)) + 1): # 2, 3, 4, 5 ...
    # 만약 소수인지 확인을 하지 않은 숫자라면 확인
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
                is_prime[j] = False

for _ in range(N):
    num = int(input())
    cnt = 0
    for i in range(2, (num // 2) + 1) :
        if is_prime[num - i] and is_prime[i]: # 만약 소수라면 
            cnt += 1
        
    print(cnt)