f = open("input.txt","r")
n = int(f.readline())
temp = []
for _ in range(n):
    temp.append(list(map(int,f.readline().split())))

dx = [-1,0,0,1]
dy = [0,-1,1,0]

'''
아기상어 위치에서 거리 1인 애들 보고 없으면 거리 2인 애들 보고, ....
'''