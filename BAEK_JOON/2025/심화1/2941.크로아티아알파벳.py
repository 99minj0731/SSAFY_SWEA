import sys
sys.stdin = open('input.txt')

word = input()

#일단 크로아티아 알파벳을 저장
# 주의해야할 점: dz=을 z=보다 더 먼저 처리해야함
croatian = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatian:
    word = word.replace(i, "*")

print(len(word))