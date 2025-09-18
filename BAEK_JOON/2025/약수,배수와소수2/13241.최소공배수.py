'''
최소공배수 구하기
'''

import sys
sys.stdin = open('input.txt')

def gdc(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
result = gdc(A, B)
print(A * B // result)

