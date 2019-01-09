'''
x2개를 temp[2] + D[2]
3개를 temp[3] + D[1]
n개를 temp[n]
'''

f = open("input.txt", "r")
n = int(f.readline())
temp = f.readline().split()
temp = [int(i) for i in temp]
D = [0]*(n)

for i in range(1, n):
    for j in range(1, i):
        print(i, i-j, j)
        D[i] = max(D[i], D[i-j]+temp[j])
print(D)