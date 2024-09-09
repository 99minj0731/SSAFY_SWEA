import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    road = list(map(int,input().split()))  # 2 3 1
    city = list(map(int,input().split()))  # 5 2 4 1 (도시 기름 가격)

    sum_val = road[0] * city[0]   # 맨 초기값은 0번 인덱스끼리 곱해야됨
    start_pos = 1

    min_val = city[0]  # 최저 기름값

    for i in range(1,len(city)):
        if city[i] < min_val:   # 기름 최저값
            min_val = city[i]
            sum_val += min_val * road[start_pos]
            start_pos += 1
            if start_pos == len(road):
                break
        else:
            sum_val += min_val * road[start_pos]
            start_pos += 1
            if start_pos == len(road):
                break

    print(sum_val)





#-------------------------------------------------------------------------------


N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
sum_price = 0

def FindPrice():
    global N, road, price, sum_price
    for i in range(N - 1):
        sum_road = road[i]
        for j in range(i + 1, N - 1):
            if price[i] <= price[j]:  # 현재 주유소 기름 가격이 적거나 같은 경우
                sum_road += road[j]  # 도로의 길이를 더해줌
                if j == N - 2:
                    sum_price += price[i] * sum_road  # 현재 주유소 기름 가격과 갈 수 있는 도로의 길이를 곱함
                    return sum_price
            else:  # 현재 주유소 기름 가격이 큰 경우
                break
        sum_price += price[i] * sum_road  # 현재 주유소 기름 가격과 갈 수 있는 도로의 길이를 곱함
    return sum_price
    # else:
    #     sum_price += price[i] * sum_road

ans = FindPrice()
print(ans)

# -------------------------------------------------------------------------------














