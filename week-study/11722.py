import sys
import array

leng1 = sys.stdin.readline().strip()
leng2 = sys.stdin.readline().strip()

x = leng2.split()
x = list(map(int,x))

print(x)

D=[None]*len(x)

def decrese(x):
	for i in range(len(D)):
		D[i] = 1
		for j in range(i):
			if(x[j]>x[i])&(D[i]<D[j]+1):
				D[i] = D[j]+1
	return max(D)


print(decrese(x))


