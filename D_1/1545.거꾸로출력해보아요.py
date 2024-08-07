import sys
sys.stdin = open("input.txt", "r")

T = int(input()) #8

# #for문 사용
# arr = []
# for i in range(0, T + 1):
#     arr.append(i)
# result = arr[::-1]
# print(*result)

#while문 사용
arr = []
while 0 <= T:
    num = T
    T -= 1
    arr.append(num)

print(*arr)



