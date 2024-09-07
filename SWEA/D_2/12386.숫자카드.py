import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    # 문자 개수
    N = int(input())  # 5
    # arr = input()   # 49679
    arr = list(input())  #['4', '9', '6', '7', '9'] type=str

    # 카드가 몇 개인지 확인 할 리스트 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    counts = [0] * 10

    for i in range(N):  # 0, 1, 2, 3, 4
        counts[int(arr[i])] += 1  #[0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # counts = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    max_card_num = 0
    max_card_idx = 0

    for i in range(10):
        if max_card_num <= counts[i]:
            max_card_num = counts[i]
            max_card_idx = i

    print(f'#{test_case} {max_card_idx} {max_card_num} ')

'''
1. 카드 개수만큼 반복해서
2. A 리스트에 해당 값 자리에 += 1 ex. [1, 2, 0, 3, 2, 1]
3. A 리스트에서 최댓값 구하기 = 3
4. 해당 인덱스 구하기 = 4
5. 만약 장수가 같다면 -> 최댓값을 구할 때 > 말고 >= 사용
'''