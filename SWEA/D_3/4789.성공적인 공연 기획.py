import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    arr = input()  #09 110011

    # 처음부터 박수치고 있는 사람의 수
    clap = int(arr[0])
    hire = 0

    # 1. arr의  1번째 인덱스부터 탐색한다.
    for i in range(1, len(arr)):
        if arr[i] == '0':
            continue
        # 2. 만약 i-1 이 clap 보다 크다면
        if i > clap:
            hire += i - clap
            clap += i - clap + int(arr[i])

        else:
            clap += int(arr[i])

    print(f'#{test_case} {hire}')




'''
1. arr를 1번째 인덱스 부터 N -1까지 순회를 돌면서
2. 만약 현재 박수치고 있는 사람을 0번째 숫자(clap)만큼이라고 하고
3. 만약 i 번째의 숫자-1이 clap 보다 같거나 크다면 해당 i 번째 숫자를 clap에 더해줌
4. 만약 i 번째의 숫자-1이 clap보다 작다면 i 번째 - clap의 수를 clap에 더해줌
'''



