import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split()))for _ in range(9)]

    result = True

    # 가로 줄 검사
    for i in range(9):
        num_list = []
        for j in range(9):
            if arr[i][j] not in num_list:     # 만약 리스트 안에 없다면
                num_list.append(arr[i][j])    # 해당 값을 리스트 안에 넣는다.
            else:
                result = False

    #세로 줄 검사
    for i in range(9):
        num_list = []
        for j in range(9):
            if arr[j][i] not in num_list:
                num_list.append(arr[j][i])
            else:
                result = False


    # 왼쪽 세 칸 검사
    for i in range(0, 7, 3):
        num_list = []
        for j in range(3):
            for k in range(3):
                if arr[i+j][k] not in num_list:
                    num_list.append(arr[i+j][k])
                else:
                    result = False

    # 가운데 세 칸 검사
    for i in range(0, 7, 3):
        num_list = []
        for j in range(3):
            for k in range(3, 6):
                if arr[i + j][k] not in num_list:
                    num_list.append(arr[i + j][k])
                else:
                    result = False

    # 오른쪽 세 칸 검사
    for i in range(0, 7, 3):
        num_list = []
        for j in range(3):
            for k in range(6, 9):
                if arr[i + j][k] not in num_list:
                    num_list.append(arr[i + j][k])
                else:
                    result = False

    if result == True :
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')





