f = open("input.txt", "r")
n, m = map(int, f.readline().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, f.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

check = [False for _ in range(n)]

def dfs(x):
    check[x] = True
    for i in graph[x]:
        if check[i] == False:
            dfs(i)

ans = 0
for i in range(n):
    if not check[i]:
        dfs(i)
        ans += 1
print(ans)