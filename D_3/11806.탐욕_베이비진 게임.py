import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,  T + 1):
    arr = list(map(int, input().split()))

    # 연속적인 숫자가 3개 이상이면 run, 같은 숫자 3개 이상이면 triple

    # 플레이어 2명이 낼 카드
    A_card = []  #[5, 2, 1, 2, 9, 0]
    B_card = []  #[3, 9, 5, 0, 2, 0]

    for i in range(0, len(arr), 2):
        A_card.append(arr[i])
        B_card.append(arr[i+1])

    # 0 ~ 9까지 넣을 곳
    A_check_card = [0]*10
    B_check_card = [0]*10

    # 카드를 한 번씩 낼 때마 횟수 기록. 적은 사람이 이기는 거다.
    A_count = 0
    B_count = 0



    A_flag = False
    for j in A_card:  # i = 5, 2, 1, 2, 9, 0
        A_check_card[j] += 1
        for i in range(10):
            #트리플일 경우
            if A_check_card[i] == 3:
                A_flag = True
                break
            #베이비진일 경우
            if 0 <= i <= 7:
                if A_check_card[i] >= 1 and A_check_card[i+1] >= 1 and A_check_card[i+2] >= 1:
                    A_flag = True
                    break
        # 트리플 혹은 베이비진일 경우 끝낸다.
        if A_flag:
            break
        A_count += 1


    B_flag = False
    for j in B_card:  # i = 5, 2, 1, 2, 9, 0
        B_check_card[j] += 1
        for i in range(10):
            # 트리플일 경우
            if B_check_card[i] == 3:
                B_flag = True
                break
            # 베이비진일 경우
            if 0 <= i <= 7:
                if B_check_card[i] >= 1 and B_check_card[i + 1] >= 1 and B_check_card[i + 2] >= 1:
                    B_flag = True
                    break
        # 트리플 혹은 베이비진일 경우 끝낸다.
        if B_flag:
            break
        B_count += 1


    # 누가 이겼는지 비교

    #아무도 run이나 triple이 안됐을 경우
    if A_count == 6 and B_count == 6:
        print(f'#{test_case} 0')
    elif A_count > B_count:
        print(f'#{test_case} 2')
    elif A_count < B_count:
        print(f'#{test_case} 1')
    # A가 먼저 가져갔으니까 얘가 먼저 승리할 때가 있음
    else:
        print(f'#{test_case} 1')

    # print(A_count, B_count)







