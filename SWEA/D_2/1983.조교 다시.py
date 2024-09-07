import sys
sys.stdin = open('input.txt', 'r')

T = int(input()) #1

for test_case in range(1, T+1):
    stu_num, find_stu_num = map(int,input().split())   #10 #2
    score = [list(map(int, input().split())) for _ in range(stu_num)]

    sum_score = [0] * stu_num   # 학생들의 점수 합산3 평균 리스트, 정렬 안된거
    # [74, 92, 88, 99, 72, 85.8, 96, 68, 85, 85]  #92점 맞은 학생

    for i in range(stu_num):     #학생의 수만큼 반복한다.
        for j in range(3):       #중간고사, 기말고사, 과제
            if j == 0:           #만약 j가 중간고사라면 35%가 들어가야하니까
                sum_score[i] += (score[i][j] * 35 / 100)     #해당 값의 35%를 더해주고
            elif j == 1:         #만약 j가 기말고사라면
                sum_score[i] += (score[i][j] * 45 / 100)     #해당 값의 45%를 더해주고
            else:                #만약 과제라면
                sum_score[i] += (score[i][j] * 20 / 100)     #해당 값의 20%를 더해준다.

    sort_sum_score = [num for num in sum_score]     # 정렬된 리스트
    #[99, 96, 92, 88, 85, 85.7, 85, 74, 72, 68]

    # sum_score 내림차순으로 정렬하기
    for i in range(len(sort_sum_score)-1, 0, -1):   # i = 9, 8, 7, 6, 5, 4, 3, 2, 1
        for j in range(i):                     # j = 0 1 2 3 4 5 6 7 8
            if sort_sum_score[j] < sort_sum_score[j + 1]:
                sort_sum_score[j], sort_sum_score[j + 1] = sort_sum_score[j + 1], sort_sum_score[j]

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    grade_idx = 0
    for i in range(stu_num):  #학생 수 만큼 반복해서
        if sum_score[find_stu_num - 1] == sort_sum_score[i]:   # 92가 i = 3번째, 2번쨰 인덱스에 위치
            grade_idx = i // (stu_num // 10)

    print(f'#{test_case} {grade[grade_idx]}')

