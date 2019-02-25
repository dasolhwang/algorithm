f = open("input.txt", "r")
n, min, max = map(int, f.readline().split())

temp = []
for _ in range(n):
    temp.append(list(map(int, f.readline().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x,y,visited):
    sum = temp[x][y]; cnt = 1;
    index = [[x,y]]
    queue = [[x,y]]
    while queue != []:
        queue = queue[1:]
        visited[x][y] = True
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if (0<=newX<n)&(0<=newY<n):
                if (min <= abs(temp[x][y]-temp[newX][newY]) <= max)&(visited[newX][newY] is False)&([newX,newY] not in index):
                    queue.append([newX, newY])
                    sum += temp[newX][newY]
                    cnt += 1
                    index.append([newX,newY])
        if queue != []:
            x = queue[0][0]
            y = queue[0][1]
    if cnt != 1:
        return (int(sum/cnt), index)
    return False

ans = 0
while True:
    change = False
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                value = bfs(i,j,visited)
                if value is not False:
                    newValue = value[0]
                    index = value[1]
                    for idx in index:
                        temp[idx[0]][idx[1]] = newValue
                    change = True
    if not change:
        break
    ans += 1
print(ans)