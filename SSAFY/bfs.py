arr = 'ABC'
N = 3
Q = [[]]

while Q:
    node = Q.pop(0)
    if len(node) == N:
        print(node)
    else:
        for val in arr:
            if val in node:
                continue
            Q.append(node+[val])