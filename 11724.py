f = open("input.txt", "r")
n, m = map(int, f.readline().split())

adj = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = f.readline().split()
    a = int(a)-1
    b = int(b)-1
    adj[a][b] = 1
    adj[b][a] = 1

graphs = {}
for i in range(n):
    graphs[i+1] = [idx+1 for idx, val in enumerate(adj[i]) if val==1]

def DFS(graphs, v):
    stack = [v]
    visited = []
    cnt = 0
    while len(visited) != n:
        cnt += 1
        while stack:
            current = stack.pop()
            if current not in visited:
                stack += sorted(graphs[current])
                visited.append(current)
        if len(visited) != n:
            stack = []


    return cnt

print(DFS(graphs, 1))