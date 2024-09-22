import sys
sys.stdin = open('input.txt')

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

def tictok(who, cnt):
    global X_player, O_player

    # 만약 cnt가 4가 된다면 해당 플레이어가 이기는 것
    if cnt == 4:
        return who






T = int(input())

for test_case in range(1, T + 1):
    game = []
    #[['X', 'O', 'X', '.'], ['O', 'X', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]

    for _ in range(4):
        arr = list(input())
        game.append(arr)

    M = ['X', 'O']

    X_player = 0
    O_player = 0

    for i in M:  # i = X, O
        tictok(i, 0)



print(f'#{test_case} {game}')

