import sys
sys.stdin = open('input.txt')

for test_case in range(1,11):
    N = int(input())

    tree = [0] * (N + 1)  # [0, '-', '-', '10', '88', '65']
    left = [0] * (N + 1)  # [0, 2, 4, 0, 0, 0]
    right = [0] * (N + 1) # [0, 3, 5, 0, 0, 0]


    for _ in range(N):
        arr = input().split()

        tree[int(arr[0])] = arr[1]

        # 자식이 있는 노드라면 왼쪽, 오른쪽 자식값을 저장
        if len(arr) == 4:
            left[int(arr[0])] = int(arr[2])
            right[int(arr[0])] = int(arr[3])

    # 사칙연산하기
    def calc(n): # n = 1-> 2-> 4-> return tree[4]
        # 왼쪽에 자식이 없다면 자식이 오른쪽에도 없는거니까 나를 호출했던 함수 L이 88이됨
        if left[n] == 0:
            return tree[n]

        # 왼쪽 맨 아래 자식부터 시작
        L = calc(left[n]) # 88, 이때 n의 값은? 2
        R = calc(right[n]) # n = 2 -> 5 -> turn tree[5] -> n = 2 -> R = 65

        L, R = int(L), int(R)
        if tree[n] == '+':
            result = L + R
        elif tree[n] == '-':
            result = L - R
        elif tree[n] == '*':
            result = L * R
        else:
            result = L // R

        return result # L = 23 이 때 n의 값은? 2 -> 1

    ans = calc(1)

    print(f'#{test_case} {ans}')














