T = list(input())  # ['A', 'B', 'C', 'D', 'E', 'F'

num = []
for i in range(len(T)):
    num.append(ord(T[i]) - 64)     #A=65, B=66 '''

print(*num)