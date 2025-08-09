import sys
sys.stdin = open('input.txt')

W = [list(input()) for _ in range(5)]

# 최소 1개부터 15개까지
result = []

# 가장 긴 줄 찾기
max_len = 0
for row in W :
    if len(row) > max_len : max_len = len(row)
# max_len = max(len(row) for row in W)

for col in range(max_len):
    for row in range(5):
        # 만약 가장 긴줄 범위 안에 들어있다면 결과에 추가
        if col < len(W[row]):
            result.append(W[row][col])

print(*result, sep="")