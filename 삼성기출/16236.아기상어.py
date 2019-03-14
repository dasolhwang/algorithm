f = open("input.txt","r")
n = int(f.readline())

temp = []
for _ in range(n):
    temp.append(list(map(int,f.readline().split())))

for i in range(len(temp)):
    for j in range(len(temp)):
        if temp[i][j] == 9:
            x,y = i,j
            temp[i][j] = 0
            break

# 먹을 수 있는 큐, 기본 큐 두개만들어라~~~
def search(x,y,eat,shark_size):
    pass

'''
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
'''
search(x,y,0,2)














'''
    position = []
    position.append((x, y))

    while position:
        x,y = position.pop()
        for dx,dy in (-1,0),(0,-1),(1,0),(0,1): #위/왼/아래/오
            newX = x+dx
            newY = y+dy

            if (0<=newX<n)&(0<=newY<n):
                if 0 < temp[newX][newY] < shark_size:
                    eat += 1
                    temp[x][y] = 0
                    if eat == shark_size:
                        shark_size += 1
                        eat = 0
'''





















'''
f = open("input.txt","r")
n = int(f.readline())

temp = []
for _ in range(n):
    temp.append(list(map(int,f.readline().split())))


def search(x,y,eat,shark_size):
    position = []
    while True:
        for dx,dy in (-1,0),(0,-1),(1,0),(0,1):
            newX, newY = x+dx, y+dy
            if (0 <= newX < n)&(0 <= newY < n):
                if (temp[newX][newY] <= shark_size)&([newX,newY] not in position):
                    position.append([newX,newY])
                    if (0 < temp[newX][newY]) & (temp[newX][newY] < shark_size):
                        eat += 1
                        print("Eat:", eat)
                        if eat == shark_size:
                            shark_size += 1
                            eat = 0
                        return newX, newY, eat, shark_size
        x = position[0][0]
        y = position[0][1]

        position = position[1:]

# 상어의 위치 찾기
for i in range(len(temp)):
    for j in range(len(temp)):
        if temp[i][j] == 9:
            shark = [i,j]
            break
x = shark[0]; y = shark[1];
eat = 0; size = 2; cnt = 0

while True:
    temp[x][y] = 0
    if sum(sum(temp,[])) == 0:
        break
    newx, newy, eat, size = search(x,y,eat,size)
    print([newx,newy] , "크기:",size)
    print(temp)
    cnt += (abs(newx-x) + abs(newy-y))
    x = newx
    y = newy
    temp[x][y] = 9
print(cnt)

'''