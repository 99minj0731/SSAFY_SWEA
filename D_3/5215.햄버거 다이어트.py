import sys
sys.stdin = open('input.txt')

def burger(k, sum_taste, sum_kcal): # 0 0 1000
    global max_taste  # 비교값

    # # 최대 칼로리가 넘지 않을 때까지만 반복
    # while sum_kcal < kcal:

    # 현재까지 더한 값이 최대 칼로리를 넘기거나 트리 범위 밖이라면 돌아간다.
    if sum_kcal > max_kcal:
        return

    if k == N:
        # 최대 칼로리랑 현재 누적 칼로리 비교
        if max_taste < sum_kcal:
            max_taste = sum_kcal
        return

    # 최대 칼로리에 도달하지 못했다면
    burger(k + 1, sum_taste + food[k][0], sum_kcal + food[k][1])
    burger(k + 1, sum_taste, sum_kcal)




T = int(input()) #1

for test_case in range(1, T + 1):
    # N = 재료 개수, kcal = 먹을 수 있는 칼로리
    N, max_kcal = map(int, input().split())

    # food_taste_lst = []   #[100, 300, 250, 500, 400]
    # food_cal_lst = []     #[200, 500, 300, 1000, 400]

    # for _ in range(N):
    #     food_taste, food_cal = map(int, input().split())
    #     food_taste_lst.append(food_taste)
    #     food_cal_lst.append(food_cal)

    food = [list(map(int, input().split())) for _ in range(N)]
    # [[100, 200],[500, 1000], [400, 400]]

    # visited = [0] * N   #[0, 0, 0]
    max_taste = 0

    burger(0, 0, 0)

    print(f'#{test_case} {max_taste}')

'''
food 리스트에서 각 요소의 1번째 자리에 위치한 것들을 부분집합으로 만들고
만약 kcal가 넘는다면 탐색하지 않는다
각 요소의 0번째 자리를 더해줘서
제일 큰 값을 출력
'''


