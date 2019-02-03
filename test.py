f = open("input.txt", "r")
n,m = f.readline().split()
n = int(n); m = int(m)
K = []

for _ in range(n):
    K.append(list(map(int,f.readline().split())))

x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]

# 바이러스 퍼지기
stack = copy.deepcopy(virus)
while stack:
    temp = stack.pop()
    for i in dir:
        next_x, next_y = temp[0] + i[0], temp[1] + i[1]
        if -1 < next_x < n and -1 < next_y < m and test_area[next_x][next_y] == 0:
            test_area[next_x][next_y] = 2
            stack.append([next_x, next_y])
            safe_area -= 1


def virus_infect(i, j, D):
    for k in range(4):
        newX = x[k] + i
        newY = y[k] + j
        if (0 <= newX < n) & (0 <= newY < m):
            if D[newX][newY] == 0:
                D[newX][newY] = 2
                virus_infect(newX, newY, D)

visited = []
for i in range(n):
    for j in range(m):
        if K[i][j] == 0:
            visited.append([i,j])

start = []
for i in range(n):
    for j in range(m):
        if K[i][j] == 2:
            start.append([i,j])

import copy
result = copy.deepcopy(K)
temp = []

for i in range(len(visited)):
    for j in range(i+1, len(visited)):
        for k in range(j+1, len(visited)):
            result[visited[i][0]][visited[i][1]] = 1
            result[visited[j][0]][visited[j][1]] = 1
            result[visited[k][0]][visited[k][1]] = 1
            for l in range(len(start)):
                virus_infect(start[l][0], start[l][1], result)
            temp.append(sum(result,[]).count(0))
            result = copy.deepcopy(K)
print(max(temp))
