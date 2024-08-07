T = int(input())  # 예시 갯수

for test_case in range(1, T + 1):
    N = int(input())  # 행의 갯수
    box = [([0] * 10) for _ in range(10)]  # 10*10짜리 리스트를 만들었다.

    count = 0  # 겹치는 부분을 일단 0이라고 하고
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())  # 각각의 값을 따로 만들겠다. [2, 2, 4, 4, 1]
        for i in range(r1, r2 + 1):  # 세로의 길이 만큼
            for j in range(c1, c2 + 1):  # 가로의 길이 만큼./
                if box[i][j] == 0:  # 만약 그 자리가 0이라면
                    box[i][j] = color  # 그 자리를 color값으로 변경하고
                else:
                    box[i][j] = 3  # 아니라면 그 자리가 3을 넣겠다.
                    count += 1  # 그리고 count의 값을 1씩 올리겠다.

    print(f'#{test_case} {count}')