f = open("input.txt","r")
'''
1 은 이동 가능
0 은 이동 못함
(0,0)에서 (N,M)까지 가는 최단거리

101111
101010
101011
111011
'''

N,M = map(int, f.readline().split())

temp = []
for _ in range(N):
    temp.append(list(map(int, list(f.readline().strip()))))
dx = [0,0,1,-1]
dy = [1,-1,0,0]

queue = []
visited = [[False for _ in range(M)] for _ in range(N)]

queue = []
queue.append((0,0))
visited[0][0] = 1
while queue: # BFS
    x, y = queue.pop(0)
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if (0<=newX<N)&(0<=newY<M):
            if visited[newX][newY] == 0 and temp[newX][newY] == 1:
                visited[newX][newY] = visited[x][y] + 1
                queue.append((newX,newY))
