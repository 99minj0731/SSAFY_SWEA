# T = input()  #6789, str
# T = int(input()) #6789, int
# T = list(int(input())  #안됨
T = list(input())  # ['6', '7', '8', '9'], list 안에 str으로 저장

sum_num = 0
for i in range(len(T)):  # len(T) = 4
    sum_num += int(T[i])

print(sum_num)