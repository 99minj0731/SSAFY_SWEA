import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 2
    arr = list(map(int, input().split()))

    # 일단 제일 큰 값으로 가정
    ans = 1e9

    # lecture = []   #[0, 4, 6]
    # M = len(lecture) # 일주일에 강의를 몇 번 들을 수 있는지

    # # 일주일을 순회
    # for i in range(7):
    #     if arr[i] == 1:
    #         lecture.append(i)

    for start in range(7):
        days = 0
        count = 0
        if arr[start] == 1:
            # 시작 요일을 정함
            now = start
            # 수업을 다 들을 때까지 반복
            while N > count:
                if arr[now % 7] == 1:
                    count += 1
                days += 1
                now += 1

            ans = min(ans, days)

    print(f'#{test_case} {ans}')

'''
arr를 순회하면서
N이 0이 될때까지 반복
1 이 나오면 N을 1개 빼주고 ans += 1

'''