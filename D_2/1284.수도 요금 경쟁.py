import sys
sys.stdin = open('input.txt')

T = int(input()) #2

for test_case in range(1, T + 1):

    # P = A사 1L당 요금, Q = B사 R리터 이하 요금, S = B사 1L 당 요금, W = 사용한 물의 양
    P, Q, R, S, W = map(int, input().split())

    price = 0
    A_price = 0
    B_price = 0

    # W가 R 보다 작을 때
    if W <= R:
        A_price = P * W
        B_price = Q
        if A_price > B_price:
            price = B_price
        else:
            price = A_price

    # W가 R보다 클 때
    else:
        A_price = P * W
        B_price = Q + (S * (W - R))
        if A_price > B_price:
            price = B_price
        else:
            price = A_price

    print(f'#{test_case} {price}')

