'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''
import sys
sys.stdin = open('input.txt')

result_X = []
result_Y = []

for i in range(3):
    X, Y = map(int, input().split())

    # 만약 리스트 안에 없으면 넣고, 있으면 없애자
    if X not in result_X : 
        result_X.append(X)
    else : 
        result_X.remove(X)
    
    if Y not in result_Y :
        result_Y.append(Y)
    else :
        result_Y.remove(Y)

print(*result_X, *result_Y)
