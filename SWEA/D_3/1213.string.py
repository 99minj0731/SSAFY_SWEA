import sys
sys.stdin = open("input.txt", encoding ="UTF8")


for test_case in range(10):
    T = int(input())  # 테스트 케이스 번호
    p = str(input())  # 찾아야 하는 것 ti
    t = str(input())  # 문자열 Starteatingwellwitht'''

    M = len(p)  # is의 길이 #2
    N = len(t) #전체 문자열의 길이

    i = 0 #전체 문자열의 위치 t
    j = 0 # is 위치 p
    cnt = 0

    while i < N and j < M:  # 범위 이내에 있을 때까지 반복
        if t[i] != p[j]:  # 값이 다르다면
            i = i - j + 1  # 찾았던 인덱스 바로 뒤부터 다시 시작 여기서 +1 해도 됨
            j = 0  # 찾아야하는 문자는 처음으로 돌아가
        # i += 1
        # j += 1
        else: #일치하다면
            cnt += 1

        print(f'#{T} {cnt}')

    # for i in range(N-M+1):
    #     for j in range(M):
    #         if t[i+j] != p[j]:  #값이 일치하지 않는다면
    #             break     # for j, 멈추고 다음 글자부터 비교 시작
    #         else:   #일치하다면
    #             continue #계속 반복해
    #     else:   #for j가 중단없이 반복되면
    #         cnt += 1





