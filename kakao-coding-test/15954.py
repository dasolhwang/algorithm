import math
f = open("input.txt", "r")
N, K = map(int, f.readline().split())
prefer = list(map(int, f.readline().split()))
std = []

if K == 1:
    print(0)
else:
    for k in range(K, N+1):
        temp = []
        for i in range(N-k+1):
            print(prefer[i:i+k])
            m = sum(prefer[i:i+k])/k
            v = sum(map(lambda x: (x-m)**2, prefer[i:i+k]))/k
            temp.append(v)
        std.append(min(temp))
    print(math.sqrt(min(std)))
# Python3 시간초과
# Pypy3 성공