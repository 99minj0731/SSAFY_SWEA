import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N = 마을 사람 수, M = 알려줄 정보 수
    N, M = map(int, input().split())

    p = [i for i in range(N + 1)]  #[0, 1, 2, 3, 4, 5, 6]

    # x가 속한 집합의 대표자를 반환하는 함수
    def find_set(x):
        # 만약 자기 자신이 대표자라면 자기자신 반환
        if x == p[x]:
            return x
        # 아니라면 자기 부모의 부모의 부모값을 찾아서 반환
        else:
            p[x] = find_set(p[x])
            return p[x]

    result = N  # 일단 처음에는 개인들이 각각의 무리라고 가정

    for _ in range(M):
        v, e = map(int, input().split())
        a = find_set(v)  #4
        b = find_set(e)  #6
        if a == b:
            continue
        # 합쳐질 때마다 -1씩 해줌
        p[a] = b
        result -= 1

    print(f'#{test_case} {result}')



