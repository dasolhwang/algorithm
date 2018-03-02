import sys

q = lambda: sys.stdin.readline().strip()
n = int(q())
stack = []

for _ in range(n):
	temp = q()
	if temp[:4]=='push':
		stack.append(int(temp[4:]))
	
	elif temp=='pop':
		if len(stack)>0: print(stack.pop())
		else: print(-1)
	
	elif temp=='top':
		if len(stack)>0: print(stack[-1])
		else: print(-1)
	
	elif temp=='empty':
		if len(stack)==0: print(1)
		else: print(0)
	
	elif temp=='size':
		print(len(stack))

		
