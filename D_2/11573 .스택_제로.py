T = int(input())

for test_case in range(1, T+1):
    N = int(input())    #크기
    arr = list(map(int, input().split()))   #4 0 2 3 0

# S = [0] * N #저장소를 만들어
# top = -1 #초기값은 빈스택이니까 -1에다가, 마지막에 입력된 값의 인덱스 저장
#
# #push
# for i in range(N):        #크기만큼 돌릴건데
#     if arr[i] != 0:      #0이 아니라면
#         top += 1         #돌 때마다 top에 1를 더하고
#         S[top] = arr[i]
#     else:                 #arr[i] == 0:  #근데 0을 만났어
#         top -= 1     #그럼 top에 -1을 하고
#         # 그 전의 값을 없애야하는데
# #적힌 수들의 합
# sum_num = 0
# for i in range(0, top+1):
#     sum_num += S[i]


#3번 append, pop
S = []   #빈 리스트를 만들고
for i in range(N):
    if arr[i] != 0:        #0이 아니면
        S.append(arr[i])   #리스트에 넣고
    else:        # arr[i] == 0:   #0을 만났으면
        S.pop()  #0을 없애

#적힌 수들의 합
sum_num = 0
for i in range(len(S)):
    sum_num += S[i]

print(f'#{test_case} {sum_num}')