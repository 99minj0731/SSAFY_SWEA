'''
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다
'''

import sys
sys.stdin = open('input.txt')

N = int(input())

numbers = list(map(int, input().split()))

sorted_numbers = sorted(set(numbers))

my_dic = {} # {-10: 0, -9: 1, 2: 2, 4: 3}
result = []

for numberSet in enumerate(sorted_numbers):
    i, v = numberSet
    my_dic[v] = i
    # print(i, v)

# result = [my_dic[i] for i in numbers]

for i in numbers :
    result.append(my_dic[i])

print(*result)

# 시간초과
# for i in numbers :
#     result.append(sorted_numbers.index(i))
