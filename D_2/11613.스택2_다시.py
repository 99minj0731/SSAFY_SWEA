import sys
sys.stdin = open('input.txt', 'r')

def calcul(numbers):
    stack = [0] * len(numbers)  #빈 스택을 만들고
    top = -1     #top을 일단 지하에 저장

    for token in numbers:   #numbers에서 하나씩 빼서 확인을 할거다.
        if token == '.':    #만약 '.'이 나온다면
            break           #멈추고
        elif token.isdigit():  #만약에 토큰이 숫자라면
            top += 1  #탑을 하나 올리고
            stack[top] = int(token)  #top에다가 그 값을 넣어줄건데 숫자니까 int로 넣어주고
        else:      #연산자가 나왔어 그러면
            if top < 1: #근데 계산하려고 했는데 남은 숫자가 1개 이하야
                return 'error'
            num1 = stack[top-1]   #현재 탑 앞에 있는 번호
            num2 = stack[top]       #현재 탑에 있는 번호
            top -= 1                #top을 하나 내려서 거기다가 뭘 넣을거냐면
            if token == '-':
                stack[top] = num1 - num2
            elif token == '/':
                stack[top] = num1 // num2
            elif token == '+':
                stack[top] = num1 + num2
            else:
                stack[top] = num1 * num2

    if top > 0:   #계산을 다 끝냈는데 스택이 -1이 아니야
        return 'error'

    return stack[top]



T = int(input())  #3


for test_case in range(1, T+1):
    nums = input().split()   #['10', '2', '+', '3', '4', '+', '*', '.']
    result = calcul(nums)

    print(f'#{test_case} {result}')
