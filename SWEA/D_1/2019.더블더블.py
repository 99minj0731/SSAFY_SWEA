import sys
sys.stdin = open("input.txt", "r")

T = int(input())   #8

arr = []
j = 1
for i in range(T):
    arr.append(j)
    j = j*2

print(*arr)