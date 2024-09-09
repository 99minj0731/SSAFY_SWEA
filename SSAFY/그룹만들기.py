# 요리사 그룹나누기

arr = 'ABCD'
N = len(arr)


def backtrack(k):
    if k == N:
        if not B:
            return
        print(A, B)



    else:
        A.append(arr[k])
        backtrack(k + 1)
        A.pop()

        B.append(arr[k])
        backtrack(k + 1)
        B.pop()


A, B = [arr[0]], []
backtrack(1)

'''
--------------------------------------------
'''

arr = [0, 1, 2, 3]
N = len(arr)

def dfs(cnt, idx):
    global used

    # 만약에 반으로 나눴다면
    if cnt == N //2:
        A_food = []
        B_food = []

        for i in range(N):
            if used[i] == 1:
                A_food.append(arr[i])
            else:
                B_food.append(arr[i])
        print(A_food, B_food)
        return

    for i in range(idx, N): # i= 0, 1, 2, 3
        # 만약 사용하지 않았다면 방문했다고 표시
        if used[i] == 0:
            used[i] = 1
            dfs(cnt + 1, idx + 1)
            # 다시 초기화
            used[i] = 0

used = [0] * N

dfs(0, 0)