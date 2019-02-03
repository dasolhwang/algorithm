f = open("input.txt", "r")
n = int(f.readline())

temp = []
for i in range(n):
    temp.append(list(map(int, f.readline().split())))

def solve(member):
    all = [i for i in range(n)]
    link_team = []
    for i in all:
        if i not in member:
            link_team.append(i)

    start = 0
    link = 0
    for i in member:
        for j in member:
            start += temp[i][j]
    for i in link_team:
        for j in link_team:
            link += temp[i][j]
    return abs(start - link)




visited = [0 for i in range(n)]

def dfs(i, cnt):
    if cnt != int(n/2):
        visited[i] = 1
        for j in range(1, n):
            if i+j < n:
                dfs(i+j, cnt + 1)
                visited[i+j] = 0
    else:
        start_team = []
        link_team = []
        for i in visited:
            if i == 1:
                start_team.append(i)
            else:
                link_team.append(i)

        start = 0
        link = 0
        for i in start_team:
            for j in start_team:
                start += temp[i][j]
        for i in link_team:
            for j in link_team:
                link += temp[i][j]
        return abs(start - link)

for i in range(n):
    print(dfs(i, 0))