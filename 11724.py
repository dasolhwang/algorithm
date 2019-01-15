f = open("input.txt", "r")
n, m = map(int, f.readline().split())

graphs = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,f.readline().split())
    graphs[a-1].append(b-1)
    graphs[b-1].append(a-1)

check = [False]*n

def dfs(x):
    check[x] = True
    for y in graphs[x]:
        if check[y] == False:
            dfs(y)
ans = 0
for i in range(n):
    if not check[i]:
        dfs(i)
        ans += 1
print(ans)