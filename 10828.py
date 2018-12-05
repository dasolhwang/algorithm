import sys

n = sys.stdin.readline().strip() # strip()공백 제거
stack = []

for _ in range(n):
	temp = sys.stdin.readline().strip()

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

