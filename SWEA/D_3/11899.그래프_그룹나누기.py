import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    #N = 사람수, M = 신청서 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))  #[1, 2, 3, 4]

    # 자신의 최상위 부모를 저장
    p = [i for i in range(N + 1)]  #[0, 1, 2, 3, 4, 5]

    # 일단 다 혼자 한다고 가정
    result = N

    # 최상위 부모를 만들어 주는 함수
    def group(x):
        # 만약 자신이 부모라면
        if p[x] == x:
            return x
        # 만약 아니라면 자신의 부모의 부모의 부모의 값으로 바꿔줌
        else:
            x = group(p[x])
            return x


    for i in range(0, M * 2, 2):
        u = arr[i]
        v = arr[i + 1]

        a = group(u)
        b = group(v)

        # 만약 두 개의 값이 다르다면 하나의 조로 묶어줌
        if a == b:
            continue
        p[a] = b
        result -= 1

    print(f'#{test_case} {result}')