import sys
sys.stdin = open('../input.txt', 'r')

T = int(input()) #1

for test_case in range(1, T+1):
    stu_num, find_stu_num = map(int,input().split())   #10 #2
    score = [list(map(int, input().split())) for _ in range(stu_num)]
    # print(stu_num)
    # print(score) #[[87, 59, 88], [99, 94, 78]... [98, 84, 67], [85, 84, 91]]

    sum_score = [0] * stu_num   # 학생들의 점수 합산 평균 리스트, 정렬 안된거

    for i in range(stu_num):     #학생의 수만큼 반복한다.
        for j in range(3):       #중간고사, 기말고사, 과제
            if j == 0:           #만약 j가 중간고사라면 35%가 들어가야하니까
                sum_score[i] += (score[i][j] * 35 / 100)     #해당 값의 35%를 더해주고
            elif j == 1:         #만약 j가 기말고사라면
                sum_score[i] += (score[i][j] * 45 / 100)     #해당 값의 45%를 더해주고
            else:                #만약 과제라면
                sum_score[i] += (score[i][j] * 20 / 100)     #해당 값의 20%를 더해준다.
            # 이 for문은 한 줄로 간단하게 표현 가능

    # print(sum_score) [75, 93, 89, 100, 72, 86, 96, 69, 85, 86] 이건 round 쓴거

    sort_sum_score = [num for num in sum_score]     # 정렬된 리스트인데 깊은 복사해서 위에 리스트가 바뀌지 않도록

    # sum_score 내림차순으로 정렬하기
    for i in range(len(sort_sum_score)-1, 0, -1):     # i = 9, 8, 7, 6, 5, 4, 3, 2, 1
        for j in range(i):                            # j = 0 1 2 3 4 5 6 7 8
            if sort_sum_score[j] < sort_sum_score[j + 1]:
                sort_sum_score[j], sort_sum_score[j + 1] = sort_sum_score[j + 1], sort_sum_score[j]

    # print(sort_sum_score)  #[99.45, 96.25, 92.54, 88.8, 85.85, 85.75, 85.5, 74.6, 72.35, 68.95]

    #학점 리스트
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    grade_idx = 0                                              #일단 0이라고 가정하고
    for i in range(stu_num):                                   #학생 수 만큼 반복해서
        #만약 정렬되지 않은 리스트에서 찾고자 하는 학생의 점수와 / 정렬된 리스트에서 i인덱스에 위치한 값이 같다면
        if sum_score[find_stu_num - 1] == sort_sum_score[i]:
            grade_idx = i // (stu_num // 10)                   #학생의 10%만 부여해야하니까

    print(f'#{test_case} {grade[grade_idx]}')











 # 정렬하기 전의 숫자를 기억할 것
 # total _ score  계산 시점에 저장을 해놓고 num_to_find  = total_score[K-1]라고 저장
 # 정렬 후에 저장한 수가 몇 번째에 저장되어 있는지 찾아볼 것
 # 정렬 후 몇 번째에 있음.

 # 인덱스를 총 갯수를 10으로 나는 구간으로 나누어 몫을 구한다.
 # grade 리스트 안에
 #grade 인덱스는 3번재 줄에서 구한 index// (N//10)









