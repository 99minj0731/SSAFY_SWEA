import sys; sys.stdin = open('input.txt', 'r')
#=================================================


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    H = [0] * (N + 1)
    top = 0
    for val in arr:
        top += 1
        H[top] = val
        c, p = top, top//2
        while p and H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            c, p = p, p//2
    ans = 0
    p = N//2
    while p:
        ans += H[p]
        p //= 2
    # print(f'#{tc} {ans}')
    print(H)