T = int(input()) #3

for test_case in range(1, T+1):
    arr = list(input())  #리스트에 넣어   #print('{} {}'.format(1, 2))

S = [0] * len(arr)   #스택 생성
top = -1  #-1에다가 초기값 설정

result = True  #일단 맞다고 가정하고

for x in arr:
    if x == '{' or x == '(':     #만약 여는 괄호라면
        top += 1         #top을 위로 한 칸 올리고
        S[top] = x  #top자리에 arr[i]를 넣겠다.
    if x == ')' or x == '}':   #만약 닫는 괄호가 나왔으면
        if S[top] == -1: #닫는 괄호가 있는데 만약 스택이 비었다면
            result = False
            break
        # if x == ')' and S[top] == '(':     #닫는 소괄호고 top이 여는 소괄호라면
        #     top -= 1         # top 한 칸 내려
        # elif x == '}'and S[top] == '{':     #닫는 중괄호고 top이 닫는 중괄호라면
        #     top -= 1      #한 칸 내려
        if x == '}'and S[top] != '{':    #{}같은 종류의 괄호가 아니라면
            result = False
            break
        elif x == ')' and S[top] != '(':  #
            result = False
            break
        top -= 1

if top != -1:  #스택 정상적으로 다 없어지지 않았다면
    result = False


if result:
    print(f'#{test_case} 1')
else:
    print(f'#{test_case} 0')