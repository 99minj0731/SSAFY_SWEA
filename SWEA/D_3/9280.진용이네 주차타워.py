import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 단위 무게 당 요금
    R = [list(map(int, input()))for _ in range(N)]  # [[2], [3], [5]] (단위 무게당 요금)
    W = [list(map(int, input()))for _ in range(M)]  # [[2], [1], [3], [8]] (차량의 무게)
    car_list = [list(map(str,input())) for _ in range(2*M)] #[['3'], ['2'], ['-', '3'], ['1'], ['4'], ['-', '4'], ['-', '2'], ['-', '1']]

    parking_lot = [0] * N
    money = 0

    for k in range(2 * M):

            # 만약 들어오는 차량이라면
            if len(car_list[k]) == 1:
                for i in range(N):  # i = 0, 1, 2
                    if parking_lot[i] == 0:
                        money += int(W[int(car_list[k][0]) - 1][0]) * int(R[i][0])
                        # 주차장에 해당 자동차 번호를 넣어줌
                        parking_lot[i] = int(car_list[k][0])
                        # idx[i] = parking_lot.index(int(car_list[k][0]))
                        break

            # 만약 나가는 차량이라면
            elif len(car_list[k]) == 2:
                # 그 자리를 0으로 만들어 준다.
                # parking_lot.insert(int(car_list[k][1]), 0)
                for i in range(len(parking_lot)):
                    if parking_lot[i] == int(car_list[k][1]):
                        parking_lot[i] = 0
                        break


    print(f'#{test_case} {money}')
















