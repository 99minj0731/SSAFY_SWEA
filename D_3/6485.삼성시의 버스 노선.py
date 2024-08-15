import sys
sys.stdin = open('input.txt', 'r')

T = int(input())  #1

for test_case in range(1, T+1):

    # 1, 2 총 두 번 반복 = N
    N = int(input())  # 2
    # for tc in range(1, N + 1): # 아래 bus 값으로 받기때문에 필요 없음
    # i 번째의 버스 노선은 Ai 이상, Bi 이하인 모든 정류장을 다닌다.
    bus = [list(map(int, input().split()))for l in range(N)]    # [[1, 3],[2, 5]]

    bus_station_num = int(input())  #5
    # bus_station_list = [0] * (bus_station_num + 1)   # 0번째 자리는 비워둠
    bus_station_list = [0] * 5001   # 버스 정류장이 총 5000개니까

    for i in range(N): # 0, 1 버스 2개니까 2번 반복
        # Ai 부터 Bi 까지 반복을 해서 해당 버스 정류장 자리에 +1씩 한다.
        for j in range(bus[i][0], bus[i][1]+1):  # 처음과 끝 정류장
            bus_station_list[j] += 1

    bus_index = [int(input()) for _ in range(bus_station_num)]
    # print(bus_index) # [1, 2, 3, 4, 5]

    print(f'#{test_case}', end=' ')

    for k in range(bus_station_num): # 0 1 2 3 4
        print(f'{bus_station_list[bus_index[k]]}', end=' ')
    print() # 다음 테스트 케이스가 나오면 줄 바꿈을 해줘야한다.

