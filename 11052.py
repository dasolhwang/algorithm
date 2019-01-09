'''
x2개를 temp[2] + D[2]
3개를 temp[3] + D[1]
n개를 temp[n]

5
10 9 8 7 6

'''

f = open("input.txt", "r")
n = int(f.readline())
temp = f.readline().split()
temp = [int(i) for i in temp]
temp = [0]+temp
D = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        D[i] = max(D[i], temp[j] + D[i-j])
print(D[n])