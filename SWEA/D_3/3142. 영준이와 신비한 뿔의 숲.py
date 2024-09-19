import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N = 뿔의 개수, M = 동물의 수
    N, M = map(int, input().split()) # 7 5

    twin = 0

    # 뿔의 개수가 동물의 수와 같아진다면 끝
    while N > M :
        twin += 1
        N -= 2
        M -= 1

    print(f'#{test_case} {N} {twin}')

'''
만약 뿔의 개수가 7이고 동물의 개수가 5다.
트윈혼부터 계산해서 (뿔 2개)
트윈혼에다가 += 1씩 할 때마다 뿔의 개수를 -= 2, 동물의 개수 -= 1
만약 뿔의 개수와 동물의 개수가 같아진다면 
유니콘의 수는 현재 뿔의개수(동물의수)이다. 
'''