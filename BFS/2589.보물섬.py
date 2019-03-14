from collections import deque
from sys import stdin
input = stdin.readline

n,m = map(int, input().split())
temp = [list(input().strip()) for _ in range(n)]
def bfs(x,y):
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque()
    maximum = 0
    queue.append((x,y))
    while len(queue) != 0:
        x, y = queue.popleft()
        for dx, dy in dir:
            newX, newY = x+dx, y+dy
            if 0<=newX<n and 0<=newY<m:
                if visited[newX][newY]==0 and temp[newX][newY]=="L":
                    visited[newX][newY] = visited[x][y]+1
                    maximum = max(maximum, visited[newX][newY])
                    queue.append((newX,newY))
    return maximum

ans = 0
for i in range(n):
    for j in range(m):
        if temp[i][j]=="L":
            visited = [[0]*m for _ in range(n)]
            ans = max(ans, bfs(i,j))
print(ans)
