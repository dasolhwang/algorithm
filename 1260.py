
f = open("input.txt", "r")
n, e, v = f.readline().split()
n = int(n) # 정점
e = int(e) # 간선
v = int(v) #

# 인접 행렬 n x n
adj = [[0 for _ in range(n)] for _ in range(n)]
for i in range(e):
    a, b = f.readline().split()
    a = int(a)-1
    b = int(b)-1
    adj[a][b] = 1
    adj[b][a] = 1
print(adj)

# 그래프
graphs={}
for i in range(n):
    graphs[i+1] = [idx+1 for idx, val in enumerate(adj[i]) if val == 1]
print(graphs)


# 깊이우선탐색(스택)
def DFS(graphs, v):
    visited = []
    stack = [v]
    while stack:
        current = stack.pop()
        if current not in visited:
            stack += sorted(graphs[current], reverse=True)
            visited.append(current)
    return visited

# 너비우선탐색(큐)
def BFS(graphs, v):
    visited = []
    queue = [v]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            queue += sorted(graphs[current])
            visited.append(current)
    return visited

print(DFS(graphs, v))
print(BFS(graphs, v))
