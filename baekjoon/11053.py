'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
'''

f = open("input.txt", "r")
n = int(f.readline())

temp = f.readline().split()
temp = [int(i) for i in temp]
D = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if (temp[j] < temp[i]) & (D[i] < D[j]+1):
            D[i] = D[j] + 1
print(max(D))
