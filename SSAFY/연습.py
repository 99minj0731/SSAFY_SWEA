ans = [4, 7, 15, 14]

answer = ''

for i in ans:
    result = ''
    for j in range(4):  # 각 문자당 4자리를 만들어야 하니까 4번 반복

        # 0 이 되면 앞에 계속 0을 붙힘
        if i == 0:
            result = '0' + result
        # 나머지가 0일 경우
        elif i % 2 == 0:
            result = '0' + result
            i = i // 2
        # 나머지가 1일 경우
        elif i % 2 == 1:
            result = '1' + result
            i = i // 2
    answer = answer + result

print(answer)