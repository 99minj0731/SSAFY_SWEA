import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N = 카드수
    N = int(input())

    arr = list(input().split())  # ['ALAKIR', 'ALEXSTRASZA', 'DR-BOOM', 'LORD-JARAXXUS', 'AVIANA']

    D = N // 2 + N % 2

    first_lst = []
    second_lst = []
    result = []

    for i in range(D):
        first_lst.append(arr[i])

    for i in range(D, N):
        second_lst.append(arr[i])

    for i in range(D): # i = 0, 1, 2
        if first_lst != []:  # 빈 리스트가 아닐경우
            result.append(first_lst.pop(0))
        if second_lst != []:
            result.append(second_lst.pop(0))

    print(f'#{test_case}', *result)

'''
1. 카드의 갯수가 짝수일 때와 홀수일 때 반을 어떻게 나눌 것인지
'''