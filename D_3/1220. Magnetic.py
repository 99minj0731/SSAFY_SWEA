import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    # 1 = N극, 2 = S극, 위에 N극, 아래 S극

    N = int(input())  # 항상 100
    arr = [list(map(int, input().split()))for _ in range(N)]


    result = 0

    # 열우선 순회
    for i in range(100):
        find_n = 0  # 위에 n극이 있나없나 확인하는 용
        for j in range(100):
            if arr[j][i] == 1:  # 만약 N극을 만났다.
                find_n = 1      # 위에 N이 있다고 만들어 놓고
            elif arr[j][i] == 2 and find_n == 1:   #만약 위에 N극이 있고 현재 위치에 S극이 있다.
                result += 1    # 교착상태에 1을 추가하고
                find_n = 0     # 확인용을 다시 0으로 리셋해놓는다

    print(f'#{test_case} {result}')



'''
1. 열 우선 순회
2. np = 0
3. 1을 만났는데(np=1) 2를 만났어 그럼 교착상태에 1을 추가후 np=0으로 리셋
4. 1은 아래로 탐색, 2는 위로 탐색 
'''