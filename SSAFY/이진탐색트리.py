N = 6
# tree = [0, 4, 2, 6, 1, 3, 5]
tree = [0] * (N + 1)
cnt = 1
def dfs(v):
    global cnt
    if v > N :  #없는거임
        return
    dfs(v*2)
    tree[v] = cnt
    cnt += 1
    # print(tree[v], end= ' ')
    dfs(v*2 + 1)

dfs(1)
print(tree[1:])