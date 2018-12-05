import sys

n,e,v=input().split()
n=int(n);e=int(e);v=int(v)

adj = [[0 for x in range(n)]for y in range(n)] # 인접 행렬
for k in range(e):
	i, j= input().split()
	i = int(i)-1; j = int(j)-1
	adj[i][j]=1
	adj[j][i]=1


graphs = {} # 인접 리스트
for i in range(n):
	 graphs[i+1] = [idx+1 for idx,val in enumerate(adj[i]) if val==1]
print(graphs)



# 깊이 우선 탐색
def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop(len(stack)-1)
        if node not in visited:
            visited.append(node)
            neighbors = sorted(graphs[node], reverse=True)
            stack += neighbors
            
    return visited
 
# 너비 우선 탐색
def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = sorted(graphs[node])
            queue += neighbors
            
    return visited
 

print (' '.join(map(str,dfs(graphs,v))))
print (' '.join(map(str,bfs(graphs,v))))