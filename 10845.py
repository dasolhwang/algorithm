import sys

r = lambda: sys.stdin.readline().strip()
n = int(r())

stack =[]

for _ in range(n):
	command = q()
	if command[:4] == 'push':
		stack.append(int(command[4:]))
	
	elif command == 'pop':
		if len(stack) ==0: print(-1)
		else: print(stack[0]); stack = stack[1:]

	elif command == 'front':
		if len(stack)>0: print(stack[0])
		else: print(-1)
	elif command == 'back':
		if len(stack)>0: print(stack[-1])
		else: print(-1)
	elif command == 'size': print(len(stack))
	elif command == 'empty':
		if len(stack) == 0: print(1)
		else: print(0)
