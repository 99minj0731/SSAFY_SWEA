def matgip(N, L, lst):
    arr = [0] * (L + 1)    # 저장할 배열 만들기
    for score, cal in lst:   # 리스트에서 점수랑 칼로리를 꺼낼꺼야
        for cur_sum in range(L, cal - 1, -1): # 뒤에서부터 검사할꺼야
            # 현재의 값과 비교하면서 큰 쪽으로 갱신해줌
            arr[cur_sum] = max(arr[cur_sum], arr[cur_sum - cal] + score)

    return arr[L]

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())  # N = 재료의 수, L = 제한 칼로리
    lst = []
    for _ in range(N):
        score, cal = map(int, input().split())  # 맛 점수, 칼로리
        lst.append((score, cal))

    result = matgip(N, L, lst)
    print(f'#{tc} {result}')


















T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    lst = []
    for _ in range(N):
        score, cal = map(int, input().split())
        lst.append((score, cal))

    max_score = 0

    for i in range(1 << N):  # 부분집합 사용
        sum_cal = 0
        sum_score = 0

        # subset_list = []

        for j in range(N):
            subset = []
            if i & (1 << j):
                # subset.append(lst[j])
                sum_score += lst[j][0]
                sum_cal += lst[j][1]
            # subset_list.append(subset)

        if sum_cal <= L:
            max_score = max(max_score, sum_score)

    # print(subset_list)
    # [[(100, 200)], [(300, 500)], [(250, 300)], [(500, 1000)], [(400, 400)]]
    print(f'#{tc} {max_score}')