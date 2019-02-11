import math

f = open("input.txt","r")
n = int(f.readline())
temp = list(map(int, f.readline().split()))

# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# a = 3
if temp[0] == 1:

'''
시간초과
다시
'''



if temp[0] == 2:
    temp = temp[1:]
    result = 0
    visited = []
    for t in temp:
        n -= 1
        visited.append(t)
        for j in sorted(temp):
            if (j < t) & (j not in visited):
                result += math.factorial(n)
    print(result+1)




