import sys
sys.stdin = open("input.txt", "r")

T = int(input())  #3

for test_case in range(1, T + 1):
    N, K = map(int, input().split())   # N=7, K=5
    arr = list(map(int, input().split())) # 1 3 5 6 4 4 6

    # 버블정렬
    for i in range(N): # N번째까지 반복하는 for 문
        min_num = arr[i]  # 가장 작은 수를 0번째라고 가정하고
        for j in range(i+1, N): # 그 뒤의 값들을 비교해서
            if arr[i] > arr[j]: # 뒤의 값이 더 작다면
                arr[i], arr[j] = arr[j], arr[i] #둘의 자리를 바꿔준다

    print(arr) # 정렬 끝 # 1 3 4 4 5 6 6

    # K번째 작은 수 찾기
    # K_num_idx = K-1 # 일단 k 번째 작은 수의 위치를 k-1이라고 가정하고
    # for s in range(N):
    #     for a in range(s+1, N):
    #         if arr[s] == arr[a]: #숫자가 같을 때만
    #             K_num_idx += 1  #1씩 더한다.
    #
    # K_num = arr[K_num_idx]    -> 같은 값이 3개 이상일 때부터 안됨

    # arr_1 = []
    # for i in range(N):
    #     if arr[i] not in arr_1:
    #         arr_1.append(arr[i])
    #
    # K_num = arr_1[K-1]
    # # print(arr_1)
    # print(f'#{test_case} {arr_1[K-1]}')
