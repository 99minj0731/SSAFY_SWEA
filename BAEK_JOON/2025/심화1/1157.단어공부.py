import sys
sys.stdin = open('input.txt')

from collections import Counter

# 아예 이런식으로 받아도됨
word = input().strip().upper()

'''
처음으로 들어오는 알파벳은 소문자로 교체
word = input()
word[0] = word[0].lower() # 타입 에러남. 파이썬의 문자열은 변경불가능하기 떄문에
word = word[0].lower() + word[1:]

list = []

for i in word :
    list.append(i)
'''


# 가장 많이 나온 숫자 고르기 
# result = max(set(list), key = list.count)

# 빈도수 계산하기
counter = Counter(word) # Counter({'I': 4, 'S': 4, 'M': 1, 'P': 1})

#정렬된 결과 확인하기
most_common = counter.most_common() #[('I', 4), ('S', 4), ('M', 1), ('P', 1)]
max_count = most_common[0][1] # 4

# 가장 많이 등장한 알파벳이 1개인지 2개인지 확인
'''
C = []  # 빈 리스트를 먼저 만든다

for i, count in most_common:  # most_common 리스트를 하나씩 순회하며
    if count == max_count:    # 등장 횟수가 max_count와 같으면
        C.append(i)    
'''
C = [i for i, count in most_common if count == max_count]  # ['I', 'S']

# 만약 1개인지 2개인지 확인
if len(C) == 1:
    print(C[0])
else: 
    print("?")
    