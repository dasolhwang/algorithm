f = open("input.txt", "r")
n = int(f.readline())
temp = []
for _ in range(n):
    temp.append(list(map(int,list(f.readline().strip()))))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[0 for _ in range(n)] for _ in range(n)]


def dfs(i,j,cnt):
    
    pass




