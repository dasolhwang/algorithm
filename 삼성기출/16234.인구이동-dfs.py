f = open("input.txt", "r")
n, min, max = map(int, f.readline().split())

temp = []
for _ in range(n):
    temp.append(list(map(int, f.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x,y,index,visited):
    global sum
    global cnt
    visited[x][y] = True
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if (0<=newX<n)&(0<=newY<n):
            if (min <= abs(temp[x][y]-temp[newX][newY]) <= max)&(visited[newX][newY] is False):
                index.append([newX,newY])
                sum += temp[newX][newY]
                cnt += 1
                dfs(newX, newY, index, visited)

ans = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    change = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                index = []
                cnt = 0
                sum = 0
                dfs(i,j,index,visited)
                if cnt != 0:
                    cnt += 1
                    sum += temp[i][j]
                    index.append([i,j])
                    change = True
                    for idx in index:
                        temp[idx[0]][idx[1]] = int(sum/cnt)
    if not change:
        break
    ans += 1

print(ans)
