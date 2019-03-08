f = open("input.txt", "r")
n = int(f.readline())
temp = []
for _ in range(n):
    temp.append(list(map(int,list(f.readline().strip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, queue, cnt):
    queue.append((x, y))
    while len(queue) != 0:
        x, y = queue.pop()
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
            if (0 <= newX < n) & (0 <= newY < n):
                if (visited[newX][newY] == 0) & (temp[newX][newY] == 1):
                    queue.append((newX, newY))
                    visited[newX][newY] = 1
                    cnt += 1
    return cnt + 1



queue = []
visited = [[0 for _ in range(n)] for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        if (visited[i][j] == 0) & (temp[i][j] == 1):
            visited[i][j] = 1
            cnt = bfs(i, j, queue, 0)
            result.append(cnt)

print(len(result))
for p in sorted(result):
    print(p)