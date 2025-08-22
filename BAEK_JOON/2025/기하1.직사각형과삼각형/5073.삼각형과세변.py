'''
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우

단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

입력
각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.

출력
각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.

'''

import sys
sys.stdin = open("input.txt")

last_testcase = True

while last_testcase :
    
    N, M, K = map(int,input().split())

    if N == 0 and M == 0 and K == 0 : 
        last_testcase = False
    
    else: 
        long_side = max(N, M, K)
        short_side = 0

        numberList = [N, M, K]
        numberList.remove(long_side)

        for i in range(2):
            short_side += numberList[i]

        

        if short_side > long_side :
            if N == M == K :
                print("Equilateral")
            
            # 한 변이라도 다른 길이가 있을 경우
            else:
                if long_side in numberList or numberList[0] == numberList[1] :
                    print("Isosceles")
                    
                else: print("Scalene")

        #만약 두 변의 합이 제일 긴 변보다 짧다면 invalid
        else : 
            print("Invalid")

