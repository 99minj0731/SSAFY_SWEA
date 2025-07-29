import sys
sys.stdin = open('input.txt')

input = int(input())

N = input // 4 # 총 나와야 하는 개수 
letter = 'long '
print(letter * N + 'int')