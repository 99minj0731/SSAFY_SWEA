import sys
sys.stdin = open("input.txt", "r")

T = int(input()) #10

for test_case in range(1, T+1):  #1번부터 10번
    N = int(input())    #4이라고 가정

    S = []  #빈 리스트를 만들고

    # arr= [[1]*k for k in range(1,N+1)]   #아래있는 3줄 이렇게 변경 가능
    for k in range(1, N+1):
        M = [1] * k
        S.append(M)   #[[1],[1,1],[1,1,1],[1,1,1,1]]

    if 2 < test_case :  #테스트 케이스 3번 부터
        for i in range(2, N):   #행의 범위     #0행, 1행은 안바꿔도 되니까 2행부터
            for j in range(1, i):  #열의 범위  #0열, 마지막열은 안바꿔도 되니까
                S[i][j] = S[i-1][j-1] + S[i-1][j]  #그 값을 위의 두 개의 값을 더한걸로 바꿔준다.
    #             # if S[i-1][j-1] < N and S[i-1][j] < i+1 :  #범위 밖을 벗어난다면
    #             #     S[i-1][j-1] = 0
    #             #     S[i-1][j] = 0
    #             # else:
    #             #     S[i][j] = S[i-1][j-1] + S[i-1][j]


    # print(S) #[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    # print(*S) #[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]

    print(f'#{test_case}')
    for row in S:
        print(*row)
