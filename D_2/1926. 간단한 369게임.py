import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #100  #숫자로 받고


for i in range(1, T+1):  #1부터 100까지 반복
    num = str(i) # 숫자열 1~100 을 문자열로 바꿔줌, '1', '2' '''' '99', '100'

    count = 0
    for j in num:
        if j == '3' or j == '6' or j == '9':   #3, 6, 9가 있다면
            count += 1

    if count > 0:  #3, 6, 9가 들어갔을 경우
        print('-'*count, end=' ') #카운트의 갯수만큼'-'출력
    else:   #아닌경우 num 출력
        print(num, end=' ')

print(' ',end= '')  #?????

# for i in range(1, int(T)+1):  #1부터 100까지 반복
#     lst.append(i)
#     if '3' or '6' or '9' in str(i):
#         lst.append('-')