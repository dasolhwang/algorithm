# 2
# 17
'''
뒤가 0이면 1만 올수이꼬
뒤가 9면 8만 올숭수잇고

'''

f = open("input.txt", "r")
n = int(f.readline())
D = [[0 for i in range(10)] for j in range(n+1)]
print(D)
# 길이 / 마지막수


for i in range(1, 10):
    D[1][i] = 1

for i in range(2, n+1):
    for j in range(0, 10):
        if j == 0:
            D[i][j] = D[i-1][j+1]
        elif j == 9:
            D[i][j] = D[i-1][j-1]
        else:
            D[i][j] = D[i-1][j-1] + D[i-1][j+1]
ans = 0
for i in range(0,10):
    ans += D[n][i]
print(ans)