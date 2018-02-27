import sys
import array

q = int(sys.stdin.readline().strip())

D = [None]*(q+1)

def tile_2xn(x):
	D[0]=1
	D[1]=1
	for i in range(2,x+1):
		D[i]=D[i-1]+D[i-2]
	return D[x]
		
print(tile_2xn(q)%10007)