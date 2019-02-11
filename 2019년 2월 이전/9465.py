f = open("input.txt", "r")
k = int(f.readline())

for _ in range(k):
    n = int(f.readline())
    a = f.readline().split()
    b = f.readline().split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
# 행열
    A = [a,b]
    D = [[0 for i in range(3)] for j in range(n)]

    D[0][1] = A[0][0]
    D[0][2] = A[1][0]

    for i in range(1, n):
        D[i][0] = max(D[i-1][0],D[i-1][1],D[i-1][2])
        D[i][1] = max(D[i-1][0],D[i-1][2]) + A[0][i]
        D[i][2] = max(D[i-1][0],D[i-1][1]) + A[1][i]

    print(max(D[n-1]))


