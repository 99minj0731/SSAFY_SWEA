import sys
sys.stdin = open('input.txt')

T = int(input())  # 3

for test_case in range(1, T + 1):

    # 칠할 영역 개수 // N = 2
    N = int(input())

    # 10 * 10 리스트 만들기
    paper = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        # 2 2 4 4 1
        # 3 3 6 6 2

        # 색이 1일 경우 먼저
        if color == 1:
            for i in range(r1, r2 + 1):       # i = 2, 3, 4
                for j in range(c1, c2 + 1):   # j = 2, 3, 4
                    # 해당 자리가 자신과 같은 색으로 칠해져 지지 않을 경우에만 색을 칠하겠다.
                    if paper[i][j] != 1 :
                        paper[i][j] += 1
        # 색이 2일 경우
        else:
            for i in range(r1, r2 + 1):       # i = 3, 4, 5, 6
                for j in range(c1, c2 + 1):   # j = 3, 4, 5, 6
                    # 해당 자리가 자신과 같은 색으로 칠해져 지지 않을 경우에만 색을 칠하겠다.
                    if paper[i][j] != 2 :
                        paper[i][j] += 2

    purple = 0

    # 합이 3(보라색)인 곳 찾기
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                purple += 1

    print(f'#{test_case} {purple}')




'''
1. 빈 박스를 만들고
2. 해당 영역에 color 값을 더해주는데
3. 만약 나랑색이 같으면 더해주지 않는다.
4. color가 1일 경우랑 2일 경우를 나눠서 해야하나
'''


