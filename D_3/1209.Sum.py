import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):  #tc 총 10개 줄거다.
    test_case = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]

    # 행의 합 구하기
    max_c_result = 0
    for i in range(100):
        max_c = 0
        for j in range(100):
            max_c += arr[i][j]
        if max_c_result < max_c:
            max_c_result = max_c

    # 열의 합 구하기
    max_r_result = 0
    for i in range(100):
        max_r = 0
        for j in range(100):
            max_r += arr[j][i]
        if max_r_result < max_r:
            max_r_result = max_r

    # 왼쪽 아래로 내려가는 대각선의 합 구하기
    max_left_result = 0
    for i in range(100):
        max_left_result += arr[i][99-i]

    # 오른쪽 아래로 내려가는 대각선의 합 구하기
    max_right_result = 0
    for i in range(100):
        max_right_result += arr[i][i]

    # print(max_c_result, max_r_result, max_left_result,  max_right_result)

    # 4개의 값 중 제일 큰 값을 줄력
    result = 0

    lst = [max_c_result, max_r_result, max_left_result, max_right_result]
    for i in range(4):
        if lst[i] > result:
            result = lst[i]

    print(f'#{test_case} {result}')


