import sys
sys.stdin = open('input.txt')

'''
KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.

또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.

훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
'''

H, M = map(int, input().split())
T = int(input())

# 일단 시간을 더하고 60으로 나눠서 몫을 H에다가 더한다. 
M = M + T

#만약 new_M이 60을 넘는다면 시간에다가 60으로 나는 몫을 H에다가 더하자. 
if 60 <= M :
    H = H + (M // 60)
    M = M % 60

    # 만약 자정을 넘어가는 시간이라면
    if 24 <= H :
        H = H - 24

    print(H, M) 

# 만약 60이 넘지 않는다면 바로 출력
else : print(H, M)
