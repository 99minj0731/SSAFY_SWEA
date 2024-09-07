def charge(s, cnt):  # s= 현재 위치, cnt = 충전 횟수
    global charge_num

    # 가지치기
    # 만약 충전횟수가 앞에 구해놨던 횟수보다 크다면 그 이후로는 볼 필요 없음
    if cnt >= charge_num:
        return

    # 만약 종점 혹은 종점을 넘었다.
    if s >= N - 1:
        if charge_num > cnt:
            charge_num = cnt
            return

    # 1부터 해당 정류장에서 갈 수 있는 만큼
    for i in range(1, arr[s]+1):
        charge(s+i, cnt + 1)

T = int(input())
for test_case in range(1, T + 1):          # [5, 2, 3, 1, 1]
    arr = list(map(int, input().split()))  # [2, 3, 1, 1]
    N = arr.pop(0) # 정류장의 갯수  #5

    # 최대 충전 횟수는 정류장의 수 - 1이니까 일단 이걸로 저장
    # 처음 충전한거는 충전에 포함이 안되니까 - 2라고 가정
    charge_num = N - 2

    # 시작은 0번쨰 정류장부터, 충전횟수는 -1부터 시작한다.
    charge(0, -1)

    print(f'#{test_case} {charge_num}')