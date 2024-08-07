import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #4
#
# for test_case in range(1, T+1):
#     carrot_num = int(input()) #당근의 갯수
#     arr = list(map(int, input().split())) #[1, 2, 1, 2, 3, 1, 2, 1]
#
#     max_count = 0 # 연속으로 커지는 당근의 갯수
#
#     count = 1 # 연속으로 커지지 않는 경우 1이 나와야 하니까
#
#     for i in range(1, carrot_num): #1번째부터 찾아보면 되니까 1부터 시작
#         if arr[i - 1] + 1 == arr[i]: #앞의 값과 1차이가 난다면
#             count += 1 #카운트에 1 증가
#         else: #만약 아니라면, 값이 줄어들거나 같은경우
#             if max_count < count:
#                  max_count = count
#
#     print(max_count)
#     T = int(input())
#
# for test_case in range(1, T+1):
#     carrot_num = int(input()) # 당근의 갯수
#     arr = list(map(int, input().split())) # [1, 2, 1, 2, 3, 1, 2, 1]
#
#
#     max_count = 0 # 연속으로 커지는 당근의 갯수
#     #
#
#     count = 1 # 연속으로 커지지 않는 경우 1이 나와야 하니까
#     decrease = False
#     #
#
#     for i in range(1, carrot_num): #1번째부터 찾아보면 되니까 1부터 시작
#         if arr[i - 1] < arr[i]: #앞의 값과 1차이가 난다면
#             decrease = False
#             count += 1 #카운트에 1 증가
#         else: #만약 아니라면, 값이 줄어들거나 같은경우
#             decrease = True
#
#     if max_count < count:
#         max_count = count
#         count = 1
# #
#
#     if not decrease: # 한번도 당근 크기가 줄어들지 않은 경우
#         max_count = count
#     #
#
#     print(f'#{test_case}', max_count)
#     T = int(input())  # 4

for test_case in range(1, T + 1):
    carrot_num = int(input())  # 당근의 갯수
    arr = list(map(int, input().split()))  # [1, 2, 1, 2, 3, 1, 2, 1]

    max_count = 1  # 연속으로 커지는 당근의 갯수

    count = 1  # 연속으로 커지지 않는 경우 1이 나와야 하니까

    for i in range(1, carrot_num):  # 1번째부터 찾아보면 되니까 1부터 시작
        if arr[i - 1] < arr[i]:  # 앞의 값과 1차이가 난다면
            count += 1  # 카운트에 1 증가
            if max_count < count:
                max_count = count
        else:  # 만약 아니라면, 값이 줄어들거나 같은경우
            count = 1

    print(f'#{test_case}', max_count)