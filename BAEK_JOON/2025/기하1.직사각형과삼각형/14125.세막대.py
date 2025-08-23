'''
영선이는 길이가 a, b, c인 세 막대를 가지고 있고, 각 막대의 길이를 마음대로 줄일 수 있다.

영선이는 세 막대를 이용해서 아래 조건을 만족하는 삼각형을 만들려고 한다.

각 막대의 길이는 양의 정수이다
세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
삼각형의 둘레를 최대로 해야 한다.
a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램을 작성하시오. 

첫째 줄에 a, b, c (1 ≤ a, b, c ≤ 100)가 주어진다.

첫째 줄에 만들 수 있는 가장 큰 삼각형의 둘레를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

slides = sorted(map(int, input().split()))
a, b, c = slides

if a + b > c :
    print(a+b+c)
else:
    c = a + b - 1
    print(a+b+c)

# num_list = list(map(int, input().split()))

# '''
# 가장 큰 값을 찾고, 큰 값을 (나머지값 합친거)에 루트씌운 후 반올림 한 것으로 교체. 
# '''
# max_side = max(num_list)
# num_list.remove(max_side)
# sum_both_side = 0

# for i in range(2):
#     sum_both_side += num_list[i]

# new_max_side = sum_both_side ** 0.5
# result = new_max_side + sum_both_side

# # 만약 소수일 경우 반올림한다. 
# if result == int(result) :
#     print(int(result))
# else:
#     print(int(result + 1))