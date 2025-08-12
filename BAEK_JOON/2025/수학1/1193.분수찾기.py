'''
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.

X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오
'''

import sys
sys.stdin = open('input.txt')

# 1 -> 2 -> 3 -> 4 -> 5-> ...

N = int(input())
line = 1 # 현재 대각선 번호
count = 1

while count < N:
    line += 1
    count += line


# 몇 번째에 있는지 찾기.
fine_index = count - N

# 근데 홀수일 경우에는 위부터 0시작, 짝수일 경우에는 아래부터 0시작

# 만약 홀수라면
if line % 2 == 1:
    left_number = fine_index + 1
    right_number = line - fine_index
    print(f'{left_number}/{right_number}')
else : 
    left_number = line - fine_index
    right_number = fine_index + 1
    print(f'{left_number}/{right_number}')

