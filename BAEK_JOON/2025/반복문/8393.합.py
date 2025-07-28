import sys
sys.stdin = open('input.txt')

N = int(input())

result = 0

for i in range(1, N + 1):
    result = result + i

print(result)