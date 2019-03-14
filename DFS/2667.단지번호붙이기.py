f = open("input.txt", "r")
n = int(f.readline())
temp = []
for _ in range(n):
    temp.append(list(map(int,list(f.readline().strip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0 for _ in range(n)] for _ in range(n)]
'''
0120100
0220101
1220101
0000111
0100000
0111110
0111000
'''

def dfs(x,y):
    global cnt

    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if (0<=newX<n)&(0<=newY<n):
            if (visited[newX][newY]==0)&(temp[newX][newY]==1):
                visited[newX][newY] = 1
                cnt +=1
                dfs(newX,newY)

result = []
for i in range(n):
    for j in range(n):
        if (visited[i][j] == 0) & (temp[i][j] == 1):
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)
            result.append(cnt)


print(len(result))
for p in sorted(result):
    print(p)



