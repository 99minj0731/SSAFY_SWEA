import sys
sys.stdin = open('input.txt', 'r')

def find_minsum(i, N, sum_ij):

    global result

    # 행을 탐색하다가 더 큰 값이 나와 더 이상 탐색하지 않아도 될 때
    # 다시 자신을 호출한 함수로 돌아가도록 한다.
    if sum_ij > result:
        return

    # 만약 마지막 행까지 다 돌았다.
    if i == N:
        result = sum_ij

    else:
        for j in range(N):        # j = 0, 1, 2
            if visited[j] == 0:   # 만약 j의 값이 0이다.(방문하지 않았다)
                visited[j] = 1    # 방문할 예정이니 1로 바꿔준다.

                #이제 아래 행으로 이동하고, 그 값을 저장하겠다.
                find_minsum(i+1, N, sum_ij + arr[i][j])
                visited[j] = 0



T = int(input())

for test_case in range(1, T + 1):
    N = int(input())  #3
    arr= [list(map(int,input().split()))for _ in range(N)]

    # 탐색을 했는지 안했는지 판단할 리스트
    visited = [0] * N

    result = float('inf') #제일 큰 값으로 저장

    # i = 0부터 탐색할 것이고, i가 N이 되면 종료할 것이고, 값의 합을 0으로 가정하고 시작
    find_minsum(0, N, 0)

    print(f'# {test_case} {result}')