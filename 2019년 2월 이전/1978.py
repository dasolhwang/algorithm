# 나누기(/) 몫(//) 나머지(%)

import sys
n = int(sys.stdin.readline())
x = map(int, sys.stdin.readline().split())
cnt = 0
for i in x:
    k = i
    if k == 1:
        cnt += 0
    else:
        cnt += 1
        for i in range(2, k):
            if k % i == 0:
                cnt -= 1
                break
print(cnt)


import sys
_ = int(sys.stdin.readline())
x = map(int, sys.stdin.readline().split())

cnt = 0
for i in x:
    if i > 1:
        cnt += 1
        for j in range(2, i):
            if i % j == 0:
                cnt -= 1
                break
print(cnt)
