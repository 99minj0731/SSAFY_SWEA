'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

주어진 수들 중 소수의 개수를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))

# 소수를 판별해주는 함수 
def is_prime(num):
    # 만약 1이라며는 소수가 아니다.
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1): # 2, 
        if num % i == 0:
            return False
    return True

count = 0
for num in numbers:
    if is_prime(num):
        count += 1

print(count)