import sys
import array

q = int(sys.stdin.readline().strip())

def Bottom_Up(x):
	D = [None]*(x+1)
	D[1]=0
	for i in range(2,x+1):
		D[i] = D[i-1] + 1

		if(i%2==0)&(D[i]>D[int(i/2)]+1):
			D[i] = D[int(i/2)]+1
		if(i%3==0)&(D[i]>D[int(i/3)]+1):
			D[i] = D[int(i/3)]+1

	return D[x]

print(Bottom_UP(q))
