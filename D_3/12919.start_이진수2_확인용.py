import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    number = float(input())   # 0.125


    # 계속 2를 곱해서 1 이상일경우 1을 넣고, 소수에서는 1을 빼줌, 1이면 1넣고 끝, 1보다 작으면 0을 넣음

    # 이진법이 들어갈 곳
    ans = []
    # 13이상이 필요하다면 overflow
    space = 0

    while space <= 13:

        number = number * 2

        if number < 1:
            ans.append(0)
            space += 1
        elif number > 1:
            ans.append(1)
            number -= 1
        else:  # 1인경우 이진법으로 바꾸는 건 종료
            ans.append(1)
            number += 1
            break

    # print(ans)   # [1, 0, 1]


    # 빈 칸 없이 출력 & 13이상일 때 overflow 출력하기
    # 13자리 이상 넘어간다면
    if space >= 13:
        print(f'#{test_case} overflow')
    else:
        print(f'#{test_case}', end=' ')
        for i in ans:
            print(i, end='')
        print()
