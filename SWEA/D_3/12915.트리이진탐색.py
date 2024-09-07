import sys
sys.stdin = open('input.txt')



def subtree(n):
    global cnt
    if n > N:  #범위 밖을 넘어감
        return

    subtree(n * 2)    # 왼쪽 자식으로 이동
    arr[n] = cnt      # 왼쪽 자식 다 봤으면 그 자리에 1 부터 넣기
    cnt += 1          # 다음부터는 2를 넣을거다.
    subtree(n*2 + 1)  # 오른쪽 자식


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())     #6
    arr = [0] * (N + 1)  # [0,0,0,0,0,0,0] -> [0, 4, 2, 6, 1, 3, 5]
    cnt = 1

    subtree(1)

    a = arr[1]
    b = arr[N//2]

    print(f'#{test_case} {a} {b}')

