import sys
sys.stdin = open('../input.txt')


def food(row, col): #
    global min_dif, visited

    second_food = arr[row][col]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            else:
                visited[i][j] = 1
                visited[j][i] = 1
                second_food = arr[i][j] + arr[j][i]
                two_food_difference = abs(food_1 - second_food)
                if two_food_difference < min_dif:
                    min_dif = two_food_difference

    # visited 초기화
    visited = [[0] * N for _ in range(N)]
    return second_food

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    # 일단 두 요리 차이를 큰 값으로 저장
    min_dif = 99999

    # 모든 곳 다 탐색
    for i in range(N):
        for j in range(N):
            # 재료가 같다면 pass
            if i == j:
                visited[i][j] = 1
                visited[j][i] = 1
            elif visited[i][j] == 0:
                visited[i][j] = 1
                visited[j][i] = 1
                food_1 = arr[i][j] + arr[j][i]
                food_2 = food(0, 0)

    print(f'#{test_case} {min_dif}')