import sys
sys.stdin = open('input.txt')

def deliver(truck):
    global w

    # 아무것도 없는 트럭이 있을 수 있으니 기본 값을 먼저 0으로 가정
    ans = 0

    # 트럭이 현재 옮길 수 있는 화물들만 리스트에 담는다.
    container_list = [x for x in w if x <= truck]

    # 만약 옮길 수 있는 화물이 있다면
    if container_list:
        # 그 중 가장 큰 값을 저장
        deliver_container = max(container_list)
        # 큰 값의 위치를 구하고
        delivered_idx = w.index(deliver_container)
        # 화물 리스트에서 없애준다.
        w.pop(delivered_idx)
        ans = deliver_container
    return ans


T = int(input())

for test_case in range(1, T + 1):

    # N = 컨테이너 수, M = 트럭 수
    N, M = map(int, input().split())    # 5 10

    # 컨테이너 화물의 무게
    w = list(map(int, input().split()))  # [2, 12, 13, 11, 18]

    # 트럭이 옮길 수 있는 양
    t = list(map(int, input().split()))  # [17, 4, 7, 20, 3, 9, 7, 9, 20, 5]

    # 옮겨진 화물의 무게
    max_deliver = 0

    # 트럭을 하나씩 빼서 비교
    for i in t:
        max_deliver += deliver(i)


    print(f'#{test_case} {max_deliver}')

