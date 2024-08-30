import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    N, M = map(int, input().split())


    # # M을 이진수로 표현하기
    # e_jinsu = ''   #0101111

    # while M >= 0:
    #     if M == 0:
    #         e_jinsu = '0' + e_jinsu
    #         break
    #     elif M % 2 == 1:
    #         e_jinsu = '1' + e_jinsu
    #         M = M // 2
    #     elif M % 2 == 0:
    #         e_jinsu = '0' + e_jinsu
    #         M = M // 2

    # print(bin(M))
    # print(bin(M)[2:])

    # 조명이 켜졌는지 확인하기
    for i in range(N): # N=0, 1, 2, 3
        result = M & (1 << i)
        # print(result)
        # print(bin(result))
        if result == 0:
            print(f'#{test_case} OFF')
            break
    else:
        print(f'#{test_case} ON')


'''    
    flag = False

    # for i in range(len(e_jinsu)-1, len(e_jinsu)-N + 1, -1):
    k = len(e_jinsu)

    result = e_jinsu[k-N:k]


    if '0' in result:
        print(f'#{test_case} OFF')
    else:
        print(f'#{test_case} ON')

        # #0일경우
        # if i == -1:
        #     if e_jinsu == '0':
        #         print('OFF')
        #         break
        #     else:
        #         print('ON')
        #         break
        #
        # #다른 정수일 경우
        # else:
        #     if e_jinsu[i] == 1:
        #         pass
        #     else:
        #         print('OFF')
        #         break
        #
        # print('ON')
'''









