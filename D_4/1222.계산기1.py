import sys
sys.stdin = open('input.txt', 'r')


def postfix(numbers):
    stack = [0] * len(numbers)  #일단 빈 스택을 만들고
    top = -1  #일단 top을 지하에다가 저장
    result1 = []  #후위 계산식

    for token in arr:  # 리스트에서 토큰을 하나씩 뽑아서
        if token == '+':  #만약 토큰이 연산자 + 라면
            # if top >= 0:   #만약 스택 안에 연산자가 있다면
            while top > -1: #스택 안에 아무것도 남지 않을 때까지
                result1.append(stack[top])  #그 값을  result 에 넣어준다.
                top -= 1  # 탑을 하나 내려주고
            # else: #만약 빈 스택이라면
            top += 1 #탑을 하나 올려주고
            stack[top] = token  #그 곳에다가 해당 토큰을 넣어준다.
        else:  #token.isdigit(): # 만약 토큰이 피연산자 숫자라면
            result1.append(token) #후위 계산식에 그 토큰 값을 넣어준다.

    return result1

def postfix_2(nums):   #후위 계산식을 계산하는 함수
    stack2 = [0] * len(nums)
    top = -1 #일단 top의 위치를 -1로 해놓고

    for token in nums:
        if token == '+':     #'+'가 나온다면
            right_num = stack2[top] #오른쪽 숫자를 현재 탑에있는 걸로하고
            top -= 1   #탑 하나 내리고
            left_num = stack2[top]  #왼쪽 숫자를 현재 탑에있는 거
            top -= 1   #탑 하나 내려
            stack2[top] = right_num + left_num #그리구 거기에 두 값의 합을 넣어준다
        else:   # 스트링이지만 숫자인척하는 애들이 나온다면
            top += 1  #탑을 하나 올리고
            stack2[top] = token

    return stack2[0]




for test_case in range(10):
    N = int(input())  # 101
    arr = list(input())  # ['9', '+', '8', '+', '5'...'6', '+', '6']

    cal_change = postfix(arr)
    sum_result = postfix_2(cal_change)

    print(sum_result)




