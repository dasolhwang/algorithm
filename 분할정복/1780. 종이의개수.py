f = open("input.txt", "r")
n = int(f.readline())
temp = []
for _ in range(n):
    temp.append(list(map(int, f.readline().split())))

def same(x,y,k): # (x,y)에서부터 크기가 k인 배열 같은 수인지 확인
    for i in range(x,x+k):
        for j in range(y,y+k):
            if temp[x][y] != temp[i][j]:
                return False
    return True

def solve(x,y,k,cnt): # 배열이 같은 수면 cnt += 1
    if same(x,y,k):
        cnt[temp[x][y] + 1] += 1

    else: # 배열이 다른 수면 9개의 배열로 쪼개서
        m = int(k/3)
        for i in range(3):
            for j in range(3):
                solve(x+i*m,y+j*m,m, cnt)

cnt = [0 for i in range(3)]
solve(0,0,n,cnt)
for i in cnt:
    print(i)