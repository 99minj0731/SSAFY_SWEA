import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input()) #3

for test_case in range(1, T+1):

    # N = 화덕의 크기, K = 피자의 개수
    N, K = map(int, input().split())

    # 화덕에 들어갈 피자 리스트
    pizza_list = deque(list(map(int, input().split())))  #[7, 2, 6, 5, 3]

    # 화덕
    oven = deque([0] * N)  #[0, 0, 0]

    # 끝난 피자를 넣을 곳
    fin_pizza_list = [0] * K

    # 피자 위치 확인용 리스트
    pizza_idx = [] #[1, 2, 3, 4, 5]
    for i in range(1, K+1):
        pizza_idx.append(i)

    while len(fin_pizza_list) == K-1:
        pizza_list.popleft()
        oven.append()


    # print(pizza_idx)



'''
필요한 리스트
0. 구워야할 피자 리스트
1. 빈 화덕
2. 피자가 들어간 화덕 -> 필요 없음
3. 피자의 번호를 알려줄 수 있ㅇ는거 (피자 인덱스 확인용)
4. 피자 다 구웠으면 넣을 거

피자 리스트에서 화덕의 크기만큼 빼줌
뺀 피자들 빈 화덕안에 넣음 (자리가 0일 경우)
피자 인덱스 확인용에다가 각각 자리의 번호를 넣음 (????????)
while 문을 돌려서 (언제까지? 화덕에 요소가 1개가 남을 때까지 or 끝난 피자가 전체-1이 됐을때)
한 번 while문을 돌 때마다 //2를 해줌
만약 치즈가 다 녹은 피자가 존재한다면(0이 됐다면)
그 피자 인덱스 확인용 자리랑 비교해서...??
그걸 없애버리고
자리가 빈 오븐(0이 된 자리에) 피자 리스트에서 하나를 뽑아서 그 자리에 넣는다
피자 인덱스 확인용 자리에 남은 1개를 출력

아니면 다 끝난 피자 리스트에다가 그 끝난 피자를 넣고
피자 리스트랑 비교?????????

'''