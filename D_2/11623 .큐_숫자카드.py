import sys
sys.stdin = open('input.txt', 'r')


'''
T = int(input())

for test_case in range(1, T+1):
    N = int(input())  # 4
    Q = []            # 빈 리스트를 만들어줌
    rear = -1

    for i in range(1, N + 1):   # i = 1, 2, 3, 4
        Q.append(i)

    # Q = [0] * N  # [0, 0, 0, 0]
    # for i in range(1, N+1):           # i = 1, 2, 3, 4
    #     rear = (rear + 1) % N         # rear의 값을 바꿔줌
    #     Q[rear] = i                       # Q = [1, 2, 3, 4]

    while N > 1:           #N의 값이 1 보다 클 때까지 반복
        Q.pop(0)           # [2, 3, 4]
        N -= 1             # N = 3 ... 2... 1...
        Q += [Q.pop(0)]   # [3, 4, 2]
    print(f'#{test_case} {Q[0]}')
'''


from collections import deque

T = int(input())  #3

for tese_case in range(1, T + 1):
    N = int(input())    #4
    arr = list(range(1, N + 1))   # arr = [1, 2, 3, 4]
    cards = deque(arr)
    # print(arr)

    for i in range(len(cards) - 1):     # i = 0, 1, 2
        cards.popleft()                 # 위에 위치한 값을 빼고
        cards.append(cards.popleft())   # 뻬고 난 후 제일 위에 위치한 값을 맨 아래로 이동시킨다.

    print(f'#{tese_case}', *cards)
