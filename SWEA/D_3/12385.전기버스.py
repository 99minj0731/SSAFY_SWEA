import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # K = 한 번 충전시 갈 수 있는 정류장 수, N = 가야하는 정류장 번호, M = 충전기 있는 정류장의 수
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # [1, 3, 5, 7, 9]

    # 충전기가 있는 정류장을 1로 표기
    bus_charge = [0] * (N + 1)
    for i in arr:
        bus_charge[i] += 1

    # 현재 버스가 있는 자리 idx
    cur_bus = 0
    # 충전 횟수
    charge_num = 0
    # 정류장 배치가 이상할 때 사용할 리스트

    flag = False
    # 목표 정류장(N)이상 갈 때까지 반복
    while cur_bus < N:   #목표 정류장 이상으로 갔다면 안한다.
        cur_bus += K
        wrong_bus = K  # 1이 되면 평생 안되는거임  3
        if cur_bus >= N:
            break
        # 해당 자리에 충전기가 없다면
        if bus_charge[cur_bus] != 1:
            #충전기가 나올 때까지 한 정류장씩 앞으로 이동
            while bus_charge[cur_bus] == 0:
                cur_bus -= 1
                wrong_bus -=1
                if wrong_bus == 1 and bus_charge[cur_bus] == 0 :
                    flag = True
                    break
            if flag:
                break
            charge_num += 1
        # 해당 자리에 충전소가 있다면 충전하고 간다.
        else:
            charge_num += 1

    if flag:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} {charge_num}')




'''
1. 현재 자리에서 +3 을 해준다 +k
2. 근데 갔는데 충전기가 없다
3. 충전기 리스트 [0] * N +1 에다가 충전기 있는 곳에 1로 표시해놓고
4. 지금 버스가 있는 자리에다가 -1 씩 하면서 1이 있는 곳까지 간다음에
5. 그 자리에서 충전을 하고 (여기서 charge 횟수 +1 씩 해주기)
6. 다시 +k를 해준다
'''