# 나누기(/) 몫(//) 나머지(%)
# 소수 : 1과 자기 자신으로밖에 나누어지지 않는 정수 (1제외)

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
