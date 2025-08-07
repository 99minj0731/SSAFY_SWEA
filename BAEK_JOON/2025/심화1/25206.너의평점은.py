'''
치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
과연 치훈이는 무사히 졸업할 수 있을까?
20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
치훈이의 전공평점을 출력한다.
정답과의 절대오차 또는 상대오차가 
\(10^{-4}\) 이하이면 정답으로 인정한다.
'''

import sys
sys.stdin = open('input.txt')

# 일단 학점 표를 만들자
score = dict([("A+", 4.5), ("A0", 4.0), ("B+", 3.5), ("B0", 3.0), ("C+", 2.5), ("C0", 2.0), ("D+", 1.5), ("D0", 1.0), ("F", 0.0) ])

'''
score = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0
}
'''
sum_credit = 0
sum_score = 0

while True:
    try:
        subject, credit, grade = map(str, map(str,input().split()))
        # 만약 P/F 과목이라면 계산에서 제외한다. 
        if grade != "P":
            sum_credit += int(float(credit))
            # sum_score += (int(float(credit))) * (int(float(score[grade]))) # 이렇게 할 경우 뒤에 소수가 짤림
            sum_score += float(credit) * float(score[grade])

    except EOFError:
        break

print(sum_score / sum_credit)