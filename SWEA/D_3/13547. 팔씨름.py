import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    fight = input()
    N = 7
    count = 0

    for i in fight:
        if i == 'x':
            count += 1

    if count > N:
        print(f'#{test_case} NO')
    else:
        print(f'#{test_case} YES')
