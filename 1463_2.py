import sys
import array

q = int(sys.stdin.readline().strip())

D = [None]*(q+1)

 
def Top_Down(x):
	if (x==0)|(x==1):
		return 0

	temp=[]
	temp.append(Top_Down(x-1))
	if(x%2==0):
		temp.append(Top_Down(x//2))
	if(x%3==0):
		temp.append(Top_Down(x//3))
	
	D[x] = min(temp)+1
	return D[x]
		
print(Top_Down(q))
