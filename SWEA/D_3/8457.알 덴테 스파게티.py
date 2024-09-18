import sys
sys.stdin = open('input.txt', 'r')

def pasta(cur_sec, count): #cur_sec = 현재 초수, count = 횟수
    global ans

    # 가지치기
    # 1. 만약 count가 ans보다 더 크다면 종료
    # 2. 현재 초수가 오차범위를 벗어났을 경우 종료
    if count > ans or cur_sec > B + E:
        return

    # 오차 범위 안에 들어왔다면 종료
    if B - E <= cur_sec <= B + E:
        if count < ans:
            ans = count
        return

    for i in arr: # i = 3, 4
        pasta(cur_sec+i, count + 1)


T = int(input())

for test_case in range(1, T + 1):
    # N:모래시계 개수, B:이상적인 초 E:오차 허용 범위
    N, B, E = map(int, input().split()) # 2 10 2
    # 모래시계 초 list
    arr = list(map(int, input().split())) # 3 4

    ans = 1e9

    pasta(0,0)

    if ans == 1e9:
        ans = 0

    print(f'#{test_case} {ans}')
'''
B에서 E를 빼고 더한 수를 저장(범위 생성)
result 값 생성 후 더 낮은 횟수가 최종이 될거임
arr를 모두 곱하면서 돌아서 while 문으로 범위 안에 들 때까지 
만약 범위 밖으로 벗어난다면 break
'''

# for i in range(len(arr)):  # i = 0, 1
#     clock = arr[i]
#     while arr[i] <= B - E:  # 3 <= 8
#         i = arr[i] * cnt
#         cnt += 1
#         pre_result += 1
#         # 오차 범위 안에 있는지 확인
#         if B-E <= i <= B+E:
#             cnt = 0
#             if pre_result < ans:
#                 ans = pre_result
#                 pre_result = 0
#             break
#         # 만약 오차 범위 밖으로 넘어갔다면 다 초기화
#         if B + E < i:
#             ans = 0
#             cnt = 0
#             break
