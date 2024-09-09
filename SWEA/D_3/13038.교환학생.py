import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input()) # 2
    arr = [list(map(str, input().split()))]

    # 일단 0이라고 가정
    ans = 0

    print(arr)
    
    # # 출결일수가 0이 될 때까지 반복
    # while N > 0:
    #     for i in arr:
    #         if i == 0:
    #             ans += 1
    #             N -= 1    

    
'''
arr를 순회하면서
N이 0이 될때까지 반복
1 이 나오면 N을 1개 빼주고 ans += 1

'''