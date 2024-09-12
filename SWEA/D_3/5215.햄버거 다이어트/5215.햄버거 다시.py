import sys
sys.stdin = open('../input.txt')

def burger(k, sum_taste, sum_kcal):
    global ans

    if sum_kcal > max_cal:
        return
    if k == N :
        if sum_taste > ans:
            ans = sum_taste
            return
    else:
        burger(k+1, sum_taste + foods[k][0], sum_kcal + foods[k][1])
        burger(k+1, sum_taste, sum_kcal)

T = int(input())

for test_case in range(1, T + 1):
    N, max_cal = map(int,input().split())
    foods = [list(map(int, input().split())) for _ in range(N)]
    # [[100, 200], [300, 500], [250, 300], [500, 1000], [400, 400]]

    ans = 0

    burger(0, 0, 0) # 깊이, 맛 점수 합계, 칼로리 합계

    print(f'#{test_case} {ans}')