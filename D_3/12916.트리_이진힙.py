import sys
sys.stdin = open('input.txt')

T = int(input())

# 상위루트가 제일 작은 값이 되도록 만드는 함수
def enq(n):
    global last
    last += 1  # 트리 자리 1부터 채워서 함수 호출할 때마다 하나씩 자리를 늘려준다.
    tree[last] = n  # 일단 해당 자리에 값을 넣고
    child = last    # 그 자리를 자손자리로 한다.
    parent = child // 2

    # 부모가 존재하고 부모가 자식보다 더 큰 경우에 바꿔주겠다.
    while parent >= 1 and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]  #서로의 값을 바꿔주고
        child = parent   # 자식의 자리를 부모의 자리로 옮기고
        parent = child // 2 # 부모도 한 단계 올려준다.

for test_case in range(1, T + 1):
    N = int(input())  #노드의 개수
    arr = list(map(int, input().split()))  #[7, 3, 5, 2, 4, 6]

    tree = [0] * (N + 1)  # [0, 0, 0, 0, 0, 0, 0]

    last = 0  # 하나씩 더해줘서 1부터 인덱스 자리를 만듦

    for num in arr: # num = 7, 3, 5, 2, 4, 6
        enq(num)

    # enq(num)결과
    # print(tree)  #[0, 2, 3, 5, 7, 4, 6]

    # 조상 노드의 합 구하기
    parent_sum = 0
    while N > 0:  # N이 1이 될 때까지 반복한다.
        parent_sum += tree[N//2]
        N = N // 2

    print(f'#{test_case} {parent_sum}')


