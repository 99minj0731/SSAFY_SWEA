import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_cast in range(1, T+1):
    arr = list(input())  #['K', 'O', 'R', 'E', 'A', ....'K', 'O', 'R', 'E', 'A']
    pattern = []         #빈 리스트를 만들어주고

    for i in range(1, len(arr)):  #1번부터 시작하는건 슬라이싱할 때 그 전까지만 하니까
        pattern = arr[:i]         #계속 갱신해서 넣어줄건데
        if arr[i:i+len(pattern)] == pattern:    #만약 그 시작 점부터 시작점 + 패턴까지의 문자가 패턴과 일치하다면
            print(f'#{test_cast} {len(pattern)}') #출력하고
            break  #멈추겠다.



# for test_case in range(1, T+1):
#     arr = list(input())
#     pattern = []
#     for i in range(1, len(arr)):
#         pattern.append(arr[:i])  #append면 갱신하는게 아니라 계속 1, 2, 3, 이렇게 들어감
#         if arr[i : i + len(pattern)] == pattern :
#             print(f'#{test_case} {len(pattern)}')
#             break















