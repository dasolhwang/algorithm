# 시간초과

import sys

q = sys.stdin.readline().strip().split(' ')
q = list(map(int,q))

N = q[0]
M = q[1]
queue = [x+1 for x in range(N)]
result=[]

for j in range(N):
	for i in range(M-1):
		queue.append(queue[0])
		queue = queue[1:]
	result.append(queue[0])
	queue = queue[1:]


k = '<'+str(result)[1:20]+'>'
print(k)
