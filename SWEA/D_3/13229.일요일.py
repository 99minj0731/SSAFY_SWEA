import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = (input())

    if N == 'MON':
        print(f'#{test_case} 6')
    if N == 'TUE':
        print(f'#{test_case} 5')
    if N == 'WED':
        print(f'#{test_case} 4')
    if N == 'THU':
        print(f'#{test_case} 3')
    if N == 'FRI':
        print(f'#{test_case} 2')
    if N == 'SAT':
        print(f'#{test_case} 1')
    if N == 'SUN':
        print(f'#{test_case} 7')
