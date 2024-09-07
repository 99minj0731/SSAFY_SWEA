import sys
sys.stdin = open('input.txt')

def merge_sort(m):

    #만약 1개만 남았다면 그 값을 출력
    if len(m) == 1:
        return m

    #반으로 나눈 후, mid기준 앞쪽은 left에 뒤쪽은 right에 널음
    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    #계속 나눠서 정렬
    left = merge_sort(left) #:2
    right = merge_sort(right) # 2:

    # 젤 먼저 앞 두자리가 return 받음
    return merge(left, right)


# 왼쪽 오른쪽 비교하면서 작은 수부터 정렬하기

def merge(left, right):
    result = [0] * ((len(left)+(len(right))))
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    #left와 right의 인덱스를 지정
    l = 0
    r = 0

    #끝까지 비교할 때까지 반복
    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] =right[r]
            r += 1

    # 남은 것들 넣어주기
    while l < len(left):
        result[l+r] = left[l]
        l += 1
    while r < len(right):
        result[l+r] = right[r]
        r += 1

    return result


T = int(input())

for test_case in range(1,  T + 1):
    N = int(input())  #5
    arr = list(map(int, input().split()))  #[2, 2, 1, 1, 3]

    cnt = 0
    arr = merge_sort(arr)
    ans = arr[N//2]

    print(f'#{test_case} {ans} {cnt}')