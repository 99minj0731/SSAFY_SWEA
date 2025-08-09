import sys
sys.stdin = open('input.txt')

A = [list(map(int, input().split())) for _ in range(9)]

max_N = A[0][0]
result = [1, 1]

for i in range(9) :
    for j in range(9):
        if A[i][j] > max_N :
            max_N = A[i][j]
            result = [i + 1, j + 1]


print(max_N)
print(*result)
