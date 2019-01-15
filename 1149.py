f = open("input.txt", "r")
n = int(f.readline())

R = []
for i in range(n):
    R.append(list(map(int, f.readline().split())))

D =[[0 for i in range(3)] for j in range(n)]
D[0] = R[0]

for i in range(1, n):
    D[i][0] = R[i][0] + min(D[i-1][1], D[i-1][2])
    D[i][1] = R[i][1] + min(D[i-1][0], D[i-1][2])
    D[i][2] = R[i][2] + min(D[i-1][0], D[i-1][1])

print(min(D[n-1]))