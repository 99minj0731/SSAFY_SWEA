import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #1

for test_case in range(1, T+1):
    stu_num, find_stu_num = map(int,input().split())   #10 #2
    score = [list(map(int, input().split())) for _ in range(stu_num)]
    # print(stu_num)
    # print(score) #[[87, 59, 88], [99, 94, 78]... [98, 84, 67], [85, 84, 91]]

    sum_score = [0] * stu_num   # 학생들의 점수 합산 평균 리스트

    for i in range(stu_num):     #학생의 수만큼 반복한다.
        for j in range(3):       #중간고사, 기말고사, 과제
            if j == 0:           #만약 j가 중간고사라면 35%가 들어가야하니까
                sum_score[i] += (score[i][j] * 35 / 100)     #해당 값의 35%를 더해주고
            elif j == 1:         #만약 j가 기말고사라면
                sum_score[i] += (score[i][j] * 45 / 100)     #해당 값의 45%를 더해주고
            else:                #만약 과제라면
                sum_score[i] += (score[i][j] * 20 / 100)     #해당 값의 20%를 더해준다.

    # print(sum_score) #[75, 93, 89, 100, 72, 86, 96, 69, 85, 86]

    # sum_score 정렬하기
    for i in range(len(sum_score)-1, 0, -1):   # i = 9, 8, 7, 6, 5, 4, 3, 2, 1
        for j in range(i):                     # j = 0 1 2 3 4 5 6 7 8
            if sum_score[j] > sum_score[j + 1]:
                sum_score[j], sum_score[j + 1] = sum_score[j + 1], sum_score[j]

    # print(sum_score)  #[69, 72, 75, 85, 86, 86, 89, 93, 96, 100]

    #k번째 학생 인덱스 구하기
    #오또케,,,,?









