f = open("input.txt","r")
N,M = map(int, f.readline().split())

# 1월 29일 못품

'''
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 0 6 0
0 0 0 0 0 0
'''

temp = []
for i in range(N):
    temp.append(list(map(int,f.readline().split())))


def update(i, cctv, copy):
    x = cctv[1]
    y = cctv[2]
    i = (i%4)
    if i == 0:
        for j in range(x+1, M):
            if copy[j][y] == 6:
                break
            copy[x][y] = -1
    if i == 1:
        for j in range(y-1, 0):
            if copy[x][j] == 6:
                break
            copy[x][y] = -1
    if i == 2:
        for j in range(x-1, 0):
            if copy[j][y] == 6:
                break
            copy[x][y] = -1
    if i == 3:
        for j in range(y+1, N):
            if copy[x][j] == 6:
                break
            copy[x][y] = -1


def dfs(cctv_idx):
    import copy

    if cctv_idx == len(cctv):
        answer = 0
        for i in range(N):
            for j in range(M):
                if cop[i][j] == 0:
                    answer += 1
        return answer

    for i in range(rotation[cctv[cctv_idx][0]-1]):
        cop = copy.deepcopy(temp)
        if cctv[cctv_idx][0] == 1:
            update(i, cctv[cctv_idx], cop)
        elif cctv[cctv_idx][0] == 2:
            update(i, cctv[cctv_idx], cop)
            update(i+2, cctv[cctv_idx], cop)
        elif cctv[cctv_idx][0] == 3:
            update(i, cctv[cctv_idx], cop)
            update(i+1, cctv[cctv_idx], cop)
        elif cctv[cctv_idx][0] == 4:
            update(i, cctv[cctv_idx], cop)
            update(i+1, cctv[cctv_idx], cop)
            update(i+2, cctv[cctv_idx], cop)
        elif cctv[cctv_idx][0] == 5:
            update(i, cctv[cctv_idx], cop)
            update(i+1, cctv[cctv_idx], cop)
            update(i+2, cctv[cctv_idx], cop)
            update(i+3, cctv[cctv_idx], cop)

        dfs(cctv_idx+1)


rotation = [4,2,4,4,1]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < temp[i][j] < 6:
            cctv.append([temp[i][j], i, j])
print(cctv)

dfs(0)



'''
def cctv_region(temp, idx, d):
    x = idx[1]
    y = idx[2]
    while (0 <= x <= N-1) & (0 <= y <= M-1):
        if temp[x][y] != 6:
            temp[x][y] = "#"
            x += d[0]
            y += d[1]

print(cctv_region([1,2,2],[1,0]))

def solve(i):
    if idx[i] == 1:
        d = [[1,0],[0,1]]
        for j in d:
            cctv_region(temp, idx[i], j)
            solve(idx+1)

    if idx[i] == 2:
        d = [[1,0],[-1,0]]
        for j in d:
            cctv_region(temp, idx[i], j)
            solve(idx+1)

    if idx[i] == 3:
    if idx[i] == 4:
    if idx[i] == 5:
'''