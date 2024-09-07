import sys; sys.stdin = open('input.txt')

def fitness(month, sum_cost): #month:시작 달, sum_cost:시작 달 전까지의 금액
    global min_cost, visited

    # 종료 조건
    # 만약 12월달까지 다 봤으면 계산해서 값 수정하기
    if month > 11:
        if sum_cost < min_cost:
            min_cost = sum_cost
            # min_cost = min(min_cost, sum_cost)
            return

    # 가지 치기
    # 만약 지금까지 더한 값이 더 크다면 그 뒤로는 볼 필요 없음
    if sum_cost >= min_cost:
        return

    flag = True

    # 총 12달을 탐색
    for i in range(12):
        if visited[i] == 0:
            visited[i] = 1
            # 총 4개의 경우 탐색
            for j in range(4):
                # sum_cost += monthly_plan[i] * price[j]
                if j == 0: # 1일권을 구매했을 경우
                    fitness(month + 1, sum_cost + (monthly_plan[month] * price[0]))
                    visited[i] = 0
                elif j == 1: # 한달권을 구매했을 경우
                    fitness(month + 1, sum_cost + price[1])
                    visited[i] = 0
                elif j == 2: # 세달권을 구매했을 경우
                    fitness(month + 3, sum_cost + price[2])
                    visited[i] = 0
                else:
                    flag = False
                    break
        if flag == False:
            break

T = int(input())

for test_case in range(1, T + 1):
    # 1일권, 한 달 권, 3개월 권, 1년권
    price = list(map(int, input().split()))  #[10, 40, 100, 300]
    monthly_plan = list(map(int, input().split()))
    #[0, 0, 2, 9, 1, 5, 0, 0, 0, 0, 0, 0]

    # 방문한 곳 체크용
    visited = [0] * len(monthly_plan)

    # 일단 1년권이 가장 적다고 가정하고 시작
    min_cost = price[3]

    fitness(0, 0)
    print(f'#{test_case} {min_cost}')


'''
1. 1일 권을 구매 했다. -> 한 달 뒤 확인
2. 한달 권을 구매 했다. -> 한 달 뒤 확인
3. 세 달 권을 구매했다. -> 세 달 뒤 확인
4. 일 년 권을 구매했다. -> 확인 불필요.

1. 1일권 -> 1일권, 한 달 권, 세 달 권
2. 한달권 -> 1일권, 한달 권, 세 달 권
3. 세달권 -> 1일권, 한달권, 세달 권
4. 1년권 

    # 1일권을 구매했을 경우
    fitness(month + 1, sum_cost + (monthly_plan[month] * price[0]))
    # 1달권을 구매했을 경우
    fitness(month + 1, sum_cost + price[1])
    # 세달권을 구매했을 경우
    fitness(month + 3, sum_cost + price[2])
    # 1년권을 구매했을 경우
    # fitness(month+12, sum_cost + price[3])

'''
