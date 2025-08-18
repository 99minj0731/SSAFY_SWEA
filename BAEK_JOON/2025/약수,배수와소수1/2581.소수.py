'''
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
'''
import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())

prime_list = []

for i in range(M, N + 1): # 1, 2

    if M == 1 and N == 1 :
        break

    # i중에서 소수를 찾아보자
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0 : 
            is_prime = False
            break
    
    if is_prime == True:
        prime_list.append(i)

if len(prime_list) >= 1:
    # 만약 1이 들어있다면 없애자
    if 1 in prime_list:
        prime_list.remove(1)

    A = sum(prime_list)
    B = min(prime_list)
    print(A)
    print(B)
else : print("-1")