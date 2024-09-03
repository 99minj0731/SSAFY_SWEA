import sys
sys.stdin = open('input.txt')

# 도시의 개수
N = int(input()) #4
distance = list(map(int, input().split()))   #[2, 3, 1]  -> [2, 3, 1, 0]
price = list(map(int, input().split()))    #[5, 2, 4, 1] -> [5, 2, 4]
price.pop()  # 맨 뒤에 있는 주유소는 필요없으니까 일단 뺌
distance.append(0)

#일단 첫번째 정류장은 무조건 들려야함
# oil_price = price[0] * distance[0]

oil_price = 0
n = N

while n > 0 :
    # 최소값 뒤에는 다 최솟값 * 그 뒤의 모든 거리
    min_num = min(price)
    min_num_idx = price.index(min_num)
    for i in range(min_num_idx, n):
        oil_price += distance[i] * min_num

    # 뒤에 값을 다 없애버리고 앞에 다시 시작
    price = price[:min_num_idx]
    distance = distance[:min_num_idx]
    n = min_num_idx

print(oil_price)


# price의 처음부터 끝-1까지 제일 작은 값을 구함
# while n > 0 :
#     min_num = min(price)
#     min_idx = price.index(min_num)
#     n = min_idx

# 제일 작은 값 뒤부터는 제일 작은 주유값 + 뒤에 있는 모든 거리
# 제일 작은 값 앞에를 다시 탐색해서 그 중 가장 작은 값을 찾아냄
# 그 앞에 다시 검색해서 가장 작은 값을 찾아냄
# 언제까지? 처음 도시까지 도달 할 때까지
