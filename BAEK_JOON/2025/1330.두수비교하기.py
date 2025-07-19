import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readlines

First_input, Second_input = map(int,input().split())

if First_input > Second_input :
    print(">")
elif First_input < Second_input :
    print("<")
else : print("==")