import sys
sys.stdin = open("input.txt", "r")

T = int(input()) #3

for test_case in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(2)]

    str_1 = arr[0][0]    #첫번째 줄  XYPV
    str_2 = arr[1][0]    #두번째 줄  EOGGXYPVSY

    # print(str_1)   #XYPV
    # print(len(str_1))  #4
    # print(str_1[0])  # X

    result = 0
    for i in range(len(str_1)):
        # max_idx = str_1[i]
        count = 0
        for j in range(len(str_2)):
            if str_1[i] == str_2[j]:
                count += 1
        if count > result:
            result = count

    print(f'#{test_case} {result}')


