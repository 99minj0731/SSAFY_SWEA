import sys
sys.stdin = open('input.txt')

def subtree(n):
    global cnt

    if n == 0:
        return

    # if left[n] != 0:
    #     cnt += 1
    # if right[n] != 0:
    #     cnt += 1

    subtree(left[n])
    subtree(right[n])
    cnt += 1

T = int(input())

for test_case in range(1, T + 1):

    # E = 간선의 개수, N = N을 루트로 하는 노드들의 갯수찾기
    E, N = map(int, input().split())  # 5, 1
    arr = list(map(int, input().split()))
    # 2 1 2 5 1 6 5 3 6 4

    left = [0] * (E+2)   #[0, 0, 0, 0, 0, 0, 0]  [0, 6, 1, 0, 0, 3, 4]
    right = [0] * (E+2)  #[0, 0, 0, 0, 0, 0, 0]  [0, 0, 5, 0, 0, 0, 0]

    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    cnt = 0
    subtree(N)

    print(f'#{test_case} {cnt}')

