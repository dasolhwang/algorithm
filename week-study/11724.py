import sys

n,e=input().split()
n=int(n);e=int(e)

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
def dfs(graph):
    visited = []
    cnt=0
    stack=[1]

    while  stack:
    	node = stack.pop(len(stack)-1)
    	
#    while graphs: 
#    	cnt+=1

	stack=[1]
     while stack:
         node = stack.pop(len(stack)-1)
         print("node",node)
         if node not in visited:
             visited.append(node)
             print("visited",visited)
             neighbors = sorted(graphs[node], reverse=True)
             stack += neighbors
     print(visited not in [x for x in range(1,n+1)])

	




print(dfs(graphs))