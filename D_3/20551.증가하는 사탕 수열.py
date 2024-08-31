import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    cnt = 0

    flag = True

    while arr[0] >= arr [1]:
        arr[0] -= 1
        cnt += 1
        if arr[0] == 0 or arr[1] == 0:
            flag = False
            break

    while arr[1] >= arr[2]:
        arr[1] -= 1
        cnt += 1
        if arr[0] == 0 or arr[1] == 0:
            flag = False
            break
        if arr[1] == arr[0]:
            arr[0] -= 1
            cnt += 1

    if flag == False:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {cnt}')