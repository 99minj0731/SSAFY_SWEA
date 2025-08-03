'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N, P = map(str,input().split())
    N = int(N)
    L = len(P) # 단어의 길이

    list = []

    for j in range(L):
        for i in range(N):
            list.append(P[j])

    print(*list, sep="")
