import sys
sys.stdin = open('input.txt')

# cnt = 이동한 횟수, lst = 이동하면서 7자리 만들기
def seven(row, col, cnt, lst):
    global arr, seven_number_zip

    # 종료 시점 : 7자리 숫자를 만들었을 때
    if cnt == 6:
        # 만약 숫자 모음집에 없다면 추가해준다. 있을 경우 다시 돌아감
        if lst not in seven_number_zip:
            seven_number_zip.add(lst)
        return

    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

    for r, c in delta:
        nr, nc = row + r, col + c
        # 격자판을 벗어나지 않는다면
        if 0 <= nr < 4 and 0 <= nc < 4:
            seven(nr, nc, cnt + 1, lst + str(arr[nr][nc]))
            # lst = lst[:-1] 얘는 필요없음 재귀 때 어차피 다시 리셋해줌


T = int(input()) #1

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    # set를 활용해서 중복 피하기
    seven_number_zip = set()

    # 격자판 16곳 모두 탐색
    for i in range(4):
        for j in range(4):
            seven(i, j, 0, str(arr[i][j]))

    ans = len(seven_number_zip)

    print(f'#{test_case} {ans}')
    # print(seven_number_zip)