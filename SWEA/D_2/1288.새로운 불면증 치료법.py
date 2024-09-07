import sys
sys.stdin = open('input.txt', 'r')
T = int(input()) #5

for test_case in range(1, T+1):
    N = int(input())    # 1, 2, 11, 1295, 1692

    num_list = []  # 0 ~ 9까지 담을 리스트를 만든다.
    count = 0      # 0 ~ 9까지 모든 숫자를 볼 때까지 몇 번인지
    #count의 값이 결국 i의 값이니까 굳이 count 리스트를 만들지 않아도 됨

    for i in range(1, 1000000):        # 일단 최대한 많이 포문을 돌려서
        if len(num_list) == 10:        # 만약 num_list가 10개 라면
            break                      # 멈추고
        str_num = str(N * i)           # 그 값을 문자열로 바꿔주고
        count += 1                     # 한 번 셀 때마다 count 의 값을 1개씩 늘려준다.
        for num in str_num:            # 해당 숫자를 순회해서
            if num not in num_list:    # 만약 해당 숫자가 num_list에 없다면 넣어준다.
                num_list.append(num)
            #elif 문도 필요 없음
            elif num in num_list:      # 만약 리스트 안에 있다면
                pass
    print(f'#{test_case} {N * count}')




# ''' # 교수님 풀이법
# # while => 반복횟수는 알 수 없지만, 종료 조건은 안다.
# # 초기값 N으로부터 2N, 3N, 4N .......
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     val = 0
#     num_set = set()
#     # 0 ~ 9가 모두 나왔다면 반복 종료
#     while len(num_set) < 10:
#         val += N  # 생성되는 양의 번호
#         # val에서 각 자리값을 추출해서
#         # 이미 나온 숫자인 아닌지 계산 => 여러가지 방법이 가능
#         for num in str(val):
#             num_set.add(num)
#
#     print(f'#{tc} {val}')
# '''



