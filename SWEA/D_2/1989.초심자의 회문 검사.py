import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    arr = list(input())

    result = 1                       #일단 다 맞다고 가정하고

    for i in range(len(arr)//2+1) :  # arr 원소의 처음부터 가운데까지 돌거다.
        if arr[i] == arr[-(1+i)]:    # i번째랑 N- i번째랑 값이 똑같다면 continue
            continue
        else:                        # 만약 다르면
            result = 0               # False로 바꾼다.
            break                    # 그리고 중단

    print(f'#{test_case} {result}')  # else에 걸리지 않는 다면 1출력

