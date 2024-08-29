import sys
sys.stdin = open('input.txt')

# 16진수를 10진수로 만들어주는 함수
def make_jinsu(num):
    if num == 'A':
        tenjinsu = 10
    elif num == 'B':
        tenjinsu = 11
    elif num == 'C':
        tenjinsu = 12
    elif num == 'D':
        tenjinsu = 13
    elif num == 'E':
        tenjinsu = 14
    elif num == 'F':
        tenjinsu = 15
    # 숫자일 경우 문자열에서 숫자열로 만들어줌
    else:
        tenjinsu = int(num)

    return tenjinsu

T = int(input())

for test_case in range(1, T + 1):

    N, arr = input().split() # 일단 문자열로 받고
    N = int(N)  # 문자 개수는 숫자로 바꿔줌

    ans = []  #[4, 7, 15, 14]

    for i in arr:  # i = 4, 7, F, E  16진수

        # 함수를 돌려서 10진수로 만들어 준다.
        tenjinsu = make_jinsu(i)
        ans.append(tenjinsu)

    answer = ''

    for i in ans:    # 4, 7, 15, 14
        result = ''
        for j in range(4):  # 각 문자당 4자리를 만들어야 하니까 4번 반복

            # 0 이 되면 앞에 계속 0을 붙힘
            if i == 0:
                result = '0' + result
            # 나머지가 0일 경우
            elif i % 2 == 0:
                result = '0' + result
                i = i // 2
            # 나머지가 1일 경우
            elif i % 2 == 1:
                result = '1' + result
                i = i // 2

        answer = answer + result

    print(f'#{test_case} {answer}')







