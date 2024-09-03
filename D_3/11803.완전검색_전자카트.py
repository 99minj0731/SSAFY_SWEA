import sys
sys.stdin = open('input.txt')

def cart(cur_place, visit_num, cur_sum):
    global min_course

    # 아래로 내려갔는데 이미 최소값을 넘겼다면 다시 위로 올라간다.
    if cur_sum > min_course:
        return

    # 아래 끝까지 내려갔으면 값 비교해서 갱신
    # 마지막 방문한 곳에서 다시 회사로 돌아온 곳을 다시 더해줘야함
    if visit_num == N-1:
        if min_course > cur_sum + arr[cur_place][0]:
            min_course = cur_sum + arr[cur_place][0]
            return


    else:
        # i = 1, 2, 3 회사에서 시작해서 총 3군데를 더 가야한다.
        for i in range(1, N):
            # 만약 나랑 같은 위치라면 넘어간다.
            if cur_place == i:
                continue
            # 만약 방문하지 않은 곳이다.
            if visited[i] == 0:
                visited[i] = 1
                cart(i, visit_num + 1, cur_sum + arr[cur_place][i])
                visited[i] = 0



T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 4
    arr = [list(map(int, input().split())) for _ in range(N)]
    # [[0, 83, 65, 97], [82, 0, 78, 6], [19, 19, 0, 82], [6, 34, 94, 0]]

    visited = [0] * N  # [0,0,0,0] 방문을 했으면 1로 표현
    min_course = float('inf') # 일단 제일 큰 값으로 저장해둠

    cart(0, 0, 0)

    print(f'#{test_case} {min_course}')


