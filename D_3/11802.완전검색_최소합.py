import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]


    min_number = 9999999999999

    # (r, c) 현재 위치 -> 오른쪽 (r, c+1), 아래(r+1, c)
    def dfs(r, c, count):
        global min_number
        # count += arr[r][c]

        #도착점(N-1, N-1)에 도착
        if r == N-1 and c == N-1:
            # count += arr[r][c]
            if count < min_number:
                min_number = count
                # count = 0
            return

        #오른쪽으로 갈 수 있는지
        if c + 1 < N:
            dfs(r, c+1, count + arr[r][c+1])
        # 아래로 갈 수 있는지
        if r + 1 < N:
            dfs(r+1, c, count + arr[r+1][c])


    dfs(0, 0, arr[0][0])

    print(f'#{test_case} {min_number}')