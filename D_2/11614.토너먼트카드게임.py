import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  #3

for test_case in range(1, T+1):
    N = int(input())  #4
    arr = list(map(int, input().split()))  #[1, 3, 2, 1]

    print(arr)

