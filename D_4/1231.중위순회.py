import sys
sys.stdin = open('input.txt')



def subtree(n):

    if n == 0:
        return

    subtree(left[n])
    print(parents[n], end='')
    subtree(right[n])

T = 10

for test_case in range(1, T + 1):
    N = int(input()) # 정점의 개수
    # 정점의 문자, 왼쪽 자식, 오른쪽 자식의 정점 번호
    arr = list(input().split()for _ in range(N)) # ['1', 'W', '2', '3'] type : str

    parents = [0] * (N + 1)  # [0, 'W', 'F', 'R', 'O', 'T', 'A', 'E', 'S']
    left = [0] * (N + 1)     # [0, 2, 4, 6, 8, 0, 0, 0, 0]
    right = [0] * (N + 1)    # [0, 3, 5, 7, 0, 0, 0, 0, 0]

    for i in range(N):  # i = 0, 1, 2, 3, 4, 5, 6, 7, 8
        parents[int(arr[i][0])] = arr[i][1]

    for i in range(N):
        # 왼쪽, 오른쪽 자식 모두 있을 경우
        if len(arr[i]) == 4:
            left[int(arr[i][0])] = int(arr[i][2])
            right[int(arr[i][0])] = int(arr[i][3])
        # 왼쪽 자식만 있는 경우
        if len(arr[i]) == 3:
            left[int(arr[i][0])] = int(arr[i][2])

    # 중위순회로 출력하기
    print(f'#{test_case}', end=' ')
    subtree(1)
    print()


