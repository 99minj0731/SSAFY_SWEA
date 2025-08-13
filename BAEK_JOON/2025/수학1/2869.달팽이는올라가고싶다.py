'''
땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
'''

import sys
sys.stdin = open('input.txt')

A, B, V = map(int,input().split())

# 일단 마지막 날에는 내려가지 않으니 마지막 날을 제외하면 A-B만큼 올라가는 것임.

goup = A-B

day = (V-A + goup -1) // goup + 1
print(day)


'''
# 시간초과 나는 코드
Distance = 0
day = 1

while Distance <= V :
    Distance += A
    if Distance >= V :
        break
    else:
        day += 1
        Distance -= B
    
print(day)

'''