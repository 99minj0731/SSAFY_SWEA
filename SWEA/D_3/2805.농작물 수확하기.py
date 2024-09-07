import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #50

for test_case in range(1, T+1):
    N = int(input())  # N * N 의 열 // N = 5
    arr = [list(map(int, input()))for _ in range(N)]
    # print(arr) #[[1, 4, 0, 5, 4], [4, 4, 2, 5, 0], [0, 2, 0, 3, 2], [5, 1, 2, 0, 4], [5, 2, 2, 1, 2]]

    sum_max = arr[0][N//2]  #수확한 최종 작물의 수, 초기값은 i행이 0번째일 때의 가운데 값으로 지정
    start = end = N // 2     # 시작점과 끝점(j열의 idx)을 N의 가운데 값으로 정해놓는다.

    for i in range(1, N): #0번째 행 아래에 있는 것들을 더할 것이다.
        # i(행)이 가운데보다 위일 때는 start는 왼쪽으로 한 칸씩, end는 오른쪽으로 한 칸씩 이동시킨다.
        if i <= N // 2:
            start = start - 1
            end = end + 1
            # 해당 행에서 수확할 수 있는 작물들을 더해준다.
            for j in range(start, end + 1):
                sum_max += arr[i][j]
        # i (행)이 가운데보다 아래일 떄는 start는 오른쪽으로 한 칸씩, end는 왼쪽으로 한 칸씩 이동시킨다.
        else:
            start = start + 1
            end = end - 1
            for j in range(start, end + 1):
                sum_max += arr[i][j]

    print(f'#{test_case} {sum_max}')




