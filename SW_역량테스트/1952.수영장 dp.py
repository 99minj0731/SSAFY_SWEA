import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    # 이 곳에다가 전의 값들을 저장하면서 탐색할거다.
    month = [0] * 12

    # 1월, 2월, 3월은 3개월 전을 볼 수 없으니 미리 지정을 해놓는다.
    month[0] = min(price[0] * plan[0], price[1])
    month[1] = min(month[0] + plan[1] * price[0], month[0] + price[1])
    month[2] = min(month[1] + plan[2] * price[0], month[1] + price[1], price[2])

    # 3월달부터 탐색
    for i in range(3, 12): # i = 3, 4 ~~~~ 12
        # 1일권, 1달권, 3개월권 중 가장 작은 값으로 저장
        month[i] = min(month[i-1] + plan[i] * price[0], month[i-1] + price[1], month[i-3] + price[2])

    # 1년권이랑 마지막 비교
    ans = min(month[11], price[3])

    print(f'#{test_case} {ans}')

