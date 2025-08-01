import sys
import heapq
# sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
파이썬은 heapq 최소 힙만 제공하기 때문에 최대 힙을 구하려면 음수로 저장을 해야함. 
'''

max_heap = [] #음수로 저장하여 최대 힙처럼 사용
min_heap = []

n = int(input()) #백준이가 말할 정수의 개수 

for _ in range(n) :
    num = int(input())

    # 일단 max_heap에다가 넣기
    heapq.heappush(max_heap, -num)


    # max_heap에서 가장 큰 값이 min_heap에서 가장 작은 값보다 크면 교환하기
    if min_heap and -max_heap[0] > min_heap[0]:

        max_val = -heapq.heappop(max_heap)  #max_heap에서 가장 큰 값
        min_val = heapq.heappop(min_heap)   #min_heap에서 가장 작은 값

        heapq.heappush(max_heap, -min_val) 
        heapq.heappush(min_heap,max_val)


    # max_heap이 min_heap보다 2개 이상 많다면
    if len(max_heap) > len(min_heap) + 1 :
        val = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, val)
    
    print(-max_heap[0])