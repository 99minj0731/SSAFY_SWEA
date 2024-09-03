import sys
sys.stdin = open('input.txt')

def prize(cards, n):
    if n == 0:
        return cards

    visited = [0] * len(cards)

    # 가장 큰 값을 찾음
    max_num = 0
    for i in cards:
        if max_num < int(i):
            max_num = int(i)

    max_card_idx = cards.index(max_num)
    change_card_idx = 0
    for i in visited:
        if visited[i] == 0:
            change_card_idx = visited[i]
        else:
            continue

    cards[max_card_idx], cards[change_card_idx] = cards[change_card_idx], cards[max_card_idx]
    n -= 1


# 만약에 제일 큰 숫자가 여러개라면 뒤집는 횟수가 n일 경우, 제일 큰 숫자 뒤에서 n번째의 값을
# 맨 앞이랑 바꿔줌


T = int(input())
for test_case in range(1, T + 1):
    arr, N = map(int, input().split())  #757148
    arr = list(str(arr))

    prize(arr, N)



