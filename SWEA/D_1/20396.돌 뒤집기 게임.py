import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())        # N = 5, M = 1
    arr = list(map(int, input().split()))   # 01010

    # 몇 번 돌맹이를 바꿀건지 = M
    for l in range(M):
        i, j = map(int, input().split())    # i = 2, j = 2

        # 몇 번 째 돌맹이까지 뒤집을 건지 = j
        for k in range(j):  # k = 0, 1
            # 만약 배열 안에 있고, 여기서 말하는 i(2)의 실제 위치는 i-1(1) 위치함
            if i-1 + k < N:
                if arr[i-1] != arr[i+k-1]:   # 만약 바꿔야하는 돌맹이가 나오면
                    arr[i+k-1] = arr[i-1]     # 그 돌을 i 번째 돌과 동일하게 만들어라

    print(f'#{test_case}', *arr)




