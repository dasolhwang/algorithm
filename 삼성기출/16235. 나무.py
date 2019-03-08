f = open("input.txt","r")
N,M,K = map(int, f.readline().split())

B = []
for _ in range(N):
    B.append(list(map(int, f.readline().split())))

A = [[5 for _ in range(N)] for _ in range(N)]

from collections import deque
tree = deque()
for _ in range(M):
    x,y,z = map(int, f.readline().split())
    tree.append([x-1,y-1,z])

dr = [-1,1,0,0,-1,1,-1,1]
dc = [0,0,1,-1,1,-1,-1,1]


for _ in range(K):
    i = 0
    extra = deque()
    while (len(tree) != 0)&(i <= len(tree)-1):
        r = tree[i][0]
        c = tree[i][1]
        if A[r][c] >= tree[i][2]:
            A[r][c] -= tree[i][2]
            tree[i][2] += 1
            if tree[i][2] % 5 == 0:
                for dir in range(8):
                    newR = r + dr[dir]
                    newC = c + dc[dir]
                    if (0 <= newR < N) & (0 <= newC < N):
                        extra.appendleft([newR, newC, 1])
                        i += 1
            i += 1
        else:
            A[r][c] += int(tree[i][2]/2)
            tree.remove(tree[i])
    print("Tree: ",tree, "extra: ",extra)
    if len(extra)!=0:
        extra.extend(tree)
        tree = extra
        print(tree)
    for i in range(N):
        for j in range(N):
            A[i][j] += B[i][j]
print(len(tree))