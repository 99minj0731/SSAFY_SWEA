import sys
sys.stdin = open('input.txt')

def subtree(n):
    global idx_num
    idx_num += 1

    tree[idx_num] = n

    child = idx_num
    parent = idx_num //2

    #만약 자식의 값이 부모의 값보다 작다면
    while parent > 0 and tree[child] < tree[parent]:
        tree[child], tree[parent] = tree[parent], tree[child]
        child = parent
        parent = parent // 2


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())  #노드의 개수  6
    arr = list(map(int, input().split()))  #[7, 3, 5, 2, 4, 6]

    tree = [0] * (N + 1)   #[0, 2, 3, 5, 7, 4, 6]

    idx_num = 0

    for num in arr:
        subtree(num)

    # 마지막 노드의 조상 노드에 저장된 정수의 합 구하기
    ans = 0
    while N >= 1:
        N = N // 2
        ans += tree[N]

    print(f'#{test_case} {ans}')
    # print(tree)



