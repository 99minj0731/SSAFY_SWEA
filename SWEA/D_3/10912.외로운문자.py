import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    arr = list(input())   #['q', 'n', 'w', 'e', 'r', 'r', 'e', 'w', 'm', 'q']

    # 문자들 넣고 뺄 리스트
    lst = []

    for i in range(len(arr)):
        if arr[i] not in lst:
            lst.append(arr[i])
        elif arr[i] in lst:
            lst.remove(arr[i])

    # 리스트가 비었다면 good 출력
    if len(lst) == 0 :
        print(f'#{test_case} Good')

    # 알파벳 순서대로 출력 - 아스키 사용
    else:

        # # 알파벳을 숫자로 바꾼 후 오름차순으로 정렬
        # ord_list = []
        # for i in range(len(lst)):
        #     ord_list.append(ord(lst[i]))
        # ord_list.sort()   #[97, 98, 99]
        #
        # # 숫자를 다시 알파벳으로 변경
        # ord_to_alph = []  #['a', 'b', 'c']
        # for i in range(len(ord_list)):
        #     ord_to_alph.append(chr(ord_list[i]))

        # 알파벳 순서대로 정렬하기
        for i in range(len(lst)):
            lst[i] = ord(lst[i])
        lst.sort()

        # 띄어쓰기 없애기
        print(f'#{test_case}', end=' ')
        for i in range(len(lst)):
            print(chr(lst[i]), end='')
        print()


        '''
        lst.reverse()    # c y
        print(f'#{test_case}', end=' ')
        for i in range(len(lst)):
            print(lst[i], end='')
        print()
        '''
