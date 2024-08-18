import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #3

for test_case in range(1, T+1):
    N = int(input()) #10
    arr = list(map(int,input()))  # [0, 0, 1, 1, 0, 0, 1, 1, 1, 0]

    max_count = 0
    count = 0

    for i in range(N):
        if arr[i] == 1 :
            count += 1
        else:
            if max_count < count:
                max_count = count
            count = 0
    if max_count < count:
        max_count = count


    print(f'#{test_case} {max_count}')


'''
for test_case in range(1, T+1):
    N = int(input()) #10
    arr = input() + '0'  #문자로 받아옴

    max_count = 0
    count = 0

    for i in range(N + 1): #'0'의 값까지
        if arr[i] == '1' : 
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0

    print(f'#{test_case} {max_count}')
'''