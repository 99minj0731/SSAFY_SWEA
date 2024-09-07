import sys
sys.stdin = open("input.txt", "r")

T = int(input()) #10

num_sum = 0

for i in range(1, T + 1):
    num_sum += i

print(num_sum)
