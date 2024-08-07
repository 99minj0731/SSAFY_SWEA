import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))

    max_num = arr[0]  # 일단 0번째 수를 가장 큰 수라고 가정
    for i in range(10):
        if max_num < arr[i]:  # 뒤의 값이 더 크다면 그 값으로 변경
            max_num = arr[i]

    print(f'#{test_case} {max_num}')