import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) #신청 인원

    start = []  #[20, 17, 23, 4, 8]    # [4, 8, 17, 20, 23]
    end = []    #[23, 20, 24, 14, 18]  #[14, 18, 20, 23, 24]

    for _ in range(N):
        s, e = map(int, input().split())
        start.append(s)
        end.append(e)

    # 끝나는 시간이 가장 빠른 순서로 정렬
    for i in range(N):  # i = 0, 1, 2, 3, 4
        for j in range(N-1, i, -1):  # 4 3 2 1
            if end[i] > end[j]:
                end[i], end[j] = end[j], end[i]
                start[i], start[j] = start[j], start[i]

    count = 1
    # 끝나는 시점을 일단 첫번째 end값으로 저장
    start_time = end[0]

    for k in range(1, N): # i = 0, 1, 2, 3, 4
        if start[k] >= start_time:
            count += 1
            # 시작 지점을 현재 끝 시간으로 수정
            start_time = end[k]

    print(f'#{test_case} {count}')
