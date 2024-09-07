import sys
sys.stdin = open("input.txt", "r")

A, B = map(int, input().split())  # 3, 2

#A가 이기는 경우
if A == int('2') and B == int('1'):
    print(f'A')
if A == int('3') and B == int('2'):
    print(f'A')
if A == int('1') and B == int('3'):
    print(f'A')

#B가 이기는 경우
if B == int('2') and A == int('1'):
    print(f'B')
if B == int('3') and A == int('2'):
    print(f'B')
if B == int('1') and A == int('3'):
    print(f'B')



