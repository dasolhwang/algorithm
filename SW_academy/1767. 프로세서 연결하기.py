f = open("input.txt", "r")

T = int(f.readline())


for _ in range(1):
    n = int(f.readline())
    temp = []
    for _ in range(n):
        temp.append(list(map(int, f.readline().split())))

import copy

copy = copy.deepcopy(temp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def Connected(x, y, dir):
    bool = True  # 끝까지 전원 연결 가능 여부
    while bool:
        x += dx[dir]
        y += dy[dir]
        if (x <= 0)|(y <= 0)|(x >= n)|(y >= n):
            break
        if temp[x][y] != 0:
            bool = False
            break
    return bool

def DFS(N, result):

    x = N//n # 0 ~ n-1
    y = N%n # 0 ~ n-1
    print(x,y)
    if x >= n:
        return result

    for k in range(4):
        if Connected(x,y,k):
            nx=x
            ny=y
            R=0
            while True:
                nx += dx[k]
                ny += dy[k]
                if (nx <= 0) | (ny <= 0) | (nx >= n) | (ny >= n):
                    break
                temp[nx][ny] = 2 # 전선 연결
                R += 1
            DFS(N+1, result+R)
            nx = x
            ny = y
            while True:
                nx += dx[k]
                ny += dy[k]
                if (nx <= 0) | (ny <= 0) | (nx >= n) | (ny >= n):
                    break
                temp[nx][ny] = 0 # 백트레

    DFS(N+1, result)


k = DFS(0,0)
print(k)
