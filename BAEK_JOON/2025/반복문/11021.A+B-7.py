import sys
sys.stdin = open('input.txt')

'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
'''

T = int(input())

for i in range(1, T + 1) :
    A, B = map(int, input().split())
    result = A + B
    print(f'Case #{i}: {result}')