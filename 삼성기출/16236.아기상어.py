f = open("input.txt","r")
n = int(f.readline())

temp = []
for _ in range(n):
    temp.append(list(map(int,f.readline().split())))

dx = [-1,0,0,1]
dy = [0,-1,1,0]

# 상어의 위치 찾기
for i in range(len(temp)):
    for j in range(len(temp)):
        if temp[i][j] == 9:
            shark = [i,j]
            break

def search(x,y,eat,shark_size):
    position = []
    while True:
        for i in range(4):
            newX = x + dx[i]
            newY = y + dy[i]
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
