import sys
sys.stdin = open('input.txt', 'r')


from collections import deque

T = int(input()) #3

for test_case in range(1, T+1):
    N, rotation_num = map(int, input().split())   # 숫자의 갯수, 회전 수 3, 10
    numbers = list(map(int, input().split()))     # 숫자 배열 [5527 731 31274]
    arr = deque(numbers)

    while rotation_num > 0:        # 0보다 클 때까지만 반복
        arr.append(arr.popleft())   #
        rotation_num -= 1

    print(f'#{test_case} {arr[0]}')




    '''
    # print(N, rotation_num)

    front = 0    #front 는 empty 상태와 포화 상태를 구분하기 위해 빈자리로 둔다.
    near = 0
    Q = [0] * N

    # for i in range(N):  # 0번부터 9번까지
    #     near = (near + 1) % N  # 0번째가 아닌 1번째부터 채워짐 [] 1번, 2번, 0번 반복해서 돈다.
    #     Q[near] = numbers[i]
    # # print(Q) #[31274, 5527, 731]

    for i in range(rotation_num):  # 0번부터 9번까지
        near = (near + 1) % N  # 0번째가 아닌 1번째부터 채워짐 [] 1번, 2번, 0번 반복해서 돈다.
    '''
