'''
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.

예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)

입력의 마지막엔 -1이 주어진다.

테스트케이스 마다 한줄에 하나씩 출력해야 한다.

n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

이때, 약수들은 오름차순으로 나열해야 한다.

n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

'''

import sys
sys.stdin = open('input.txt')

while True :
    N = int(input())
    if N == -1 : break
    
    # N의 약수를 구해보자
    N_list = []

    middle_N = N//2 
    for i in range(1, middle_N + 1):
        if N % i == 0 :
            N_list.append(i)

    # 리스트의 합을 구해보자
    total = 0
    for i in N_list:
        total += i
    
    if N == total :
        print(f"{N} = {' + '.join(map(str,N_list))}")
    else: 
        print(f'{N} is NOT perfect.')


