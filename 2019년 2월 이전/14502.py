f = open("input.txt", "r")
n,m = f.readline().split()
n = int(n); m = int(m)
K = []

for _ in range(n):
    K.append(list(map(int,f.readline().split())))

def virus_cnt(D):

    for i in range(n):
        for j in range(m):
            if i == 0:
                if j == 0:
                    if D[i][j] == 0:
                        if (D[i][j+1] == 2) | (D[i+1][j]==2):
                            D[i][j] = 2
                if j == m-1:
                    if D[i][j] == 0:
                        if (D[i+1][j]==2) | (D[i][j-1]):
                            D[i][j] = 2
                else:
                    if D[i][j] == 0:
                        if (D[i][j-1] == 2) | (D[i][j+1] == 2) | (D[i+1][j] == 2):
                            D[i][j] = 2
            if i == n-1:
                if j == 0:
                    if D[i][j] == 0:
                        if (D[i][j+1] == 2) | (D[i-1][j] == 2):
                            D[i][j] = 2
                if j == m-1:
                    if D[i][j] == 0:
                        if (D[i][j-1]==2) | (D[i-1][j]):
                            D[i][j] = 2
                else:
                    if D[i][j] == 0:
                        if (D[i][j-1] == 2) | (D[i][j+1] == 2) | (D[i-1][j] == 2):
                            D[i][j] = 2

            else:
                if j == 0:
                    if D[i][j] == 0:
                        if (D[i-1][j] == 2) | (D[i+1][j]==2) | (D[i][j+1]==2):
                            D[i][j] = 2
                if j == m-1:
                    if D[i][j] == 0:
                        if (D[i+1][j]==2) | (D[i][j-1]) | (D[i-1][j]==2):
                            D[i][j] = 2
                else:
                    if D[i][j] == 0:
                        if (D[i][j-1] == 2) | (D[i][j+1] == 2) | (D[i+1][j] == 2) | (D[i-1][j] == 2):
                            D[i][j] = 2

    return sum(D,[]).count(2)

for i in range(n):
    for j in range(m):
        result = K
        print(result)
        if result[i][j] == 0:
            result[i][j] = 1
            a = virus_cnt(result)
            print(a)
            result[i][j] = 0

'''
result = K
if result[0][2] == 0:
    result[0][2] = 1
print(K)
print(virus_cnt(result))
'''
'''
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''

'''
2 2 2 2 1 1 2
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
# D[i][j] 에 1 넣었을 경우에 얻어지는 안전영역 수

'''
2 0  2 1
0 0  1 0
0 0  0 0


0 0   1 0
2 0   2 1
0 0   1 0

0 0  0 0
0 0  1 0
2 0  2 1
'''