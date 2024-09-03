arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']


# path 출력 함수
def print_name():
    print(path, end=' / ')
    print('{ ', end='')
    for i in range(3):
        if path[i] == 'O':
            print(name[i], end=' ')
    print('}')


def run(lev):
    # 3개를 뽑았을 때 출력
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        run(lev + 1)
        path.pop()


run(0)



# def get_sub(tar):
#     for i in range(N):
#
# arr = ['a', 'b', 'c', 'd', 'e']
# N = len(arr)
#
# for tar in range(0, 1 << N):
#     get_sub(tar)
#
#

# arr = ['1', '2', '3', '4', '5', '6']
# path = []
# n = 3  # 3개를 던지겠다
#
# def run(lev, start):
#     if lev == n:
#         print(path)
#         return
#
#     for i in range(start, 6):
#         path.append(arr[i])
#         run(lev+1, i)
#         path.pop()
#
# run(0, 0)
#

