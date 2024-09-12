import sys
sys.stdin = open('input.txt')

def combi(n):
    global min_num, max_num

    for i in range(N): # i = 0, 1, 2, 3, 4, 5
        for j in range(i + 1, N):  # j = 1, 2, 3, 4

            # 하나씩 차례대로 바꾼다.
            n[i], n[j] = n[j], n[i]
            # 만약 앞자리 수가 0이라면
            if n[0] == '0':
                n[i], n[j] = n[j], n[i]
            else:
                # 리스트를 묶고
                new_number = int(''.join(number))

                # 최대값, 최소값 찾기
                if new_number > max_num:
                    max_num = new_number
                if new_number < min_num:
                    min_num = new_number
                # 다시 원상태로 바꿔준다.
                n[i], n[j] = n[j], n[i]


T = int(input())

for test_case in range(1, T + 1):
    number = list(input()) # type str  ['1', '2', '3', '4', '5']
    N = len(number) # 5

    min_num = int(''.join(number))
    max_num = int(''.join(number))

    combi(number)

    print(f'#{test_case} {min_num} {max_num}')

