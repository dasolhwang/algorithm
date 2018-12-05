import sys

leng1 = sys.stdin.readline().strip()
leng2 = sys.stdin.readline().strip()

x = leng2.split()
x = list(map(int,x))
re_x = list(map(int,list(reversed(x))))

D1 = [None]*len(x)
D2 = [None]*len(x)

for i in range(len(D1)):
	D1[i] = 1
	for j in range(i):
		if(x[j]<x[i])&(D1[i]<D1[j]+1):
			D1[i] = D1[j]+1

for i in range(len(D2)):
	D2[i] = 1
	for j in range(i):
		if(re_x[j]<re_x[i])&(D2[i]<D2[j]+1):
			D2[i] = D2[j]+1

print(max(list(map(lambda x,y: x+y, D1, list(reversed(D2)))))-1)
