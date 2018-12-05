import sys
import array

leng1 = sys.stdin.readline().strip()
leng2 = sys.stdin.readline().strip()

x = leng2.split()
x = list(map(int,x))

D=[None]*len(x)

def largest(x):
	for i in range(len(D)):
		D[i] = x[i]
		for j in range(i):
			if(x[j]<x[i])&(D[i]<D[j]+x[i]):
				D[i]=D[j]+x[i]
	return max(D)


print(largest(x))
