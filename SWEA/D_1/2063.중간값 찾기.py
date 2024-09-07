T = int(input())  # 199
arr = list(map(int, input().split()))
# 정렬
for i in range(T):  # 총 199번 반복을 해서
    min_idx = i  # 일단 가장 작은 수를 0번째라고 가정하고 시작
    for j in range(i + 1, T):  # 해당 i 뒤에 번호부터 끝까지 반복
        if arr[min_idx] > arr[j]:  # 만약 해당 값이 더 작다면
            min_idx = j  # min_idx를 j번째로 바꾸고
    arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 둘의 위치를 바꾼다

result = arr[T // 2]  # 가운데 값을 찾는다
print(result)