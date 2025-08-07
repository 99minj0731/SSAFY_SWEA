'''
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

result = 0

for i in range(T):
    word = input()
    len_word = len(word)

    word_list = []

    for j in range(len_word):

        if word[j] not in word_list:
            word_list.append(word[j])
            # 만약 마지막 단어라면 그룹단어이다. 
            if j == len_word -1 :
                result += 1

        # 만약에 이전에 나왔던 알파벳이라면 한 번 더 체크
        elif word[j] in word_list:
            # 만약 그 바로 전에 나온 알파벳이라면
            if word[j] == word[j-1] : 
                # 만약 마지막 알파벳이라면 그룹단어이다. 
                if j == len_word-1 :
                    result += 1
                pass
            else: 
                break
            
print(result)