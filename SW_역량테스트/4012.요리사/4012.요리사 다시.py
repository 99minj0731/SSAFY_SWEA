import sys
sys.stdin = open('input.txt')

def synergy(group, arr):
    synergy = 0

    for i in range(len(group)): # 음식에 사용한 재료의 갯수만큼 반복
        for j in range(i + 1, len(group)): # 그 뒤의 값까지
            synergy += arr[group[i]][group[j]] + arr[group[j]][group[i]]
    return synergy


def dfs(cnt, idx): # cnt = A그룹에 선택된 재료의 개수, idx = 어떤 재료인지
    global ans

    # 만약 재료를 반반으로 구별을 했다면
    if cnt == N //2:
        ingredient_A = []
        ingredient_B = []

        # 재료를 반씩 나누겠다.
        for i in range(N):
            if used[i] != 0: #만약 사용한 재료라면
                ingredient_A.append(i)
            else:
                ingredient_B.append(i)

        # A와 B음식의 시너지를 계산
        synergy_A = synergy(ingredient_A, arr)
        synergy_B = synergy(ingredient_B, arr)

        # 최솟값 구하기
        ans = min(ans, abs(synergy_A- synergy_B))
        return

    # 재료를 반씩 나눠주겠다.
    for i in range(idx, N): # i = 0, 1, 2, 3
        if used[i] == 0: #만약 사용되지 않은 재료라면
            used[i] = 1  #사용했다고 표시하고
            dfs(cnt + 1, i + 1)
            used[i] = 0  #다시 리셋시켜줌(백트레킹)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #[[0, 5, 3, 8], [4, 0, 4, 1], [2, 5, 0, 3], [7, 2, 3, 0]]

    food_A = 0
    food_B = 0
    # 계속 갱신될거임
    ans = float('inf')
    used = [0] * N # [0, 0, 0, 0]

    dfs(0, 0)

    print(f'#{test_case} {ans}')


    # # 재료가 4개면 2개씩 나눠서 사용해야함
    # # food_A 구하기
    # for i in range(N):       # i = 0, 1, 2, 3
    #     if used[i] == 0 :    # 사용하지 않은 재료라면
    #         used[i] = 1    #사용했다고 표시
    #     for j in range(N):   # j = 0, 1, 2, 3
    #         if used[j] == 0:  # 사용하지 않는 재료라면
    #             used[j] = 1   # 사용했다고 표시하고
    #             food_A = arr[i][j] + arr[j][i]
    #             food_B = food(0, 0)
    #             if abs(food_A - food_B) < ans:
    #                 ans = abs(food_A - food_B)

'''
1. 재료가 N개가 주어졌다. 
2. 그 중에서 절반을 사용한다. 
3. A음식에 사용한 건 B음식에 사용하지 못한다. 
4. 부분집합으로 N // 2 씩 만들어서 [12, 13, 14, 23, 24, 34] 총 경우의 수는 N!
5. 백드래킹으로

'''

