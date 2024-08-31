import sys
sys.stdin = open('input.txt')
def word(n):
    global result

    if n > N:
        return

    word(n*2)
    print(f'{tree[n]}', end='')
    word(n*2+1)

for test_case in range(1,11):
    N = int(input())

    tree = [0] * (N + 1)

    for _ in range(N):
        arr = list(input().split())   #['1', 'W', '2', '3']
        tree[int(arr[0])] = arr[1]
        # tree = [0, 'W', 'F', 'R', 'O', 'T', 'A', 'E', 'S']

    print(f'#{test_case}', end=' ')
    word(1)
    print()
