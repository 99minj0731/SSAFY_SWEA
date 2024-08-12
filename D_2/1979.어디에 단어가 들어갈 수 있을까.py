import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #10

for i in range(1, T+1):
    N, k = map(int, (input()))   # N =