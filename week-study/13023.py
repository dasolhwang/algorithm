import sys
q = lambda: sys.stdin.readline().strip()

A=[None]*8
B=[None]*8
edge=[[]]*8

for i in range(8):
	x = q()
	A[i] = int(x[:1])
	B[i] = int(x[2:])
	edge[i] = [A[i],B[i]]


edge = edge[1:]

for i in range(7):
	for j in range(1):
		print(edge[i])