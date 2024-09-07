import sys
sys.stdin = open("input.txt", "r")

T = int(input())

arr = []

for i in range(1, T+1):
    if T % i == 0:
        arr.append(i)

print(*arr)