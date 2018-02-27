import sys

r = lambda: sys.stdin.readline().strip()
n = int(r())

def function(n):
	queue=[]

	for i in range(n):
		command = r()

		if command[:4]=='push':
			queue.append(int(command[5:]))

		if command=='pop':
			queue=queue[1:]
			return queue

		if command=='size':
			return len(queue)

		if command=='empty':
			if len(queue)==0:
				return 1
			else: return 0

		if command=='front':
			if len(queue)==0:
				return -1
			else:
				return queue[0]

		if command=='back':
			if len(queue)==0:
				return -1
			else:
				return queue[len(queue)]


for i in range(n):
	print(function(n))
		
