import sys
from collections import deque

# sys.stdin = open('input.txt')
N = int(sys.stdin.readline().strip())

people = list(map(int, sys.stdin.readline().split()))
waiting = deque([])
num = 1

while num <= N :

    if not people and waiting:
        if waiting[0] != num:
            break

    if people :
        if people[0] != num:
            if waiting :
                if num == waiting[0]:
                    waiting.popleft()
                    num += 1
                else:
                    if people: 
                        if people[0] == num:
                            people.pop(0)
                            num += 1
                        else:
                            waiting.appendleft(people[0])
                            people.pop(0)
            else:        
                waiting.appendleft(people[0])
                people.pop(0)
        else:
            people.pop(0)
            num += 1
    else:
        if waiting:
            if waiting[0] == num:
                waiting.popleft()
                num += 1



if not people and not waiting :
    print("Nice")
else:
    print("Sad")