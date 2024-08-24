# 최소 값 구하기
arr = [9, 7, 13, 5, 7, 10, 2, 11]

min_val = arr[0]   # 0번째 인덱스의 값으로 최솟값 가정

for val in arr:
    if min_val > val:
        min_val = val
print(min_val)

for i in range(1, len(arr)): # i = 1, 2, 3, 4, 5, 6, 7
    if min_val > arr[i]:
        min_val = arr[i]
print(min_val)



# 최솟 값의 인덱스 구하기
min_idx = 0  # 0번째 인덱스로 가정

for i in range(len(arr)):  # i = 0, 1, 2, 3, 4, 5, 6, 7
    if arr[min_idx] > arr[i]:
        min_idx = i
print(min_idx, arr[min_idx])



# 최솟값이 여러개이고, 마지막 최솟값 인덱스 구하기
min_idx = 0

for i in range(len(arr)):  # i = 0, 1, 2, 3, 4, 5, 6, 7
    if arr[min_idx] >= arr[i]:  # 같음을 해줘야 뒤에도 탐색!
        min_idx = i
print(min_idx, arr[min_idx])



# 구간합의 최소, 최대 값 구하기
N = len(arr)    # N = 8
M = 3

min_val = float('inf')  #제일 큰 값으로 가정
max_val = - float('inf')  #제일 작은 값으로 가정

for s in range(N - M + 1):
    SUM = sum(arr[s:s + M])
    print(arr[s: s + M], SUM)

    if min_val > SUM:
        min_val = SUM
print(min_val)





