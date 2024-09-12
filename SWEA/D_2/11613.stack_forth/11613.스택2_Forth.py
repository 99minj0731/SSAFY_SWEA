import sys
sys.stdin = open('../input.txt', 'r')

def calculator(numbers):       #함수를 만들고
    S = [0] * len(numbers)     # 이것은 스택인데 연산코드의 길이만큼으로 만들어 줬다
    top = -1                   # top은 일단 지하에다가 넣고

    for token in numbers:      #numbers에서 하나씩 빼올건데
        if token == '.':       # '.'이 나오면 숫자를 꺼내 출력해야하니까
            break
        elif token.isdigit():  #토큰이 숫자라면
            top += 1           #탑을 하나 올리고
            S[top] = token     #S의 탑 위치에 현재 숫자를 넣는다
        else:                  #연산자일 경우
            if top < 1:        #top이 만약 1개밖에 없으면 연산이 안되니까
                return 'error'
            top -= 2           #연산할 때 2개가 필요하니까 top 2개 내리구
            n1 = int(S[top+1]) #앞에올 숫자는 top 위에오는 숫자이고
            n2 = int(S[top+2]) #뒤에 올 숫자는 top 위위에 있는 숫자로해서
            if token == '-':
                cal_num = n1 - n2
            elif token == '+':
                cal_num = n1 + n2
            elif token == '/':
                cal_num = n1 // n2
            else:  # token == '*':
                cal_num = n1 * n2
            top += 1          #그리구 탑을 하나 올려주고
            S[top] = cal_num  #top위치에다가 연산한 값을 넣어줍시다.

    if top > 0:      #연산 다 끝냈는데 스택안에 뭐가 남아있으면
        return 'error'

    return S[0]   #마지막으로 연산 다 끝내구 0번째에 있는 값이 최종 답이다!

T = int(input())

for test_case in range(1, T+1):
    arr = input().split()                      #['10', '2', '+', '3', '4', '+', '*', '.'] type(list) 안에 str
    # arr = list(input().split())              #['10', '2', '+', '3', '4', '+', '*', '.'] type(list)
    # arr = list(input().split()))   #['10', '2', '+', '3', '4', '+', '*', '.'] type(list)
    result = calculator(arr)

    print(f'#{test_case} {result}')

    # print(type(arr[3]))