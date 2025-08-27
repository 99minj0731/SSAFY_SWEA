import sys
sys.stdin = open('input.txt')


a, b, c, d, e, f = map(int, input().split())

denom = a*e - b*d   # 분모 (0이 아님이 보장됨)

x = (c*e - b*f) / denom
y = (a*f - c*d) / denom

print(int(x), int(y))


# a, b, c, d, e, f, x, y = a*d, b*d, c*d, d*a, e*a, f*a, 1, 1

# # y를 구해. 그런데 만약 a, d가 둘 다 양수라면 빼고, 아니면 더해
# if a > 0 and d > 0 :
#     y = (c-f) / (b-e)
#     x = (c - (b * y)) / a 
# else: 
#     y = (c+f) / (b+e)
#     x = (c - (b * y)) / a 

# print(int(x), int(y))




