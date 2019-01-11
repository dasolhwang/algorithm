'''
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.
'''

'''
0 1 2 3 4 5 6 7 8 9
10 9 8 7 6 5 4 3 2 1


'''
f = open("input.txt", "r")
n = int(f.readline())

d = [[0 for i in range(10)] for j in range(n)]

for i in range(10):
    d[0][i] = 1

for i in range(1, n):
    for j in range(10):
        result = 0
        for k in range(j+1):
            result += d[i-1][k]
        d[i][j] = result

print(sum(d[n-1]))

